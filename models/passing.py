from pydantic import BaseModel
from typing import Optional


class PassingStatsFor(BaseModel):
    """Model for passing statistics (for) - stats_squads_passing_for"""
    Squad: str
    Pl: str
    s90: str
    Cmp: str
    Att: str
    Cmp_pct: str
    TotDist: str
    PrgDist: str
    Ast: str
    xAG: str
    xA: str
    A_xAG: str
    KP: str
    _1_3: str
    PPA: str
    CrsPA: str
    PrgP: str


class PassingStatsAgainst(BaseModel):
    """Model for passing statistics (against) - stats_squads_passing_against"""
    Squad: str
    Pl: str
    s90: str
    Cmp: str
    Att: str
    Cmp_pct: str
    TotDist: str
    PrgDist: str
    Ast: str
    xAG: str
    xA: str
    A_xAG: str
    KP: str
    _1_3: str
    PPA: str
    CrsPA: str
    PrgP: str


class PassingTypesFor(BaseModel):
    """Model for passing types (for) - stats_squads_passing_types_for"""
    Squad: str
    Pl: str
    s90: str
    Att: str
    Live: str
    Dead: str
    FK: str
    TB: str
    Sw: str
    Crs: str
    TI: str
    CK: str
    In: str
    Out: str
    Str: str
    Cmp: str
    Off: str
    Blocks: str


class PassingTypesAgainst(BaseModel):
    """Model for passing types (against) - stats_squads_passing_types_against"""
    Squad: str
    Pl: str
    s90: str
    Att: str
    Live: str
    Dead: str
    FK: str
    TB: str
    Sw: str
    Crs: str
    TI: str
    CK: str
    In: str
    Out: str
    Str: str
    Cmp: str
    Off: str
    Blocks: str


class GCAFor(BaseModel):
    """Model for goal creation actions (for) - stats_squads_gca_for"""
    Squad: str
    Pl: str
    s90: str
    SCA: str
    SCA90: str
    PassLive: str
    PassDead: str
    TO: str
    Sh: str
    Fld: str
    Def: str
    GCA: str
    GCA90: str


class GCAAgainst(BaseModel):
    """Model for goal creation actions (against) - stats_squads_gca_against"""
    Squad: str
    Pl: str
    s90: str
    SCA: str
    SCA90: str
    PassLive: str
    PassDead: str
    TO: str
    Sh: str
    Fld: str
    Def: str
    GCA: str
    GCA90: str