from pydantic import BaseModel
from typing import Optional


class DefenseStatsFor(BaseModel):
    """Model for defensive statistics (for) - stats_squads_defense_for"""
    Squad: str
    Pl: str
    s90: str
    Tkl: str
    TklW: str
    Def_3rd: str
    Mid_3rd: str
    Att_3rd: str
    Att: str
    Tkl_pct: str
    Lost: str
    Blocks: str
    Sh: str
    Pass: str
    Int: str
    Tkl_Int: str
    Clr: str
    Err: str


class DefenseStatsAgainst(BaseModel):
    """Model for defensive statistics (against) - stats_squads_defense_against"""
    Squad: str
    Pl: str
    s90: str
    Tkl: str
    TklW: str
    Def_3rd: str
    Mid_3rd: str
    Att_3rd: str
    Att: str
    Tkl_pct: str
    Lost: str
    Blocks: str
    Sh: str
    Pass: str
    Int: str
    Tkl_Int: str
    Clr: str
    Err: str