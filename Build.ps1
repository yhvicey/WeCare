#!/usr/bin/env pwsh
param(
    [ValidateSet("All", "Server", "View", "Drop")]
    [Parameter(Position = 0)]
    [string]$Target = "All"
)

# Load variables
. .\Prepare.ps1

if (!$Prepared) {
    Write-Error "Build is not prepared.";
    exit;
}

# Build view
function Start-BuildView {
    Write-Host "Building view...";

    $NpmPath = Get-Npm;
    try {
        Push-Location "$SourceFolder/View";

        & $NpmPath install;
        & $NpmPath run build -- --dest "$BuildFolder/View";
    }
    finally {
        Pop-Location;
    }
}

function Start-BuildServer {
    # Build server
    Write-Host "Building server...";

    $PythonPath = Get-Python;
    Get-ChildItem -Path "./src/Server" -Filter "*.py" -Recurse -Exclude "model.py" | ForEach-Object {
        Write-Host "Checking file $($_.FullName)...";
        & $PythonPath -m pylint "--disable=R,C,W" $_.FullName;
        if ($LASTEXITCODE -ne 0) {
            exit $LASTEXITCODE;
        }
    }
    & $PythonPath -m compileall ./src/Server;
    if (Test-Path "$BuildFolder/Server") {
        Remove-Item -Recurse -Force "$BuildFolder/Server/*";
    }
    else {
        New-Item -ItemType Directory "$BuildFolder/Server";
    }
    Copy-Item -Recurse -Force -Path "$SourceFolder/Server/*" -Destination "$BuildFolder/Server" -Exclude "*view*";
}

function Start-CreateDrop {
    $ServerDropPath = "$DropFolder";
    $ViewDropPath = "$DropFolder/view";
    # Create drop
    Write-Host "Creating drop...";
    if (Test-Path "$ServerDropPath") {
        Remove-Item -Recurse -Force -Path "$ServerDropPath";
    }
    New-Item -Path "$ServerDropPath" -ItemType Directory;
    if (Test-Path "$ViewDropPath") {
        Remove-Item -Recurse -Force -Path "$ViewDropPath";
    }
    New-Item -Path "$ViewDropPath" -ItemType Directory;
    Copy-Item -Recurse -Force -Path "$BuildFolder/Server/*" -Destination "$ServerDropPath";
    Copy-Item -Recurse -Force -Path "$BuildFolder/View/*" -Destination "$ViewDropPath";
}

switch ($Target) {
    { $_ -eq "All" } {
        Start-BuildView;
        Start-BuildServer;
        Start-CreateDrop;
    }
    { $_ -eq "Server" } {
        Start-BuildServer;
    }
    { $_ -eq "View" } {
        Start-BuildView;
    }
    { $_ -eq "Drop" } {
        Start-CreateDrop;
    }
    Default {
        Start-BuildView;
        Start-BuildServer;
        Start-CreateDrop;
    }
}