from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.config.prisma import db


@asynccontextmanager
async def lifespan(app: FastAPI):

    # STARTUP ----------------

    try:

        print("Connecting database...")

        await db.connect()

        print("Database connected")

    except Exception as error:

        print("Database connection failed")

        raise error

    yield

    # SHUTDOWN ----------------

    try:

        print("Disconnecting database...")

        await db.disconnect()

        print("Database disconnected")

    except Exception as error:

        print("Database disconnect failed")

        raise error