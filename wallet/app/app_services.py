import uuid
from typing import Dict, Union, Any

from django.db.models import F

from app.models import Transaction, Wallet
from exceptions import ErrorType, AppError

schemas = {
    'update_wallet': {
            'type': 'object',
            'required': ['operationType', 'amount'],
            'properties': {
                'operationType': {
                    'type': 'string',
                },
                'amount': {
                    'type': 'number',
                },
            },
        },
}


class WalletHandler:

    def __init__(self, wallet_id: str, data_wallet: Dict[str, Union[str, int]] = None):
        self.wallet_id = wallet_id
        self.data_wallet = data_wallet

    def check_wallet(self) -> None:
        """
        Check wallet's UUID.
        :return: None
        :raises AppError: if UUID invalid
        """
        uuid_wallet = Wallet.objects.filter(pk=self.wallet_id).first()
        mapper = {
            'deposit': self.deposit,
            'withdraw': self.withdraw
        }
        if uuid_wallet:
            mapper[self.data_wallet['operationType']](self.wallet_id, self.data_wallet)
        else:
            raise AppError(
                {
                    'error_type': ErrorType.UUID_ERROR,
                    'description': 'Invalid UUID'
                }
            )

    def deposit(self, wallet_id: str, data_wallet: Dict[str, Union[str, int]]) -> None:
        """
        Increase the wallet balance.
        :param data_wallet: dict with key- 'operationType', 'amount'
        :param wallet_id: example, 'a8098c1a-f86e-11da-bd1a-00112444be1e'
        :return: None
        :raises AppError: if the deposit amount is negative
        """
        if data_wallet['amount'] > 0:
            data = {
                'id': str(uuid.uuid4()),
                'wallet_id': self.wallet_id,
                'operation': data_wallet['operationType'],
                'amount': data_wallet['amount']
            }
            Transaction.objects.create(**data)
            Wallet.objects.filter(pk=self.wallet_id).update(account_balance=F('account_balance') + data_wallet['amount'])
        else:
            raise AppError(
                {
                    'error_type': ErrorType.AMOUNT_ERROR,
                    'description': 'the deposit amount cannot be negative'
                }
            )

    def withdraw(self, wallet_id: str, data_wallet: Dict[str, Union[str, int]]) -> None:
        """
        Reduce the wallet balance.
        :param data_wallet:  dict with key- 'operationType', 'amount'
        :param wallet_id: example, 'a8098c1a-f86e-11da-bd1a-00112444be1e'
        :return: None
        :raises AppError: if the withdrawal amount is negative
        """
        available_amount = list(Wallet.objects.filter(pk=self.wallet_id).values('account_balance'))[0]['account_balance']
        if data_wallet['amount'] > 0 and available_amount - data_wallet['amount'] >= 0:
            data = {
                'id': str(uuid.uuid4()),
                'wallet_id': self.wallet_id,
                'operation': data_wallet['operationType'],
                'amount': data_wallet['amount']
            }
            Transaction.objects.create(**data)
            Wallet.objects.filter(pk=self.wallet_id).update(account_balance=F('account_balance') - data_wallet['amount'])
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

        account_balance = list(Wallet.objects.filter(pk=self.wallet_id).values('account_balance'))
        if account_balance:
            return account_balance
        else:
            raise AppError(
                {
                    'error_type': ErrorType.UUID_ERROR,
                    'description': 'Invalid UUID'
                }
            )


