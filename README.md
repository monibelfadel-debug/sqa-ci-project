# SQA Project: Automated Testing + Continuous Integration (CI)

This is a complete, **ready-to-run** sample SQA project using:
- **PyTest** (unit testing)
- **Coverage** (test coverage)
- **Flake8** (linting)
- **Black** (format check)
- **GitHub Actions** (CI pipeline)

## 1) Project Structure
```
sqa_ci_project/
  src/
    task_service.py
  tests/
    test_task_service.py
  .github/workflows/
    ci.yml
  requirements.txt
  pyproject.toml
  .flake8
```

## 2) Run Locally (Step-by-step)

### A) Create a virtual environment
**Windows (PowerShell)**
```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

**Linux / macOS**
```bash
python -m venv .venv
source .venv/bin/activate
```

### B) Install dependencies
```bash
pip install -r requirements.txt
```

### C) Run lint + format check
```bash
flake8
black --check .
```

### D) Run tests + coverage
```bash
pytest --cov=src --cov-report=term-missing
```

## 3) Enable CI on GitHub (Step-by-step)

1. Create a new repository on GitHub (example: `sqa-ci-project`).
2. Upload the project files (or push using git):
   ```bash
   git init
   git add .
   git commit -m "Initial SQA CI project"
   git branch -M main
   git remote add origin <YOUR_REPO_URL>
   git push -u origin main
   ```
3. Go to **GitHub → Actions** tab.
4. You will see workflow **CI** running automatically on every push / pull request.

## 4) What to show in your report / presentation
- Test cases + results (pass/fail)
- Coverage percentage
- CI logs screenshots from GitHub Actions
- How automation reduces late defect detection
