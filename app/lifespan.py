from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.config.logger import get_logger
from app.config.prisma import db

logger = get_logger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI):

    # STARTUP ----------------

    try:
        logger.info("Connecting to database...")
        await db.connect()
        logger.info("Database connected successfully")

    except Exception as error:
        logger.error(f"Database connection failed: {error}")
        raise error

    yield

    # SHUTDOWN ----------------

    try:
        logger.info("Disconnecting from database...")
        await db.disconnect()
        logger.info("Database disconnected")

    except Exception as error:
        logger.error(f"Database disconnect failed: {error}")
        raise error