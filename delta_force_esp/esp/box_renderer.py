"""Screen-space bounding box + skeleton ESP drawing primitives."""
from __future__ import annotations

from dataclasses import dataclass

from delta_force_esp.core.math3d import Vec3, world_to_screen
from delta_force_esp.core.models.player import PlayerEntity


@dataclass
class BoxStyle:
    color: tuple[int, int, int, int] = (0, 255, 90, 220)
    thickness: float = 1.4
    draw_skeleton: bool = True
    draw_health: bool = True


class BoxRenderer:
    def __init__(self, style: BoxStyle, view_matrix: list[float]) -> None:
        self.style = style
        self.vm = view_matrix

    def project(self, world: Vec3, screen_wh: tuple[int, int]) -> tuple[float, float] | None:
        return world_to_screen(world, self.vm, screen_wh)

    def draw(self, draw_ctx, player: PlayerEntity, screen_wh: tuple[int, int]) -> None:
        head = self.project(player.head_pos, screen_wh)
        feet = self.project(player.feet_pos, screen_wh)
        if not head or not feet:
            return
        h = feet[1] - head[1]
        w = h * 0.42
        x0 = head[0] - w / 2
        draw_ctx.rect(x0, head[1], w, h, self.style.color, self.style.thickness)
        if self.style.draw_health:
            draw_ctx.bar(x0 - 5, head[1], 3, h, player.health / 100.0, (255, 60, 60, 255))