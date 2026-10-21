import logging
import re
from pathlib import Path
from typing import Optional, Dict

LOG_DIR = Path("logs")
LOG_DIR.mkdir(exist_ok=True)
LOG_FILE = LOG_DIR / "app.log"

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler(LOG_FILE, encoding="utf-8"),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

EMAIL_REGEX = re.compile(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$")

def is_valid_email(email: str) -> bool:
    if not email or not isinstance(email, str):
        return False
    return bool(EMAIL_REGEX.match(email.strip()))

def clean_and_split_email(email: str) -> Dict[str, str]:
    cleaned = email.strip().lower()
    if "@" not in cleaned:
        raise ValueError("Email must contain '@'")
    username, domain = cleaned.split("@", 1)
    return {"username": username, "domain": domain, "cleaned_email": cleaned}

def orchestrate_email_processing(raw_email: str) -> Optional[Dict[str, str]]:
    logger.info(f"Received email for processing: {raw_email}")
    if not is_valid_email(raw_email):
        logger.warning(f"Invalid email format rejected: {raw_email}")
        return None
    try:
        result = clean_and_split_email(raw_email)
        logger.info(f"Successfully processed Email: {result}")
        return result
    except Exception as e:
        logger.error(f"Failed to process email '{raw_email}': {e}", exc_info=True)
        return None

def main():
    logger.info("App Started")
    print("--- Email Processor ---", flush=True)
    try:
        while True:
            print("Please enter your email (or 'q' to quit): ", end="", flush=True)
            email = input().strip()
            if email.lower() == 'q':
                print("Bye!", flush=True)
                break
            processed = orchestrate_email_processing(email)
            if processed:
                print(f"\n✅ Valid! -> {processed}\n", flush=True)
                break
            else:
                print("\n❌ Invalid email. Try again.\n", flush=True)
    finally:
        logger.info("App Stopped")

if __name__ == "__main__":
    main()
