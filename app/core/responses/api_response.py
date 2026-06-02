from typing import Any, Optional

from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from pydantic import BaseModel


class Meta(BaseModel):
    limit: int
    page: int
    total: int
    totalPage: int


def send_response(
    *,
    status_code: int,
    success: bool,
    message: Optional[str] = None,
    data: Any = None,
    meta: Optional[Meta | dict] = None,
) -> JSONResponse:
    response = {
        "success": success,
        "message": message,
        "meta": meta,
        "data": data,
    }

    return JSONResponse(
        status_code=status_code,
        content=jsonable_encoder(response),
    )