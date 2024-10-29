import json

import pytest
from django.urls import reverse


@pytest.mark.django_db
def test_update_wallet(client, order):
    url = reverse('create_order_for_receipt')
    order_info = json.dumps(
        {
            'title': 'ABC',
            'restaurant': 'restaurant-A',
        }
    )
    response = client.post(url, order_info, content_type='application/json')
    assert response.status_code == 201