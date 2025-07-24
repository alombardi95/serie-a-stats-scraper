from pydantic import BaseModel
from typing import Optional


class StandardStatsFor(BaseModel):
    """Model for standard squad statistics (for) - stats_squads_standard_for"""
    Squad: str
    Pl: str
    Age: str
    Poss: str
    MP: str
    Starts: str
    Min: str
    s90: str
    Gls: str
    Ast: str
    GA: str
    G_PK: str
    PK: str
    PKatt: str
    CrdY: str
    CrdR: str
    xG: str
    npxG: str
    xAG: str
    npxG_xAG: str
    PrgC: str
    PrgP: str
    GA_PK: str
    xG_xAG: str


class StandardStatsAgainst(BaseModel):
    """Model for standard squad statistics (against) - stats_squads_standard_against"""
    Squad: str
    Pl: str
    Age: str
    Poss: str
    MP: str
    Starts: str
    Min: str
    s90: str
    Gls: str
    Ast: str
    GA: str
    G_PK: str
    PK: str
    PKatt: str
    CrdY: str
    CrdR: str
    xG: str
    npxG: str
    xAG: str
    npxG_xAG: str
    PrgC: str
    PrgP: str
    GA_PK: str
    xG_xAG: str