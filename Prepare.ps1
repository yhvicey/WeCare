# Variables used during whole build process.
$RootFolder = $PSScriptRoot;
$BuildFolder = "$RootFolder/build/";
$DropFolder = "$RootFolder/drop/";
$SourceFolder = "$RootFolder/src/";

function Get-Npm {
    $NpmPath = $(Get-Command -ErrorAction SilentlyContinue -Name "npm").Path;
    if (!$NpmPath) {
        Write-Host "Please install npm first. See https://nodejs.org/en/download/ for more information.";
        exit;
    }
    return $NpmPath;
}

function Get-Python {
    $PythonPath = $(Get-Command -ErrorAction SilentlyContinue -Name "python3").Path;
    if (!$PythonPath) {
        $PythonPath = $(Get-Command -ErrorAction SilentlyContinue -Name "python").Path;
        if (!$PythonPath) {
            Write-Host "Please install python first. See https://www.python.org for more information.";
            exit;
        }
    }
    return $PythonPath;
}

$Prepared = $True;