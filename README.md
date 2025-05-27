## _Веб-Приложение wallet_

Веб-приложение для управления балансом кошелька.
Позволяет выполнять операции пополнения и снятия, а также получать текущий баланс по уникальному идентификатору кошелька.

  | Эндпоинт                                    | Назначение                          | 
|-----------------------------------------------|-------------------------------------|
|POST `/api/v1/wallets/<WALLET_UUID>/operation` | Пополнение/снятие средств с кошелька| 
|GET `/api/v1/wallets/<WALLET_UUID>`            | Получение баланса кошелька|

Пример запроса:
```
POST /api/v1/wallets/<WALLET_UUID>/operation
Content-Type: application/json

{
  "operationType": "DEPOSIT", // или "WITHDRAW"
  "amount": 1000
}
```

### Технологии:

Python3, Django, PostgreSQL, Poetry, Docker Compose, Pytest

Интеграционные тесты включают - положительные и негативные сценарии.
- Запуск тестов - команда pytest из директории /wallet
```
/app
  /tests          
      test_wallet_get.py 
      test_wallet_update.py
```

