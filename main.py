from fastapi import FastAPI
from controllers.recupero_dati import router as recupero_dati_router

app = FastAPI(title="Degli Betting - Backend Scraping Serie A")

app.include_router(recupero_dati_router) 