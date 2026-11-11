# EventHub QA Automation Framework

## Project Overview

EventHub QA Automation is a test automation framework built with Python, Pytest, and Playwright.

The project tests the EventHub practice application through UI and API automation. It covers authentication workflows, API response validation, and access control.

The framework follows maintainable automation practices, including Page Object Model, reusable fixtures, external test data, and environment-based configuration.

## Technology Stack

| Category | Technology |
|---|---|
| Programming Language | Python |
| Browser Automation | Playwright |
| Test Framework | Pytest |
| API Testing | Playwright APIRequestContext |
| Design Pattern | Page Object Model (POM) |
| Test Data | JSON |
| Configuration | Python-dotenv |
| Reporting | Pytest HTML |
| Logging | Python logging |
| Version Control | Git and GitHub |
| CI/CD | Jenkins (planned) |

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
│   ├── api/
│   │   ├── test_auth_api.py
│   │   ├── test_config_api.py
│   │   ├── test_successful_login_api.py
│   │   ├── test_authenticated_events_api.py
│   │   └── test_events_authentication.py
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

### UI Testing

| Test Scenario | Description |
|---|---|
| Login form visibility | Verifies that email, password, and sign-in elements are visible. |
| Invalid login | Verifies that the application rejects unregistered credentials. |
| Incorrect password | Verifies that the application rejects an incorrect password. |

### API Testing

| Test Scenario | Description |
|---|---|
| Configuration endpoint | Validates the configuration endpoint response and data types. |
| Invalid login API | Verifies that invalid credentials return HTTP 400 and the expected error response. |
| Successful login API | Validates successful authentication, token generation, and user information. |
| Authenticated events request | Verifies that a valid authentication token grants access to the events endpoint. |
| Missing authentication token | Verifies that requests without an authentication token return HTTP 401. |
| Invalid authentication token | Verifies that requests with an invalid token return HTTP 401. |

## Framework Features

- Page Object Model for separating page interactions from test logic.
- Data-driven testing using external JSON files.
- Parameterized test execution with Pytest.
- Reusable browser and API fixtures.
- Environment-based application configuration.
- Configurable Playwright timeouts.
- Automatic failure screenshots.
- Execution logging.
- Standalone HTML test reports.
- API authentication and response validation.

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/D-dataguy/eventhub-qa-automation.git
cd eventhub-qa-automation
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

### 3. Activate the virtual environment

Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Install Playwright Chromium

```bash
python -m playwright install chromium
```

### 6. Configure environment variables

Create a `.env` file in the project root.

```env
BASE_URL=https://eventhub.rahulshettyacademy.com
API_BASE_URL=https://api.eventhub.rahulshettyacademy.com
EVENTHUB_EMAIL=your_registered_email
EVENTHUB_PASSWORD=your_registered_password
```

Replace the placeholders with your own EventHub credentials.

**Security:** Never commit your `.env` file or expose authentication tokens. The `.env` file should be listed in `.gitignore`.

## Running Tests

### Run the complete test suite

```bash
python -m pytest -v
```

### Run UI tests

```bash
python -m pytest tests/ -v
```

### Run API tests

```bash
python -m pytest tests/api/ -v
```

### Run a specific test file

```bash
python -m pytest tests/api/test_auth_api.py -v
```

### Generate an HTML report

```bash
python -m pytest -v --html=reports/report.html --self-contained-html
```

## Test Evidence and Reporting

The framework generates:

- HTML test reports in `reports/`.
- Execution logs in `logs/`.
- Failure screenshots in `screenshots/`.

These outputs support test analysis, debugging, and defect investigation.

## Current Test Results

**Latest full test suite execution:**

- 11 tests passed.
- 0 tests failed.
- Execution time: 35.47 seconds.

Test results reflect the latest recorded local execution and may change as the framework evolves.

## CI/CD

Jenkins integration is planned.

The intended pipeline will install dependencies, execute automated tests, and publish test reports.

## Project Goals

This project demonstrates practical skills in:

- Python test automation.
- Browser automation with Playwright.
- API testing and authentication.
- Pytest test organisation and fixtures.
- Data-driven testing.
- Page Object Model.
- Test reporting and debugging.
- Git and GitHub version control.

## Author

**Destiny Erhunmwunse**

GitHub: https://github.com/D-dataguy

Repository: https://github.com/D-dataguy/eventhub-qa-automation
