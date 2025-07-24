from pydantic import BaseModel
from typing import Optional


class MiscellaneousStatsFor(BaseModel):
    """Model for miscellaneous statistics (for) - stats_squads_misc_for"""
    Squad: str
    Pl: str
    s90: str
    CrdY: str
    CrdR: str
    _2CrdY: str
    Fls: str
    Fld: str
    Off: str
    Crs: str
    Int: str
    TklW: str
    PKwon: str
    PKcon: str
    OG: str
    Recov: str
    Won: str
    Lost: str
    Won_pct: str


class MiscellaneousStatsAgainst(BaseModel):
    """Model for miscellaneous statistics (against) - stats_squads_misc_against"""
    Squad: str
    Pl: str
    s90: str
    CrdY: str
    CrdR: str
    _2CrdY: str
    Fls: str
    Fld: str
    Off: str
    Crs: str
    Int: str
    TklW: str
    PKwon: str
    PKcon: str
    OG: str
    Recov: str
    Won: str
    Lost: str
    Won_pct: str