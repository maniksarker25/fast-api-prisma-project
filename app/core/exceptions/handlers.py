from fastapi import Request
from fastapi.responses import JSONResponse

from fastapi.exceptions import RequestValidationError

from starlette.exceptions import HTTPException

from prisma.errors import (
    PrismaError,
    UniqueViolationError
)

from app.core.exceptions.base import AppException


async def global_exception_handler(
    request: Request,
    exc: Exception
):

    status_code = 500

    message = "Something went wrong"

    error_type = "Internal Server Error"

    error_details = []

    # APP EXCEPTION ----------------

    if isinstance(exc, AppException):

        status_code = exc.status_code

        message = exc.message

        error_type = exc.error_type

        error_details = exc.error_details

    #  VALIDATION ERROR ----------------

    elif isinstance(exc, RequestValidationError):

        status_code = 422

        message = "Validation Error"

        error_type = "Validation Error"

        error_details = [
            {
                "field": ".".join(
                    map(str, error["loc"])
                ),
                "message": error["msg"]
            }
            for error in exc.errors()
        ]

    #  HTTP EXCEPTION ----------------

    elif isinstance(exc, HTTPException):

        status_code = exc.status_code

        message = exc.detail

        error_type = "HTTP Error"

    # PRISMA UNIQUE ERROR ----------------

    elif isinstance(exc, UniqueViolationError):

        status_code = 409

        message = "Duplicate value already exists"

        error_type = "Database Error"

    # PRISMA ERROR ----------------

    elif isinstance(exc, PrismaError):

        status_code = 400

        message = "Database operation failed"

        error_type = "Database Error"

    # UNKNOWN ERROR ----------------

    return JSONResponse(
        status_code=status_code,
        content={
            "success": False,
            "message": message,
            "errorType": error_type,
            "errorDetails": error_details,
            "path": request.url.path,
            "timestamp": str(request.state.timestamp)
            if hasattr(request.state, "timestamp")
            else None,
            "stack": str(exc)
            if True
            else None
        }
    )