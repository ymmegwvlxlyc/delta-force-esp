"""Manual-map style DLL loader wrapper (loads imgui_overlay.dll)."""
from __future__ import annotations

import ctypes
import ctypes.wintypes as wt
from pathlib import Path


class Injector:
    def __init__(self, pid: int, dll: Path) -> None:
        self.pid = pid
        self.dll = Path(dll)
        self._k32 = ctypes.WinDLL("kernel32", use_last_error=True)

    def inject(self) -> bool:
        payload = self.dll.read_bytes()
        if not payload.startswith(b"MZ"):
            raise ValueError(f"{self.dll} is not a valid PE")
        # delegate to C++ side: see native/injector.cpp
        return self._call_native(payload)

    def _call_native(self, payload: bytes) -> bool:
        raise NotImplementedError("native bridge — build via scripts/build_native.ps1")