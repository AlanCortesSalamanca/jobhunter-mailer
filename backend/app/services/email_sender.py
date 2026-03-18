import smtplib
from app.services.logger import log_queue
from email.message import EmailMessage
import ssl
import time
import random


def send_emails(
    sender_email,
    sender_password,
    recipients,
    subject,
    body_template,
    cv_path=None,
    delay=5
):

    context = ssl.create_default_context()

    sent = []
    failed = []

    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:

        server.login(sender_email, sender_password)

        for i, item in enumerate(recipients):

            if i % 20 == 0 and i != 0:
                time.sleep(random.randint(60, 120))

            try:
                empresa = item["empresa"]
                email = item["correo"]

                body = body_template.replace("{empresa}", empresa)

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

                # 🔥 LOG ANTES
                log_queue.append(f"📨 Enviando a {empresa} ({email})")

                server.send_message(msg)

                # 🔥 LOG DESPUÉS
                log_queue.append(f"✅ Enviado a {empresa}")

                sent.append(email)

                sleep_time = random.randint(5, 15)
                time.sleep(sleep_time)

            except Exception as e:
                log_queue.append(f"❌ Error con {email}: {e}")
                failed.append(email)

                

    return {
        "sent": sent,
        "failed": failed
    }