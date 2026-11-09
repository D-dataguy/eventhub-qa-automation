# EventHub QA Automation Framework

## Project Overview

EventHub QA Automation is a UI test automation project built with Python, Pytest, and Playwright.

The project focuses on testing authentication workflows and demonstrating maintainable automation framework practices.

## Technology Stack

- **Language:** Python
- **Automation:** Playwright
- **Test Framework:** Pytest
- **Design Pattern:** Page Object Model (POM)
- **Test Data:** JSON
- **Configuration:** Python-dotenv
- **Reporting:** Pytest HTML
- **Version Control:** Git and GitHub
- **CI/CD:** Jenkins (planned)

## Project Structure

```text
eventhub-qa/
├── config/
│   └── settings.py
├── logs/
├── pages/
│   └── login_page.py
├── reports/
├── screenshots/
├── test_data/
│   └── login_data.json
├── tests/
│   ├── test_invalid_login.py
│   ├── test_login_inspection.py
│   └── test_login_page.py
├── utilities/
├── conftest.py
├── pytest.ini
├── requirements.txt
├── .env
├── .gitignore
└── README.md
```

## Implemented Test Scenarios

| Test | Description |
|---|---|
| Login form visibility | Verifies email, password and sign-in elements |
| Invalid login | Verifies rejection of unregistered credentials |
| Incorrect password | Verifies rejection of an incorrect password |

## Framework Features

- Page Object Model for separating page interactions from test logic.
- External JSON files for test data.
- Parameterised tests using Pytest.
- Environment-based application configuration.
- Reusable browser fixtures.
- Configurable Playwright timeout.
- Automatic screenshots on test failures.
- Execution logs.
- Standalone HTML test reports.

## Installation

Clone the repository:

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd eventhub-qa
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it on Windows:

```powershell
.venv\Scripts\Activate.ps1
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Install the Chromium browser:

```bash
python -m playwright install chromium
```

Create a `.env` file in the project root:

```env
BASE_URL=https://eventhub.rahulshettyacademy.com
```

## Running Tests

Run the complete test suite:

```bash
python -m pytest
```

Generate an HTML report:

```bash
python -m pytest --html=reports/report.html --self-contained-html
```

## Test Evidence

The framework generates:

- HTML test reports in `reports/`.
- Execution logs in `logs/`.
- Failure screenshots in `screenshots/`.

## CI/CD

Jenkins integration is planned to automate test execution following repository updates. The pipeline will install dependencies, execute tests, and publish test reports.

## Project Goals

This project demonstrates practical skills in:

- Python test automation.
- Browser automation with Playwright.
- Pytest test organisation and fixtures.
- Data-driven testing.
- Test reporting and debugging.
- Version control and CI/CD.

## Author

Destiny Erhunmwunse

**GitHub:** https://github.com/D-dataguy
