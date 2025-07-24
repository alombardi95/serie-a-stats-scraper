from pydantic import BaseModel
from typing import Optional


class LeagueStanding(BaseModel):
    """Model for Serie A league table - results2024-2025111_overall"""
    Rk: str
    Squad: str
    MP: str
    W: str
    D: str
    L: str
    GF: str
    GA: str
    GD: str
    Pts: str
    Pts_MP: str
    xG: Optional[str] = None
    xGA: Optional[str] = None
    xGD: Optional[str] = None
    xGD_90: Optional[str] = None
    Attendance: Optional[str] = None
    Top_Team_Scorer: Optional[str] = None
    Goalkeeper: Optional[str] = None
    Notes: Optional[str] = None


class HomeAwayStats(BaseModel):
    """Model for home/away statistics - results2024-2025111_home_away"""
    Rk: str
    Squad: str
    MP: str
    W: str
    D: str
    L: str
    GF: str
    GA: str
    GD: str
    Pts: str
    Pts_MP: str
    xG: Optional[str] = None
    xGA: Optional[str] = None
    xGD: Optional[str] = None
    xGD_90: Optional[str] = None