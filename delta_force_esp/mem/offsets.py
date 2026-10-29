"""Offsets for Delta Force build 2026.02 — update on patch days."""
from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class Offsets:
    build: str = "2026.02.14-1893"
    uworld: int = 0x08B4C2A8
    game_instance: int = 0x1D8
    local_players: int = 0x38
    local_pawn: int = 0x30
    player_controller: int = 0x2A0
    camera_manager: int = 0x338
    camera_cache: int = 0x1B50
    player_state: int = 0x2B8
    team_id: int = 0x2F0
    actor_root: int = 0x1B0
    health: int = 0x1D0
    mesh_component: int = 0x2C0
    bone_array: int = 0x5D0
    actor_array: int = 0x98
    actor_count: int = 0xA0


DEFAULT = Offsets()