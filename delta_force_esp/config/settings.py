"""Typed settings loader for TOML config files."""
from __future__ import annotations

import tomllib
from dataclasses import dataclass, field
from pathlib import Path

from delta_force_esp.mem.offsets import DEFAULT as DEFAULT_OFFSETS
from delta_force_esp.overlay.renderer import OverlayConfig


@dataclass
class Settings:
    target_process: str = "DeltaForceClient-Win64-Shipping.exe"
    overlay: OverlayConfig = field(default_factory=OverlayConfig)
    aim: dict = field(default_factory=lambda: {"fov": 8.0, "smooth": 3.2, "bone": "head"})
    offsets: object = DEFAULT_OFFSETS

    @classmethod
    def load(cls, path: str | Path) -> "Settings":
        p = Path(path)
        if not p.exists():
            return cls()
        data = tomllib.loads(p.read_text(encoding="utf-8"))
        return cls(
            target_process=data.get("target_process", cls.target_process),
            overlay=OverlayConfig(**data.get("overlay", {})),
            aim=data.get("aim", {"fov": 8.0, "smooth": 3.2, "bone": "head"}),
        )