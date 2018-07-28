#!/usr/bin/env pwsh

# Load variables
. .\Prepare.ps1

if (!$Prepared) {
    Write-Error "Run is not prepared.";
    exit;
}

# Check build result

if (!(Test-Path "$DropFolder/server.py")) {
    Write-Host "No drop files found, run ./Build.ps1 first.";
    exit;
}

# Run server
Write-Host "Running server...";
$PythonPath = Get-Python;
try {
    Push-Location "$DropFolder";
    & $PythonPath "$DropFolder/server.py"
}
finally {
    Pop-Location;
}