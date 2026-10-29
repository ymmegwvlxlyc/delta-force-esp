"""Read-only process memory wrapper for Delta Force client (UE5)."""
from __future__ import annotations

import ctypes
import ctypes.wintypes as wt
from typing import Optional


PROCESS_VM_READ = 0x0010
PROCESS_QUERY_INFORMATION = 0x0400


class ProcessReader:
    def __init__(self, process_name: str) -> None:
        self.process_name = process_name
        self.pid: int = 0
        self.base_address: int = 0
        self._handle: Optional[int] = None
        self._k32 = ctypes.WinDLL("kernel32", use_last_error=True)

    def attach(self) -> None:
        pid = self._find_pid(self.process_name)
        if not pid:
            raise ProcessLookupError(f"process {self.process_name!r} not found")
        self.pid = pid
        h = self._k32.OpenProcess(PROCESS_VM_READ | PROCESS_QUERY_INFORMATION, False, pid)
        if not h:
            raise OSError(ctypes.get_last_error(), "OpenProcess failed")
        self._handle = h
        self.base_address = self._module_base("DeltaForceClient-Win64-Shipping.exe")

    def read(self, address: int, size: int) -> bytes:
        buf = ctypes.create_string_buffer(size)
        n = ctypes.c_size_t(0)
        ok = self._k32.ReadProcessMemory(
            self._handle, ctypes.c_void_p(address), buf, size, ctypes.byref(n)
        )
        if not ok or n.value != size:
            raise OSError(ctypes.get_last_error(), f"ReadProcessMemory @ 0x{address:X}")
        return buf.raw

    def read_ptr(self, address: int) -> int:
        return int.from_bytes(self.read(address, 8), "little")

    def detach(self) -> None:
        if self._handle:
            self._k32.CloseHandle(self._handle)
            self._handle = None

    def _find_pid(self, name: str) -> int:
        raise NotImplementedError("toolhelp32 snapshot — see _tlhelp in this module")

    def _module_base(self, name: str) -> int:
        raise NotImplementedError("module enumeration — see _modules.py")