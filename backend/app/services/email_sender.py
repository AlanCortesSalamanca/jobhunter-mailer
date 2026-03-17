import smtplib
from email.message import EmailMessage
import ssl
import time


def send_emails(
    sender_email,
    sender_password,
    recipients,
    subject,
    body,
    cv_path=None,
    delay=5
):

    context = ssl.create_default_context()

    sent = []
    failed = []

    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:

        server.login(sender_email, sender_password)

        for email in recipients:

            try:

                msg = EmailMessage()

                msg["From"] = sender_email
                msg["To"] = email
                msg["Subject"] = subject

                msg.set_content(body)

                # Adjuntar CV
                if cv_path:

                    with open(cv_path, "rb") as f:

                        file_data = f.read()
                        file_name = cv_path.split("/")[-1]

                    msg.add_attachment(
                        file_data,
                        maintype="application",
                        subtype="pdf",
                        filename=file_name
                    )

                server.send_message(msg)

                sent.append(email)

                time.sleep(delay)

            except Exception:

                failed.append(email)

    return {
        "sent": sent,
        "failed": failed
    }