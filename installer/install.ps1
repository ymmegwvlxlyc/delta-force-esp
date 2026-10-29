# delta-force-esp installer — drops binaries, registers scheduled task
$installDir = "$env:LOCALAPPDATA\DeltaForceESP"
New-Item -ItemType Directory -Force -Path $installDir | Out-Null
Copy-Item -Recurse "$PSScriptRoot\..\delta_force_esp\*" $installDir -Force
Copy-Item "$PSScriptRoot\launcher.cmd" $installDir -Force

Write-Host "Installed to $installDir"
Write-Host "Run: $installDir\launcher.cmd"
Write-Host ""
Write-Host "NOTE: use only in offline / private matches. Educational purposes only."