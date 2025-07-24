from pydantic import BaseModel
from typing import Optional


class KeeperStatsFor(BaseModel):
    """Model for goalkeeper statistics (for) - stats_squads_keeper_for"""
    Squad: str
    Pl: str
    MP: str
    Starts: str
    Min: str
    s90: str
    GA: str
    GA90: str
    SoTA: str
    Saves: str
    Save_pct: str
    W: str
    D: str
    L: str
    CS: str
    CS_pct: str
    PKatt: str
    PKA: str
    PKsv: str
    PKm: str


class KeeperStatsAgainst(BaseModel):
    """Model for goalkeeper statistics (against) - stats_squads_keeper_against"""
    Squad: str
    Pl: str
    MP: str
    Starts: str
    Min: str
    s90: str
    GA: str
    GA90: str
    SoTA: str
    Saves: str
    Save_pct: str
    W: str
    D: str
    L: str
    CS: str
    CS_pct: str
    PKatt: str
    PKA: str
    PKsv: str
    PKm: str


class KeeperAdvancedFor(BaseModel):
    """Model for advanced goalkeeper statistics (for) - stats_squads_keeper_adv_for"""
    Squad: str
    Pl: str
    s90: str
    GA: str
    PKA: str
    FK: str
    CK: str
    OG: str
    PSxG: str
    PSxG_SoT: str
    PSxG_plus_minus: str
    _90: str
    Cmp: str
    Att: str
    Cmp_pct: str
    Att_GK: str
    Thr: str
    Launch_pct: str
    AvgLen: str
    Opp: str
    Stp: str
    Stp_pct: str
    OPA: str
    OPA_90: str
    AvgDist: str


class KeeperAdvancedAgainst(BaseModel):
    """Model for advanced goalkeeper statistics (against) - stats_squads_keeper_adv_against"""
    Squad: str
    Pl: str
    s90: str
    GA: str
    PKA: str
    FK: str
    CK: str
    OG: str
    PSxG: str
    PSxG_SoT: str
    PSxG_plus_minus: str
    _90: str
    Cmp: str
    Att: str
    Cmp_pct: str
    Att_GK: str
    Thr: str
    Launch_pct: str
    AvgLen: str
    Opp: str
    Stp: str
    Stp_pct: str
    OPA: str
    OPA_90: str
    AvgDist: str