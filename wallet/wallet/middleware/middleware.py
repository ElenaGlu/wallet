from django.http import JsonResponse

from exceptions import AppError


class CustomErrorMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response

    @staticmethod
    def process_exception(request, exception):
        error_data = exception.args[0]
        if isinstance(exception, AppError):
            return JsonResponse(
                status=error_data['error_type']['status_code'],
                data={
                    'description': error_data['description'],
                }
            )