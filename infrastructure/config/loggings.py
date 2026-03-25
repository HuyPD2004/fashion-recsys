import logging
import os
from logging.handlers import RotatingFileHandler

from infrastructure.config.settings import settings


def setup_logger(name: str = "recsys") -> logging.Logger:
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    if logger.hasHandlers():
        return logger

    os.makedirs(settings.LOG_DIR, exist_ok=True)

    log_file = os.path.join(settings.LOG_DIR, "app.log")

    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(name)s | %(message)s"
    )

    file_handler = RotatingFileHandler(
        log_file,
        maxBytes=10_000_000,  
        backupCount=5
    )
    file_handler.setFormatter(formatter)

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger