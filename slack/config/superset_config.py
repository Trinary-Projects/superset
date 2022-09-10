from celery.schedules import crontab

FEATURE_FLAGS = {
    "ALERT_REPORTS": True
}

REDIS_HOST = "redis-superset"
REDIS_PORT = "6379"

class CeleryConfig:
    broker_url = 'redis://%s:%s/0' % (REDIS_HOST, REDIS_PORT)
    imports = ('superset.sql_lab', "superset.tasks", "superset.tasks.thumbnails", )
    result_backend = 'redis://%s:%s/0' % (REDIS_HOST, REDIS_PORT)
    worker_prefetch_multiplier = 10
    task_acks_late = True
    task_annotations = {
        'sql_lab.get_sql_results': {
            'rate_limit': '100/s',
        },
        'email_reports.send': {
            'rate_limit': '1/s',
            'time_limit': 600,
            'soft_time_limit': 600,
            'ignore_result': True,
        },
    }
    beat_schedule = {
        'reports.scheduler': {
            'task': 'reports.scheduler',
            'schedule': crontab(minute='*', hour='*'),
        },
        'reports.prune_log': {
            'task': 'reports.prune_log',
            'schedule': crontab(minute=0, hour=0),
        },
    }
CELERY_CONFIG = CeleryConfig

SCREENSHOT_LOCATE_WAIT = 100
SCREENSHOT_LOAD_WAIT = 600

# Slack configuration
SLACK_API_TOKEN = "xoxb-2397059419024-3311832884097-xPb0Q7eoU0S8rt5KmZgENLUS"

# # Email configuration
# SMTP_HOST = "smtp.sendgrid.net" #change to your host
# SMTP_STARTTLS = True
# SMTP_SSL_SERVER_AUTH = True # If your using an SMTP server with a valid certificate
# SMTP_SSL = False
# SMTP_USER = "your_user"
# SMTP_PORT = 2525 # your port eg. 587
# SMTP_PASSWORD = "your_password"
# SMTP_MAIL_FROM = "noreply@youremail.com"

# WebDriver configuration
# If you use Firefox, you can stick with default values
# If you use Chrome, then add the following WEBDRIVER_TYPE and WEBDRIVER_OPTION_ARGS
WEBDRIVER_TYPE = "chrome"
WEBDRIVER_OPTION_ARGS = [
    "--force-device-scale-factor=2.0",
    "--high-dpi-support=2.0",
    "--headless",
    "--disable-gpu",
    "--disable-dev-shm-usage",
    "--no-sandbox",
    "--disable-setuid-sandbox",
    "--disable-extensions",
]

# This is for internal use, you can keep http
WEBDRIVER_BASEURL="http://superset:8088"
# This is the link sent to the recipient, change to your domain eg. https://superset.mydomain.com
WEBDRIVER_BASEURL_USER_FRIENDLY="http://localhost:8088"
