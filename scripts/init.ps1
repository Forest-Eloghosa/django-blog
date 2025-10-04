<#
PowerShell initialization script for the Django project.
Usage (PowerShell):
  ./scripts/init.ps1        # uses default venv name .venv
  ./scripts/init.ps1 -venvName "myenv"

Notes:
- Activating a venv inside a script does not persist to your interactive shell.
  After running this script, activate the venv manually with:
    .\.venv\Scripts\Activate.ps1
#>
param(
    [string]$venvName = ".venv"
)

# Move to script directory (project root)
$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Definition
Set-Location $scriptDir

Write-Host "Initializing project in: $PWD"

# Create virtual environment if missing
if (-not (Test-Path $venvName)) {
    Write-Host "Creating virtual environment: $venvName"
    python -m venv $venvName
} else {
    Write-Host "Virtual environment already exists: $venvName"
}

# Attempt to activate for the duration of this script (does not persist)
$activateScript = Join-Path $venvName 'Scripts\Activate.ps1'
if (Test-Path $activateScript) {
    Write-Host "Activating virtual environment for script run"
    & $activateScript
} else {
    Write-Host "Activation script not found; you'll need to activate manually: .\$venvName\Scripts\Activate.ps1"
}

# Upgrade pip and install requirements
Write-Host "Upgrading pip and installing requirements (if present)"
python -m pip install --upgrade pip
if (Test-Path 'requirements.txt') {
    pip install -r requirements.txt
} else {
    Write-Host "No requirements.txt found — skipping pip install"
}

# Run Django migrations
if (Test-Path 'manage.py') {
    Write-Host "Running migrations"
    python manage.py migrate
} else {
    Write-Host "manage.py not found — are you in the project root?"
}

Write-Host "Initialization finished. To activate the venv in your shell run:`n .\$venvName\Scripts\Activate.ps1"