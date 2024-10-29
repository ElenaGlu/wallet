from typing import Dict, Union, Any

from django.db.models import F

from app.models import Wallet
from exceptions import ErrorType, AppError


class WalletHandler:

    def __init__(self, uuid: str, data_wallet: Dict[str, Union[str, int]]):
        self.uuid = uuid
        self.operationType = data_wallet['operationType']
        self.amount = data_wallet['amount']

    def check_wallet(self) -> None:
        """
        Check wallet's UUID.
        :return: None
        :raises AppError: if UUID invalid
        """
        uuid_wallet = Wallet.objects.filter(pk=self.uuid).first()
        mapper = {
            'deposit': self.deposit,
            'withdraw': self.withdraw
        }
        if uuid_wallet:
            mapper[self.operationType](self.amount)
        else:
            raise AppError(
                {
                    'error_type': ErrorType.UUID_ERROR,
                    'description': 'Invalid UUID'
                }
            )

    def deposit(self, new_amount: int) -> None:
        """
        Increase the wallet balance.
        :param new_amount: example, 1000
        :return: None
        :raises AppError: if the deposit amount is negative
        """
        if new_amount > 0:
            Wallet.objects.filter(pk=self.uuid).update(amount=F('amount') + new_amount)
        else:
            raise AppError(
                {
                    'error_type': ErrorType.AMOUNT_ERROR,
                    'description': 'the deposit amount cannot be negative'
                }
            )

    def withdraw(self, new_amount: int) -> None:
        """
        Reduce the wallet balance.
        :param new_amount: example, 1000
        :return: None
        :raises AppError: if the withdrawal amount is negative
        """
        available_amount = list(Wallet.objects.filter(pk=self.uuid).values('amount'))[0]['amount']
        if new_amount > 0 and available_amount - new_amount >= 0:
            Wallet.objects.filter(pk=self.uuid).update(amount=F('amount') - new_amount)
        else:
            raise AppError(
                {
                    'error_type': ErrorType.AMOUNT_ERROR,
                    'description': 'the withdraw amount cannot be negative'
                }
            )

    def get_current_balance(self) -> list[Any]:
        """
        Get current balance.
        :return: example, 100
        :raises AppError: if UUID invalid
        """

        uuid_wallet = list(Wallet.objects.filter(pk=self.uuid).first().values())
        if uuid_wallet:
            return uuid_wallet
        else:
            raise AppError(
                {
                    'error_type': ErrorType.UUID_ERROR,
                    'description': 'Invalid UUID'
                }
            )


