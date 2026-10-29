"""Silent / smooth aimbot with FOV gating and bone targeting."""
from __future__ import annotations

import math
from dataclasses import dataclass

from delta_force_esp.core.math3d import Vec3, angle_delta


@dataclass
class AimConfig:
    fov: float = 8.0
    smooth: float = 3.2
    bone: str = "head"
    visible_only: bool = True
    key: int = 0x02  # RMB


class Aimbot:
    def __init__(self, cfg: AimConfig) -> None:
        self.cfg = cfg
        self._locked_target: int | None = None

    def pick_target(self, origin: Vec3, view_angles: Vec3, candidates) -> int | None:
        best, best_delta = None, self.cfg.fov
        for ent in candidates:
            if self.cfg.visible_only and not ent.visible:
                continue
            target = ent.bone(self.cfg.bone)
            if target is None:
                continue
            d = angle_delta(view_angles, origin.look_at(target))
            if d < best_delta:
                best, best_delta = ent.handle, d
        self._locked_target = best
        return best

    def step(self, current: Vec3, target: Vec3) -> Vec3:
        want = current.look_at(target)
        delta = want - current
        factor = 1.0 / max(self.cfg.smooth, 1.0)
        return Vec3(
            current.x + delta.x * factor,
            current.y + delta.y * factor,
            current.z + delta.z * factor,
        )