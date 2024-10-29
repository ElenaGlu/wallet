import json
from django.http import HttpRequest, HttpResponse, JsonResponse

from app.app_services import WalletHandler


def update_wallet(request: HttpRequest, uuid: str) -> HttpResponse:
    """
    Update the wallet balance.
    :param uuid: example, 'a8098c1a-f86e-11da-bd1a-00112444be1e'
    :param request: JSON object containing keys - 'operationType', 'amount'
    :return: "created" (201) response code
    """
    if request.method == "POST":
        WalletHandler(uuid, json.loads(request.body))
        return HttpResponse(status=201)


def get_wallet(request: HttpRequest, uuid: str) -> JsonResponse:
    """
    Get the wallet balance.
    :param uuid: example, 'a8098c1a-f86e-11da-bd1a-00112444be1e'
    :return: "OK" (200) response code
    """
    if request.method == "GET":
        data_wallet = WalletHandler(uuid, json.loads(request.body))
        return JsonResponse(data_wallet, status=200, safe=False)

