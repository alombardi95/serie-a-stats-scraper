#!/usr/bin/env python3
"""
Script per eseguire il debug dump delle tabelle Serie A.
Genera un file JSON con tutte le tabelle lette per analisi e debug.
"""

from services.scraper import TeamDataScraper
import sys

def main():
    """Esegue il debug dump delle tabelle Serie A."""
    try:
        url = "https://fbref.com/en/comps/11/Serie-A-Stats"
        scraper = TeamDataScraper(url)
        
        print("📊 Avvio scraping per debug dump...")
        filename = scraper.debug_dump_to_file("debug_tables_dump.json")
        
        # Leggi il file per mostrare un riassunto
        import json
        with open(filename, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        print(f"✅ Debug dump completato: {filename}")
        print(f"📈 Statistiche squadre: {data['metadata']['total_squad_stats']} squadre")
        print(f"📋 Tabelle trovate: {data['metadata']['total_tables']}")
        print("📝 Nomi tabelle:")
        for table_name in data['metadata']['table_names']:
            print(f"   - {table_name}")
            
    except Exception as e:
        print(f"❌ Errore durante il debug dump: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()