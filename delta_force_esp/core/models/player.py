"""Player entity snapshot built from a UE5 actor pointer."""
from __future__ import annotations

from dataclasses import dataclass, field

from delta_force_esp.core.math3d import Vec3
from delta_force_esp.mem.offsets import Offsets


@dataclass
class PlayerEntity:
    handle: int
    team_id: int
    health: float
    head_pos: Vec3
    feet_pos: Vec3
    visible: bool = False
    bones: dict[str, Vec3] = field(default_factory=dict)

    @property
    def is_alive(self) -> bool:
        return self.health > 0.0

    def bone(self, name: str) -> Vec3 | None:
        return self.bones.get(name)

    @classmethod
    def from_actor(cls, reader, actor: int, off: Offsets) -> "PlayerEntity | None":
        health = reader.read(actor + off.health, 4)
        hp = float(int.from_bytes(health, "little"))
        if hp <= 0 or hp > 1000:
            return None
        root = reader.read_ptr(actor + off.actor_root)
        if not root:
            return None
        pos = reader.read(root + 0x150, 12)
        feet = Vec3(*[float(int.from_bytes(pos[i:i + 4], "little", signed=True)) for i in (0, 4, 8)])
        return cls(handle=actor, team_id=0, health=hp, feet_pos=feet, head_pos=feet)