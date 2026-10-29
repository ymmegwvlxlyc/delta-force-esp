"""Triggerbot — fires when crosshair overlaps a valid hitbox."""
from __future__ import annotations

import time

from delta_force_esp.aim.aimbot import AimConfig


class Triggerbot:
    def __init__(self, cfg: AimConfig, delay_ms: int = 25) -> None:
        self.cfg = cfg
        self.delay = delay_ms / 1000.0
        self._last_fire = 0.0

    def should_fire(self, crosshair_target: int | None) -> bool:
        if crosshair_target is None:
            return False
        now = time.monotonic()
        if now - self._last_fire < self.delay:
            return False
        self._last_fire = now
        return True