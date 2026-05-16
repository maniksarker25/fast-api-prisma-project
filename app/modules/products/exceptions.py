from app.core.exceptions.base import AppException


class ProductNotFoundException(AppException):

    def __init__(self):

        super().__init__(
            message="Product not found",
            status_code=404,
            error_type="Product Error"
        )


class ProductAlreadyExistsException(AppException):

    def __init__(self):

        super().__init__(
            message="Product already exists",
            status_code=409,
            error_type="Product Error"
        )