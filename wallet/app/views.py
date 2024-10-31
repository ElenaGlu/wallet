import json
from django.http import HttpRequest, HttpResponse, JsonResponse
from jsonschema import validate, exceptions
from app.app_services import WalletHandler, schemas
from exceptions import ErrorType, AppError


def update_wallet(request: HttpRequest, wallet_id: str) -> HttpResponse:
    """
    Update the wallet balance.
    :param request: JSON object containing keys - 'operationType', 'amount'
    :param wallet_id: example, 'a8098c1a-f86e-11da-bd1a-00112444be1e'
    :return: "created" (201) response code
    :raises AppError: if json invalid
    """
    if request.method == "POST":
        schema = schemas['update_wallet']
        try:
            validate(json.loads(request.body), schema)
        except exceptions.ValidationError:
            raise AppError(
                {
                    'error_type': ErrorType.SCHEMA_ERROR,
                    'description': 'Invalid JSON',
                }
            )
        obj = WalletHandler(wallet_id, json.loads(request.body))
        obj.check_wallet()
        return HttpResponse(status=201)


def get_wallet(request: HttpRequest, wallet_id: str) -> JsonResponse:
    """
    Get the wallet balance.
    :param wallet_id: example, 'a8098c1a-f86e-11da-bd1a-00112444be1e'
    :return: "OK" (200) response code
    :raises AppError: if UUID invalid
    """
    if request.method == "GET":
        obj = WalletHandler(wallet_id)
        balance = obj.get_current_balance()
        return JsonResponse(balance, status=200, safe=False)

