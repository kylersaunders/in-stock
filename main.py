import os
from dotenv import load_dotenv
from email_service.gmail import send_email
from in_stock_service.in_stock import check_stock

# Load environment variables from .env file
load_dotenv()

url = os.getenv("TARGET_SITE")
from_email = os.getenv("FROM_EMAIL")
to_email = os.getenv("TO_EMAIL")
app_password = os.getenv("GMAIL_APP_PASSWORD")


def main():
    subject = "Daily In-stock Summary"
    body = check_stock(url)
    send_email(to_email, from_email, subject, body, app_password)


if __name__ == "__main__":
    main()
