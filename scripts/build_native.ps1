# Build the native injector + overlay DLL shipped with delta-force-esp
param(
    [string]$Configuration = "Release",
    [string]$Platform = "x64"
)

$ErrorActionPreference = "Stop"
$root = Split-Path -Parent $PSScriptRoot

Push-Location "$root\native"
try {
    cmake -B build -A $Platform -DCMAKE_BUILD_TYPE=$Configuration
    cmake --build build --config $Configuration
    Copy-Item "build\$Configuration\dfesp_injector.dll" "$root\delta_force_esp\bin\" -Force
    Write-Host "Native build OK -> delta_force_esp\bin\dfesp_injector.dll"
}
finally { Pop-Location }