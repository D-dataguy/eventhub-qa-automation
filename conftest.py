from pathlib import Path

import pytest


PROJECT_ROOT = Path(__file__).resolve().parent
SCREENSHOT_DIR = PROJECT_ROOT / "screenshots"


@pytest.fixture(autouse=True)
def configure_page(page):
    page.set_default_timeout(10000)


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        page = item.funcargs.get("page")

        if page:
            SCREENSHOT_DIR.mkdir(parents=True, exist_ok=True)

            filename = f"{item.name.replace('[', '_').replace(']', '')}.png"
            screenshot_path = SCREENSHOT_DIR / filename

            page.screenshot(path=str(screenshot_path))

            print(f"\nFailure screenshot saved: {screenshot_path}")
