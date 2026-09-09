"""
Email Automation Tool
--------------------------
Covers:
- Capstone Option 3: Email Automation Tool (read CSV of names & emails,
  auto-send personalized emails using smtplib, add subject & message dynamically)
- Mini Project Task: Automate email sending with smtplib.

Skill Gain: Python automation, real-world scripting.

IMPORTANT — SETUP BEFORE USE:
This script sends REAL emails once configured. To use it safely:
1. Never hardcode your email password directly in the script.
   Instead, set it as an environment variable before running:
     Windows (PowerShell):  $env:EMAIL_PASSWORD="your_app_password"
     macOS/Linux:            export EMAIL_PASSWORD="your_app_password"
2. If using Gmail, you must create an "App Password" (Google Account ->
   Security -> App Passwords) — your normal Gmail password will NOT work
   because Google blocks direct SMTP logins for security.
3. By default this script runs in DRY-RUN mode (it prints what would be
   sent instead of actually sending). Set DRY_RUN = False only once you
   have configured your SMTP details correctly, and only send to
   recipients who have agreed to receive these emails.
"""

import csv
import smtplib
import os
from email.mime.text import MIMEText

# ---------------- Configuration ----------------
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
SENDER_EMAIL = "your_email@gmail.com"          # <-- change this
SENDER_PASSWORD = os.environ.get("EMAIL_PASSWORD", "")  # read from environment variable

DRY_RUN = True  # Set to False only after configuring the details above
# -------------------------------------------------


def read_recipients(filename):
    """Read a CSV file with 'name' and 'email' columns."""
    with open(filename, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        return list(reader)


def build_message(name, subject, message_template):
    """Personalize the message template with the recipient's name."""
    return message_template.replace("{name}", name)


def send_email(recipient_email, subject, body):
    """Send a single email via SMTP, or print it if DRY_RUN is True."""
    if DRY_RUN:
        print(f"[DRY RUN] Would send to: {recipient_email}")
        print(f"Subject: {subject}")
        print(f"Body:\n{body}\n{'-' * 40}")
        return

    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = SENDER_EMAIL
    msg["To"] = recipient_email

    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
        server.starttls()
        server.login(SENDER_EMAIL, SENDER_PASSWORD)
        server.sendmail(SENDER_EMAIL, recipient_email, msg.as_string())

    print(f"Email sent to {recipient_email}")


def main():
    print("=== Email Automation Tool ===")
    if DRY_RUN:
        print("(Running in DRY-RUN mode — no real emails will be sent)\n")

    filename = input("Enter path to recipients CSV (e.g. recipients.csv): ").strip()

    try:
        recipients = read_recipients(filename)
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return

    subject = input("Enter the email subject: ").strip()
    print("Enter the message body. Use {name} where you want the recipient's name inserted.")
    message_template = input("Message: ").strip()

    for person in recipients:
        name = person.get("name", "")
        email = person.get("email", "")
        if not email:
            continue
        body = build_message(name, subject, message_template)
        try:
            send_email(email, subject, body)
        except Exception as e:
            print(f"Failed to send to {email}: {e}")


if __name__ == "__main__":
    main()
