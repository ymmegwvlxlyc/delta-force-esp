@echo off
setlocal
cd /d "%~dp0"
python -m delta_force_esp.bootstrap
endlocal