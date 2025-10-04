#!/usr/bin/env bash
# POSIX shell / Bash init script for the Django project.
# Usage: ./scripts/init.sh [venv_name]

VENV_NAME=${1:-.venv}
ROOT_DIR="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT_DIR" || exit 1

echo "Initializing project in: $ROOT_DIR"

if [ ! -d "$VENV_NAME" ]; then
  echo "Creating virtual environment: $VENV_NAME"
  python3 -m venv "$VENV_NAME"
else
  echo "Virtual environment already exists: $VENV_NAME"
fi

# Activate for this script run
# shellcheck disable=SC1091
source "$VENV_NAME/bin/activate"

echo "Upgrading pip and installing requirements (if present)"
python -m pip install --upgrade pip
if [ -f requirements.txt ]; then
  pip install -r requirements.txt
else
  echo "No requirements.txt found — skipping pip install"
fi

if [ -f manage.py ]; then
  echo "Running migrations"
  python manage.py migrate
else
  echo "manage.py not found — are you in the project root?"
fi

echo "Initialization finished. To activate the venv in your shell run: source $VENV_NAME/bin/activate"