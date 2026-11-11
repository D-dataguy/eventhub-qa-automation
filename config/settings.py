import os
from pathlib import Path

from dotenv import load_dotenv


PROJECT_ROOT = Path(__file__).parent.parent

load_dotenv(PROJECT_ROOT / ".env")
EVENTHUB_EMAIL = os.getenv("EVENTHUB_EMAIL")
EVENTHUB_PASSWORD = os.getenv("EVENTHUB_PASSWORD")

BASE_URL = os.getenv("BASE_URL")

if not BASE_URL:
    raise ValueError("BASE_URL is missing from the .env file")

API_BASE_URL = os.getenv("API_BASE_URL")

if not API_BASE_URL:
    raise ValueError("API_BASE_URL is missing from the .env file")
