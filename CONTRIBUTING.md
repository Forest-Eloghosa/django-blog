## Contributing to django-blog

Thanks for helping improve this project! This document describes a minimal, safe workflow to set up the project locally, run it, and contribute changes.

### 1) Prerequisites
- Python 3.8+ installed and available as `python` (or adjust commands to `python3`).
- Git installed and configured (name/email).
- Optional: VS Code for editing and using Source Control UI.

### 2) Quick setup (recommended)
Two small helper scripts are provided in `scripts/` to automate environment setup and migrations:

- PowerShell (Windows): `scripts/init.ps1`
- Bash/WSL/macOS: `scripts/init.sh`

Run the matching script for your shell to create a virtual environment, install dependencies from `requirements.txt`, and apply migrations.

PowerShell (from project root):
```powershell
# create .venv, install requirements, run migrations
./scripts/init.ps1
# then activate the venv for interactive work
.\.venv\Scripts\Activate.ps1
```

Bash / WSL / macOS:
```bash
# create .venv, install requirements, run migrations
./scripts/init.sh
# activate the venv for interactive work
source .venv/bin/activate
```

If you prefer manual steps:
```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

### 3) Working with Git
- Create a feature branch for each change:
```bash
git checkout -b feature/short-description
```
- Commit small, focused changes with meaningful messages.
- Keep `main` clean and up-to-date: fetch and rebase/pull before pushing:
```bash
git fetch origin
git pull --rebase origin main
git push origin feature/short-description
```
- Open a pull request on GitHub to merge your feature into `main`.

### 4) Files that should not be committed
This repository includes a `.gitignore` that prevents local files from being accidentally committed (e.g. `db.sqlite3`, virtualenvs, editor files). Do not commit local databases, virtual environments, or editor-specific folders.

If you accidentally tracked a local file, stop tracking it with:
```bash
git rm --cached path/to/file
git commit -m "Stop tracking <file>"
git push
```

### 5) Tests and quality
- Add tests in the appropriate app `tests.py` or `tests/` folder when you add behavior.
- Run tests locally and keep commits small to simplify review.

### 6) Style and conventions
- Keep commit messages clear and imperative (e.g. "Add blog view").
- Prefer small PRs focused on one thing.

### 7) Help and troubleshooting
- If Source Control in VS Code doesn't show your repo, make sure you opened the repo root (the folder containing `.git`) and that the Git extension is enabled. Reload the window if needed.
- If you see push rejections, fetch & rebase the remote `main` before pushing, or create a PR from a feature branch.

Thanks again — contributions are welcome. If anything in this guide is unclear, open an issue or ask in the PR comments.