import smtplib, ssl
from web.views import my_info

def send_failure_message(task_name, task_step, failure):
    """"""
    port = 465  # For SSL
    smtp_server = "smtp.gmail.com"
    sender_email = my_info.sender_email()
    receiver_email = my_info.receiver_email()
    password = my_info.sender_email_password()

    message = f"""\
Subject: Failure during {task_name}

Failure during {task_name} step: {task_step}

Failure message: {failure}"""

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)