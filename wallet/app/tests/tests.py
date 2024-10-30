import json

import pytest
from django.urls import reverse

from app.models import Wallet
from loguru import logger


@pytest.mark.django_db
def test_deposit(client, add_transaction):
    url = reverse('update_wallet', kwargs={'wallet_id': 'f50ec0b7-f960-400d-91f0-c42a6d44e3d0'})
    operation = json.dumps(
        {
            'operationType': 'deposit',
            'amount': 100,
        }
    )

    response = client.post(url, operation, content_type='application/json')
    logger.info(Wallet.objects.all().values())
    assert response.status_code == 201


@pytest.mark.django_db
def test_withdraw(client, add_transaction):
    url = reverse('update_wallet', kwargs={'wallet_id': 'f50ec0b7-f960-400d-91f0-c42a6d44e3d0'})
    operation = json.dumps(
        {
            'operationType': 'withdraw',
            'amount': 200,
        }
    )
    response = client.post(url, operation, content_type='application/json')
    assert response.status_code == 201


@pytest.mark.django_db
def test_json_negative(client, add_transaction):
    url = reverse('update_wallet', kwargs={'wallet_id': 'f50ec0b7-f960-400d-91f0-c42a6d44e3d0'})
    operation = json.dumps(
        {
            'operationType': 'test',
            'amount': '200',
        }
    )
    response = client.post(url, operation, content_type='application/json')
    logger.info(response.status_code)
    assert response.status_code == 400


@pytest.mark.django_db
def test_current_balance(client, add_transaction):
    url = reverse('get_wallet', kwargs={'wallet_id': 'f50ec0b7-f960-400d-91f0-c42a6d44e3d0'})
    response = client.get(url)
    resp_json = response.json()

    assert response.status_code == 200
    assert resp_json == [
        {
            'account_balance': '800.00'
        }
    ]
