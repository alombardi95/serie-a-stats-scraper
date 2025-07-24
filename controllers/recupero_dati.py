from fastapi import APIRouter
from services.scraper import estrai_dati_serie_a

router = APIRouter()

@router.get("/recupera-dati")
def recupera_dati():
    """Recupera i dati delle squadre di Serie A tramite scraping."""
    return estrai_dati_serie_a() 