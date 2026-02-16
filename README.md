# SQA Project: Automated Testing and Continuous Integration (CI)

This project demonstrates how to improve software quality using automated testing and continuous integration.

## Technologies Used

- **PyTest** – Unit Testing Framework
- **Coverage** – Code Coverage Measurement
- **Flake8** – Static Code Analysis (Linting)
- **Black** – Code Formatting Validation
- **GitHub Actions** – Continuous Integration (CI)

The objective is to automate quality checks and detect defects early in the development process.

---

# 1) Project Structure


sqa_ci_project/
│
├── src/
│ ├── init.py
│ └── task_service.py
│
├── tests/
│ └── test_task_service.py
│
├── .github/
│ └── workflows/
│ └── ci.yml
│
├── requirements.txt
├── pyproject.toml
├── .flake8
└── README.md


⚠ Important:  
Make sure the file `src/__init__.py` exists to allow Python to import the module correctly during testing.

---

# 2) Run the Project Locally (Step-by-Step)

## Step A — Create a Virtual Environment

### Windows (PowerShell)

```powershell
python -m venv .venv
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\.venv\Scripts\Activate.ps1
Windows (Command Prompt)
python -m venv .venv
.venv\Scripts\activate.bat
Linux / macOS
python -m venv .venv
source .venv/bin/activate

After activation, you should see:

(.venv)
Step B — Install Dependencies
pip install -r requirements.txt
Step C — Run Code Quality Checks
Run Linting
flake8
Check Code Formatting
black --check .
Step D — Run Unit Tests with Coverage
pytest --cov=src --cov-report=term-missing

Expected output:

8 passed

Coverage percentage will also be displayed.

3) Enable Continuous Integration (CI) on GitHub
Step 1 — Create a Repository

Go to GitHub

Click New Repository

Name it: sqa-ci-project

Do NOT initialize with README if pushing from local

Step 2 — Push the Project to GitHub

From inside the project folder:

git init
git add .
git commit -m "Initial SQA CI project"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/sqa-ci-project.git
git push -u origin main
Step 3 — Verify CI Execution

Open your repository on GitHub

Go to the Actions tab

You will see the workflow named CI

It runs automatically on:

Every push

Every pull request

If successful, you will see a green check mark ✅.

4) CI Pipeline Process

The CI workflow automatically:

Installs Python

Installs project dependencies

Runs Flake8 (linting)

Runs Black format check

Executes PyTest

Generates coverage report

This ensures that code quality is validated before integration.

5) What to Present in Your Demonstration

You can show:

All test cases passing (8 passed)

Code coverage percentage

GitHub Actions logs

Screenshot of successful CI run

Explanation of automated vs manual testing

Benefits of continuous integration

6) Quality Benefits

Using Automated Testing and CI provides:

Early defect detection

Faster feedback cycle

Reduced integration errors

Consistent quality enforcement

Improved maintainability

Better collaboration

7) Conclusion

This project demonstrates how Software Quality Assurance can be enhanced through:

Automated Unit Testing

Static Code Analysis

Continuous Integration

The CI pipeline acts as a quality gate that prevents defective code from being merged into the main branch.


---

After pasting it:

```bash
git add README.md
git commit -m "Final README version"
git push
