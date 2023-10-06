from dotenv import load_dotenv
import os

load_dotenv()

DB_HOST = os.environ.get("DB_HOST")
DB_PORT = os.environ.get("DB_PORT")
DB_NAME = os.environ.get("DB_NAME")
DB_USER = os.environ.get("DB_USER")
DB_PASS = os.environ.get("DB_PASS")

# DB_HOST = 'localhost'
# DB_PORT = 5432
# DB_NAME = 'test'
# DB_USER = 'postgres'
# DB_PASS = '123456'

SECRET_AUTH = os.environ.get("SECRET_AUTH")
SMTP_PASSWORD = os.environ.get("SMTP_PASSWORD")
SMTP_USER = os.environ.get("SMTP_USER")

REDIS_HOST = os.environ.get("REDIS_HOST")
REDIS_PORT = os.environ.get("REDIS_PORT")

CELERY_CONFIG = {
    # 'broker_url': 'redis://redis:6379/0',
    'broker_url': 'amqp://rmuser:123456@rabbitmq:5672/edm_vhost',
    'result_backend': f'redis://redis:6379/0',
    'task_ignore_results': True,
    'broker_connection_retry_on_startup': True,

}