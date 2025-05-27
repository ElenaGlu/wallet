import pytest
from django.urls import reverse


@pytest.mark.django_db
def test_current_balance_success(client, add_transaction):
    url = reverse('get_wallet', kwargs={'wallet_id': 'f50ec0b7-f960-400d-91f0-c42a6d44e3d0'})
    response = client.get(url)
    resp_json = response.json()

    assert response.status_code == 200
    assert resp_json == [
        {
            'account_balance': '800.00'
        }
    ]


@pytest.mark.django_db
def test_get_wallet_invalid_uuid(client, add_transaction):
    url = reverse('get_wallet', kwargs={'wallet_id': '00000000-0000-0000-0000-000000000000'})
    response = client.get(url)
    assert response.status_code == 404
