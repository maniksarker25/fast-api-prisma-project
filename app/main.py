from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.lifespan import lifespan

# ---------------- EXCEPTION HANDLERS ----------------

from app.core.exceptions.handlers import (
    global_exception_handler
)

# ---------------- BASE EXCEPTION ----------------

from app.core.exceptions.base import (
    AppException
)

# ---------------- ROUTES ----------------

from app.api.router import api_router
# ---------------- APP ----------------

app = FastAPI(
    title="Enterprise FastAPI Backend",
    description="Production Grade FastAPI Architecture",
    version="1.0.0",
    lifespan=lifespan,
    docs_url="/docs",
    redoc_url="/redoc"
)

# CORS ----------------

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "*"
    ],

    allow_credentials=True,

    allow_methods=[
        "*"
    ],

    allow_headers=[
        "*"
    ]
)

# GLOBAL EXCEPTION HANDLER ----------------

app.add_exception_handler(
    Exception,
    global_exception_handler
)

app.add_exception_handler(
    AppException,
    global_exception_handler
)

# ROOT ROUTE ----------------

@app.get("/")
async def root():

    return {
        "success": True,
        "message": "Server is running"
    }

# API ROUTES ----------------
app.include_router(
    api_router,
    prefix="/api"
)