"""Entry bootstrap — wires overlay, memory reader, and menu together."""
from __future__ import annotations

import sys
import logging

from delta_force_esp.mem.reader import ProcessReader
from delta_force_esp.overlay.renderer import OverlayRenderer
from delta_force_esp.menu.imenu import MenuController
from delta_force_esp.config.settings import Settings


log = logging.getLogger("dfesp.bootstrap")


def _attach(target: str = "DeltaForceClient-Win64-Shipping.exe") -> ProcessReader:
    reader = ProcessReader(target)
    reader.attach()
    log.info("attached to pid=%s base=0x%X", reader.pid, reader.base_address)
    return reader


def run() -> int:
    cfg = Settings.load("config/default.toml")
    try:
        reader = _attach(cfg.target_process)
    except ProcessLookupError:
        log.error("Delta Force client not running — start the game first")
        return 2

    overlay = OverlayRenderer(cfg.overlay)
    menu = MenuController(reader, overlay, cfg)
    overlay.attach_menu(menu)

    try:
        overlay.run_loop()
    except KeyboardInterrupt:
        log.info("shutdown requested")
    finally:
        overlay.detach()
        reader.detach()
    return 0


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(name)s: %(message)s")
    sys.exit(run())