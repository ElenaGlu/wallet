import pytest

from app import models


@pytest.fixture()
def printer(restaurant):
    printer = [
        {
            "id": 1,
            "title": "printer_A1",
            "restaurant_id": restaurant[0].id
        },
        {
            "id": 2,
            "title": "printer_A2",
            "restaurant_id": restaurant[0].id
        },
        {
            "id": 3,
            "title": "printer_B1",
            "restaurant_id": restaurant[1].id
        },

    ]
    temporary = []
    for obj in printer:
        temporary.append(models.Printer(**obj))
    return models.Printer.objects.bulk_create(temporary)