# Email Automation Tool

**Assignment (Capstone Option 3 / Mini Project Task 3):** Read a CSV
of names & emails, auto-send personalized emails using `smtplib`,
add subject & message dynamically.

**Skill Gain:** Python automation, real-world scripting.

Reads recipient names and emails from a CSV file, then sends each
person a personalized email using their name in the message body.

## Safety First — Read Before Running
This script sends **real emails** once configured, so it starts in
**DRY-RUN mode** (`DRY_RUN = True`) — it only prints what it *would*
send, without actually sending anything. This lets you test the
logic safely first.

## Setup (only needed once you want to actually send emails)
1. Open `email_automation.py` and set `SENDER_EMAIL` to your address.
2. **Never hardcode your password in the script.** Set it as an
   environment variable instead:
   ```bash
   # macOS/Linux
   export EMAIL_PASSWORD="your_app_password"

   # Windows (PowerShell)
   $env:EMAIL_PASSWORD="your_app_password"
   ```
3. If using Gmail, generate an **App Password** at
   Google Account → Security → App Passwords (your normal password
   won't work — Gmail blocks direct SMTP logins otherwise).
4. Set `DRY_RUN = False` in the script once you're ready.
5. Only send to people who have agreed to receive these emails.

## Concepts Used
- File I/O with the `csv` module
- The `smtplib` and `email` modules
- Environment variables for secure credential handling
- String templating for personalization

## How to Run
```bash
python email_automation.py
```
When prompted, enter `recipients.csv` (sample file included) to test.

## Example (Dry Run)
```
=== Email Automation Tool ===
(Running in DRY-RUN mode — no real emails will be sent)

Enter path to recipients CSV (e.g. recipients.csv): recipients.csv
Enter the email subject: Internship Update
Enter the message body. Use {name} where you want the recipient's name inserted.
Message: Hi {name}, your Week 4 submission has been received!

[DRY RUN] Would send to: aarav.sharma@example.com
Subject: Internship Update
Body:
Hi Aarav Sharma, your Week 4 submission has been received!
----------------------------------------
```
