"""DirectX overlay window renderer (ImGui backend)."""
from __future__ import annotations

from dataclasses import dataclass

from delta_force_esp.esp.box_renderer import BoxRenderer, BoxStyle


@dataclass
class OverlayConfig:
    width: int = 1920
    height: int = 1080
    vsync: bool = False
    menu_hotkey: int = 0x2D  # INSERT


class OverlayRenderer:
    def __init__(self, cfg: OverlayConfig) -> None:
        self.cfg = cfg
        self._menu = None
        self._box = BoxRenderer(BoxStyle(), [0.0] * 16)
        self._running = False

    def attach_menu(self, menu) -> None:
        self._menu = menu

    def run_loop(self) -> None:
        self._running = True
        while self._running:
            self._tick()

    def _tick(self) -> None:
        if self._menu is not None:
            self._menu.poll_hotkey(self.cfg.menu_hotkey)
            self._menu.render()

    def detach(self) -> None:
        self._running = False