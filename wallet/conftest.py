import pytest

from app import models


@pytest.fixture
def add_wallet():
    wallet = [
        {
            "id": "f50ec0b7-f960-400d-91f0-c42a6d44e3d0",
            "account_balance": 800,
        },
        {
            "id": "3ad5bef0-1531-4e67-b0ea-e2714bf116b7",
            "account_balance": 500,
        }
    ]
    temp = [models.Wallet(**obj) for obj in wallet]
    return models.Wallet.objects.bulk_create(temp)


@pytest.fixture
def add_transaction(add_wallet):
    transaction = [
        {
            "id": "5ca2f769-cd33-42d6-baa6-eb95101dab89",
            "operation": "DEPOSIT",
            "amount": 1000,
            "wallet_id": add_wallet[0].id
        },
        {
            "id": "b00ca877-e104-4e6e-bc67-e172bc6c61f0",
            "operation": "WITHDRAW",
            "amount": 200,
            "wallet_id": add_wallet[0].id
        },
        {
            "id": "420d0dd4-3074-46e5-b807-e3ca7feed1f5",
            "operation": "DEPOSIT",
            "amount": 500,
            "wallet_id": add_wallet[1].id
        },
    ]
    temp = [models.Transaction(**obj) for obj in transaction]
    return models.Transaction.objects.bulk_create(temp)
