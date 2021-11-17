from . import env
import logging
from logging.handlers import RotatingFileHandler

log_file = env.get_app_root_path('logs', 'pillbox.log')

logger = logging.getLogger('pillbox_default')
logger.setLevel(logging.INFO)
handler = RotatingFileHandler(filename=log_file, maxBytes=50 * 1024 * 1024, backupCount=3, encoding='utf-8')
handler.setFormatter('{asctime} {levelname} {threadName} {name} {message}')
logger.addHandler(handler)
