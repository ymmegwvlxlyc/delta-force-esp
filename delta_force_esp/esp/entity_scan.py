"""Entity scanning — walks GUObjectArray, filters live players."""
from __future__ import annotations

from typing import Iterator

from delta_force_esp.mem.reader import ProcessReader
from delta_force_esp.mem.offsets import Offsets
from delta_force_esp.core.models.player import PlayerEntity


class EntityScanner:
    def __init__(self, reader: ProcessReader, offsets: Offsets) -> None:
        self.reader = reader
        self.off = offsets

    def iter_players(self) -> Iterator[PlayerEntity]:
        level = self.reader.read_ptr(self.reader.base_address + self.off.uworld)
        if not level:
            return
        actors = self.reader.read_ptr(level + self.off.actor_array)
        count = int.from_bytes(self.reader.read(level + self.off.actor_count, 4), "little")
        for i in range(min(count, 4096)):
            actor = self.reader.read_ptr(actors + i * 8)
            if not actor:
                continue
            try:
                ent = PlayerEntity.from_actor(self.reader, actor, self.off)
            except OSError:
                continue
            if ent and ent.is_alive:
                yield ent