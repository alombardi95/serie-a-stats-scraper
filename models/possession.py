from pydantic import BaseModel
from typing import Optional


class PossessionStatsFor(BaseModel):
    """Model for possession statistics (for) - stats_squads_possession_for"""
    Squad: str
    Pl: str
    Poss: str
    s90: str
    Touches: str
    Def_Pen: str
    Def_3rd: str
    Mid_3rd: str
    Att_3rd: str
    Att_Pen: str
    Live: str
    Att: str
    Succ: str
    Succ_pct: str
    Tkld: str
    Tkld_pct: str
    Carries: str
    TotDist: str
    PrgDist: str
    PrgC: str
    _1_3: str
    CPA: str
    Mis: str
    Dis: str
    Rec: str
    PrgR: str


class PossessionStatsAgainst(BaseModel):
    """Model for possession statistics (against) - stats_squads_possession_against"""
    Squad: str
    Pl: str
    Poss: str
    s90: str
    Touches: str
    Def_Pen: str
    Def_3rd: str
    Mid_3rd: str
    Att_3rd: str
    Att_Pen: str
    Live: str
    Att: str
    Succ: str
    Succ_pct: str
    Tkld: str
    Tkld_pct: str
    Carries: str
    TotDist: str
    PrgDist: str
    PrgC: str
    _1_3: str
    CPA: str
    Mis: str
    Dis: str
    Rec: str
    PrgR: str


class PlayingTimeFor(BaseModel):
    """Model for playing time statistics (for) - stats_squads_playing_time_for"""
    Squad: str
    Pl: str
    Age: str
    MP: str
    Min: str
    Mn_MP: str
    Min_pct: str
    s90: str
    Starts: str
    Mn_Start: str
    Compl: str
    Subs: str
    Mn_Sub: str
    unSub: str
    PPM: str
    onG: str
    onGA: str
    plus_minus: str
    plus_minus_90: str
    onxG: str
    onxGA: str
    xG_plus_minus: str
    xG_plus_minus_90: str


class PlayingTimeAgainst(BaseModel):
    """Model for playing time statistics (against) - stats_squads_playing_time_against"""
    Squad: str
    Pl: str
    Age: str
    MP: str
    Min: str
    Mn_MP: str
    Min_pct: str
    s90: str
    Starts: str
    Mn_Start: str
    Compl: str
    Subs: str
    Mn_Sub: str
    unSub: str
    PPM: str
    onG: str
    onGA: str
    plus_minus: str
    plus_minus_90: str
    onxG: str
    onxGA: str
    xG_plus_minus: str
    xG_plus_minus_90: str