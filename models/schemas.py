"""
Complete schema mapping for all 24 Serie A statistics tables
Used for web scraping validation and data structure definition
"""

from typing import Dict, List, Type
from pydantic import BaseModel

from .league_standing import LeagueStanding, HomeAwayStats
from .team_statistics import StandardStatsFor, StandardStatsAgainst
from .goalkeeping import KeeperStatsFor, KeeperStatsAgainst, KeeperAdvancedFor, KeeperAdvancedAgainst
from .shooting import ShootingStatsFor, ShootingStatsAgainst
from .passing import PassingStatsFor, PassingStatsAgainst, PassingTypesFor, PassingTypesAgainst, GCAFor, GCAAgainst
from .defensive import DefenseStatsFor, DefenseStatsAgainst
from .possession import PossessionStatsFor, PossessionStatsAgainst, PlayingTimeFor, PlayingTimeAgainst
from .miscellaneous import MiscellaneousStatsFor, MiscellaneousStatsAgainst

# Schema mapping for all 24 tables
TABLE_SCHEMAS: Dict[str, Type[BaseModel]] = {
    "results2024-2025111_overall": LeagueStanding,
    "results2024-2025111_home_away": HomeAwayStats,
    "stats_squads_standard_for": StandardStatsFor,
    "stats_squads_standard_against": StandardStatsAgainst,
    "stats_squads_keeper_for": KeeperStatsFor,
    "stats_squads_keeper_against": KeeperStatsAgainst,
    "stats_squads_keeper_adv_for": KeeperAdvancedFor,
    "stats_squads_keeper_adv_against": KeeperAdvancedAgainst,
    "stats_squads_shooting_for": ShootingStatsFor,
    "stats_squads_shooting_against": ShootingStatsAgainst,
    "stats_squads_passing_for": PassingStatsFor,
    "stats_squads_passing_against": PassingStatsAgainst,
    "stats_squads_passing_types_for": PassingTypesFor,
    "stats_squads_passing_types_against": PassingTypesAgainst,
    "stats_squads_gca_for": GCAFor,
    "stats_squads_gca_against": GCAAgainst,
    "stats_squads_defense_for": DefenseStatsFor,
    "stats_squads_defense_against": DefenseStatsAgainst,
    "stats_squads_possession_for": PossessionStatsFor,
    "stats_squads_possession_against": PossessionStatsAgainst,
    "stats_squads_playing_time_for": PlayingTimeFor,
    "stats_squads_playing_time_against": PlayingTimeAgainst,
    "stats_squads_misc_for": MiscellaneousStatsFor,
    "stats_squads_misc_against": MiscellaneousStatsAgainst
}

# Export all models for easy import
__all__ = [
    "TABLE_SCHEMAS",
    "LeagueStanding",
    "HomeAwayStats",
    "StandardStatsFor",
    "StandardStatsAgainst",
    "KeeperStatsFor",
    "KeeperStatsAgainst",
    "KeeperAdvancedFor",
    "KeeperAdvancedAgainst",
    "ShootingStatsFor",
    "ShootingStatsAgainst",
    "PassingStatsFor",
    "PassingStatsAgainst",
    "PassingTypesFor",
    "PassingTypesAgainst",
    "GCAFor",
    "GCAAgainst",
    "DefenseStatsFor",
    "DefenseStatsAgainst",
    "PossessionStatsFor",
    "PossessionStatsAgainst",
    "PlayingTimeFor",
    "PlayingTimeAgainst",
    "MiscellaneousStatsFor",
    "MiscellaneousStatsAgainst"
]