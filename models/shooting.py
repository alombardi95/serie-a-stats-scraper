from pydantic import BaseModel
from typing import Optional


class ShootingStatsFor(BaseModel):
    """Model for shooting statistics (for) - stats_squads_shooting_for"""
    Squad: str
    Pl: str
    s90: str
    Gls: str
    Sh: str
    SoT: str
    SoT_pct: str
    Sh_90: str
    SoT_90: str
    G_Sh: str
    G_SoT: str
    Dist: str
    FK: str
    PK: str
    PKatt: str
    xG: str
    npxG: str
    npxG_Sh: str
    G_xG: str
    np_G_xG: str


class ShootingStatsAgainst(BaseModel):
    """Model for shooting statistics (against) - stats_squads_shooting_against"""
    Squad: str
    Pl: str
    s90: str
    Gls: str
    Sh: str
    SoT: str
    SoT_pct: str
    Sh_90: str
    SoT_90: str
    G_Sh: str
    G_SoT: str
    Dist: str
    FK: str
    PK: str
    PKatt: str
    xG: str
    npxG: str
    npxG_Sh: str
    G_xG: str
    np_G_xG: str