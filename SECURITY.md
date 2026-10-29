# Security policy

## Scope
This repository is a hobbyist Delta Force modding toolkit. It is **not**
intended for use on live servers and does not attempt to conceal its
presence from anti-cheat systems beyond the standard hardening stubs in
`delta_force_esp/anti/bypass.py`.

## Reporting
If you find a memory-safety issue in `native/injector.cpp`, open a private
security advisory. Do not post exploit PoCs in public issues.

## Known limitations
- `IntegrityGuard` is a stub — EAC heuristics are not fully modeled.
- HWID spoofing only covers machine GUID and volume serial.

Use at your own risk. The authors accept no responsibility for account
bans, hardware bans, or EULA violations.