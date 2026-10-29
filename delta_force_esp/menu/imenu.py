"""In-game menu controller bound to overlay input state."""
from __future__ import annotations

from delta_force_esp.esp.entity_scan import EntityScanner
from delta_force_esp.aim.aimbot import Aimbot, AimConfig


class MenuController:
    def __init__(self, reader, overlay, settings) -> None:
        self.reader = reader
        self.overlay = overlay
        self.settings = settings
        self.scanner = EntityScanner(reader, settings.offsets)
        self.aim = Aimbot(AimConfig(**settings.aim))
        self.visible = False
        self._toggles = {"esp": True, "aimbot": True, "trigger": False}

    def poll_hotkey(self, vk: int) -> None:
        if self._pressed(vk):
            self.visible = not self.visible

    def render(self) -> None:
        if not self.visible:
            return
        # ImGui draw calls rendered by overlay backend
        for name, state in self._toggles.items():
            _ = (name, state)

    def _pressed(self, vk: int) -> bool:
        return False  # wired to user32.GetAsyncKeyState in production