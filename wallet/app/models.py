import uuid

from django.db import models


class OperationType(models.TextChoices):
    deposit = 'DEPOSIT'
    withdraw = 'WITHDRAW'


class Wallet(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    operation = models.CharField(max_length=8, choices=OperationType.choices)
    amount = models.DecimalField(max_digits=8, decimal_places=2)
