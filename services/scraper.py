from typing import List, Dict, Any, Type
import requests
import json
from bs4 import BeautifulSoup
from pydantic import BaseModel

from models.schemas import TABLE_SCHEMAS, LeagueStanding

class TeamDataScraper:
    def __init__(self, url: str):
        self.url = url
        self.soup = None

    def fetch(self):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Language': 'it-IT,it;q=0.9,en-US;q=0.8,en;q=0.7',
            'Accept-Encoding': 'gzip, deflate, br',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
        }
        response = requests.get(self.url, headers=headers)
        response.raise_for_status()
        self.soup = BeautifulSoup(response.text, "html.parser")

    def parse_squad_stats(self) -> List[LeagueStanding]:
        table = self.soup.find("table", {"id": "results2024-2025111_overall"})
        if not table:
            table = self.soup.find("table")
        results = []
        if not table:
            return results
        
        tbody = table.find("tbody")
        if not tbody:
            return results
            
        for row in tbody.find_all("tr"):
            cells = row.find_all(["th", "td"])
            if len(cells) < 19:
                continue
            
            # Map cells to LeagueStanding fields
            data = {
                "Rk": cells[0].get_text(strip=True),
                "Squad": cells[1].get_text(strip=True),
                "MP": cells[2].get_text(strip=True),
                "W": cells[3].get_text(strip=True),
                "D": cells[4].get_text(strip=True),
                "L": cells[5].get_text(strip=True),
                "GF": cells[6].get_text(strip=True),
                "GA": cells[7].get_text(strip=True),
                "GD": cells[8].get_text(strip=True),
                "Pts": cells[9].get_text(strip=True),
                "Pts_MP": cells[10].get_text(strip=True),
            }
            
            # Add optional fields if available
            if len(cells) > 11:
                data["xG"] = cells[11].get_text(strip=True) if len(cells) > 11 else None
            if len(cells) > 12:
                data["xGA"] = cells[12].get_text(strip=True) if len(cells) > 12 else None
            if len(cells) > 13:
                data["xGD"] = cells[13].get_text(strip=True) if len(cells) > 13 else None
            if len(cells) > 14:
                data["xGD_90"] = cells[14].get_text(strip=True) if len(cells) > 14 else None
            if len(cells) > 15:
                data["Attendance"] = cells[15].get_text(strip=True) if len(cells) > 15 else None
            if len(cells) > 16:
                data["Top_Team_Scorer"] = cells[16].get_text(strip=True) if len(cells) > 16 else None
            if len(cells) > 17:
                data["Goalkeeper"] = cells[17].get_text(strip=True) if len(cells) > 17 else None
            if len(cells) > 18:
                data["Notes"] = cells[18].get_text(strip=True) if len(cells) > 18 else None
            
            results.append(LeagueStanding(**data))
        return results

    def parse_all_tables(self) -> Dict[str, List[BaseModel]]:
        tables = {}
        for table in self.soup.find_all("table"):
            table_id = table.get("id", "unknown")
            
            # Skip if no schema defined for this table
            if table_id not in TABLE_SCHEMAS:
                continue
                
            model_class = TABLE_SCHEMAS[table_id]
            
            # Find the tbody
            tbody = table.find("tbody")
            if not tbody:
                continue
                
            # Find headers (skip over_header rows)
            headers = []
            for tr in table.find_all("tr"):
                if 'over_header' not in tr.get("class", []):
                    headers = [th.get_text(strip=True) for th in tr.find_all(["th", "td"])]
                    break
                    
            if not headers:
                continue
                
            rows = []
            for row in tbody.find_all("tr"):
                if 'over_header' in row.get("class", []):
                    continue
                    
                cells = row.find_all(["th", "td"])
                if len(cells) != len(headers):
                    continue
                    
                # Create dictionary mapping headers to cell values
                row_data = {headers[i]: cells[i].get_text(strip=True) for i in range(len(headers))}
                
                try:
                    # Create model instance
                    model_instance = model_class(**row_data)
                    rows.append(model_instance)
                except Exception as e:
                    # Skip rows that don't match the schema
                    continue
                    
            tables[table_id] = rows
            
        return tables

    def extract_all(self) -> Dict[str, Any]:
        self.fetch()
        squad_stats = self.parse_squad_stats()
        tables = self.parse_all_tables()
        
        return {
            "squad_stats": [squad.model_dump() for squad in squad_stats],
            "tables": {table_name: [row.model_dump() for row in rows] for table_name, rows in tables.items()}
        }

    def debug_dump_to_file(self, filename: str = "debug_tables_dump.json"):
        """Dump all scraped tables to JSON file for debugging purposes."""
        data = self.extract_all()
        
        # Add metadata
        debug_data = {
            **data,
            "metadata": {
                "url": self.url,
                "total_squad_stats": len(data["squad_stats"]),
                "total_tables": len(data["tables"]),
                "table_names": list(data["tables"].keys())
            }
        }
        
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(debug_data, f, indent=2, ensure_ascii=False)
        
        return filename

def estrai_dati_serie_a() -> Dict[str, Any]:
    url = "https://fbref.com/en/comps/11/Serie-A-Stats"
    scraper = TeamDataScraper(url)
    return scraper.extract_all() 