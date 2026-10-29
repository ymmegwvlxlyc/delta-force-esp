"""Minimal 3D math used by ESP projection and aimbot."""
from __future__ import annotations

import math
from dataclasses import dataclass


@dataclass(frozen=True)
class Vec3:
    x: float
    y: float
    z: float

    def __sub__(self, o: "Vec3") -> "Vec3":
        return Vec3(self.x - o.x, self.y - o.y, self.z - o.z)

    def length(self) -> float:
        return math.sqrt(self.x * self.x + self.y * self.y + self.z * self.z)

    def look_at(self, target: "Vec3") -> "Vec3":
        d = target - self
        yaw = math.degrees(math.atan2(d.y, d.x))
        pitch = math.degrees(math.atan2(d.z, math.hypot(d.x, d.y)))
        return Vec3(pitch, yaw, 0.0)


def angle_delta(a: Vec3, b: Vec3) -> float:
    dy = (b.y - a.y + 180.0) % 360.0 - 180.0
    dp = b.x - a.x
    return math.hypot(dp, dy)


def world_to_screen(world: Vec3, matrix: list[float], wh: tuple[int, int]) -> tuple[float, float] | None:
    w = matrix[3] * world.x + matrix[7] * world.y + matrix[11] * world.z + matrix[15]
    if w < 0.001:
        return None
    x = (matrix[0] * world.x + matrix[4] * world.y + matrix[8] * world.z + matrix[12]) / w
    y = (matrix[1] * world.x + matrix[5] * world.y + matrix[9] * world.z + matrix[13]) / w
    return ((wh[0] / 2) * (1 + x), (wh[1] / 2) * (1 - y))