import smtplib
from email.message import EmailMessage

from celery import Celery

from src.config import SMTP_PASSWORD, SMTP_USER

CELERY_CONFIG = {
    # 'broker_url': 'redis://redis:6379/0',
    'broker_url': 'amqp://rmuser:123456@rabbitmq:5672/edm_vhost',
    'result_backend': f'redis://redis:6379/0',
    'task_ignore_results': True,
    'broker_connection_retry_on_startup': True,

}

SMTP_HOST = "smtp.gmail.com"
SMTP_PORT = 465

celery = Celery('tasks')
celery.conf.update(CELERY_CONFIG)

def get_email_template_dashboard(username: str):
    email = EmailMessage()
    email['Subject'] = 'Натрейдил Отчет Дашборд'
    email['From'] = SMTP_USER
    email['To'] = SMTP_USER

    email.set_content(
        '<div>'
        f'<h1 style="color: red;">Здравствуйте, {username}, а вот и ваш отчет. Зацените 😊</h1>'
        '<img src="https://static.vecteezy.com/system/resources/previews/008/295/031/original/custom-relationship'
        '-management-dashboard-ui-design-template-suitable-designing-application-for-android-and-ios-clean-style-app'
        '-mobile-free-vector.jpg" width="600">'
        '</div>',
        subtype='html'
    )
    return email


@celery.task
def send_email_report_dashboard(username: str):
    email = get_email_template_dashboard(username)
    with smtplib.SMTP_SSL(SMTP_HOST, SMTP_PORT) as server:
        server.login(SMTP_USER, SMTP_PASSWORD)
        server.send_message(email)