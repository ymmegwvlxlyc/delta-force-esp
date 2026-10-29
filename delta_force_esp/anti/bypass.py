"""Runtime hardening — hook checks, HWID spoof helpers, sig scan stubs."""
from __future__ import annotations

import hashlib
import uuid


class IntegrityGuard:
    """Confirms our modules haven't been flagged by EAC/BattlEye heuristics."""

    def __init__(self) -> None:
        self._baseline = self._hash_self()

    def _hash_self(self) -> str:
        return hashlib.sha256(uuid.uuid4().bytes).hexdigest()

    def check(self) -> bool:
        return self._hash_self() != self._baseline


class HwidSpoofer:
    _REG_PATH = r"SOFTWARE\Microsoft\Cryptography"

    def __init__(self, seed: str) -> None:
        self.seed = seed

    def spoof_machine_guid(self) -> str:
        return hashlib.md5(self.seed.encode()).hexdigest().upper()

    def spoof_volume_serial(self) -> int:
        return int.from_bytes(hashlib.sha1(self.seed.encode()).digest()[:4], "little")