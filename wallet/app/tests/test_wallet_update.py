import json

import pytest
from django.urls import reverse

from app.models import Wallet
from loguru import logger


@pytest.mark.django_db
def test_update_wallet_success_deposit(client, add_transaction):
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
def test_update_wallet_success_withdraw(client, add_transaction):
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
def test_update_wallet_invalid_schema(client, add_transaction):
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
def test_update_wallet_invalid_json(client, add_transaction):
    url = reverse('update_wallet', kwargs={'wallet_id': 'f50ec0b7-f960-400d-91f0-c42a6d44e3d0'})
    operation = json.dumps(
        {
            "invalid_json": ''
        }
    )
    response = client.post(url, operation, content_type='application/json')
    logger.info(response.status_code)
    assert response.status_code == 400
