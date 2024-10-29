class AppExceptions(Exception):
    pass


class AppError(AppExceptions):
    pass


class ErrorType:
    UUID_ERROR = {
        'status_code': 404,
        'summary': 'Not Found',
    }

    AMOUNT_ERROR = {
        'status_code': 400,
        'summary': 'Bad Request',
    }