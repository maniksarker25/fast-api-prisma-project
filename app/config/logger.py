import logging
import sys


def get_logger(name: str) -> logging.Logger:
    logger = logging.getLogger(name)

    if logger.handlers:
        return logger

    handler = logging.StreamHandler(sys.stdout)

    # Lazy import to avoid circular deps at module load time
    from app.config.settings import settings

    if settings.APP_ENV == "production":
        fmt = '{"time":"%(asctime)s","level":"%(levelname)s","name":"%(name)s","message":"%(message)s"}'
    else:
        fmt = "%(asctime)s | %(levelname)-8s | %(name)s - %(message)s"

    handler.setFormatter(logging.Formatter(fmt, datefmt="%Y-%m-%d %H:%M:%S"))
    logger.addHandler(handler)
    logger.setLevel(logging.DEBUG if settings.APP_ENV != "production" else logging.INFO)
    logger.propagate = False

    return logger
