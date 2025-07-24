# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Overview
FastAPI backend application that scrapes Serie A football statistics from fbref.com and exposes them via REST API endpoints.

## Architecture
- **main.py**: FastAPI app initialization and route registration
- **controllers/recupero_dati.py**: API endpoint definitions for data retrieval
- **services/scraper.py**: Web scraping logic for fbref.com Serie A statistics using BeautifulSoup and Pydantic models

## Key Models
- `SquadStats`: Pydantic model for team statistics (rank, wins, losses, goals, etc.)
- `GenericTableRow`: Flexible table row structure for additional data
- `LeagueData`: Container for all scraped league data

## Commands
```bash
# Install dependencies
pip install -r requirements.txt

# Run development server
uvicorn main:app --reload --host 0.0.0.0 --port 8000

# API endpoint
GET /recupera-dati - Returns scraped Serie A statistics
```

## Data Source
Scrapes from: https://fbref.com/en/comps/11/Serie-A-Stats