# Delta Force Offsets — Build 2026.02.14

Offsets change on every patch. This repo ships the 2026.02.14 set.

## Updating
Run `python scripts/update_offsets.py 2026.02.14-1893`. The script pulls
the community-maintained offset DB and patches `delta_force_esp/mem/offsets.py`.

## Signature notes
- `UWorld` — pattern `48 8B 05 ?? ?? ?? ?? 48 8B 88 ????0000`
- `GUObjectArray` — pattern `48 8B 0D ?? ?? ?? ?? 48 85 C9 74 ?? 8B 41`
- `LocalPawn` — walk from `PlayerController` at `0x2A0`

## Known broken builds
- 2026.01.30 — UE5.4 hotfix shifted `ActorRoot` by `+0x8`