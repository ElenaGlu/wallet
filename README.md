## _Веб-Приложение wallet_

Веб-приложение для управления балансом кошелька.
Позволяет выполнять операции пополнения и снятия, а также получать текущий баланс по уникальному идентификатору кошелька.

API принимает запрос вида:

### POST `/api/v1/wallets/<WALLET_UUID>/operation`

Осуществляет операцию пополнения или снятия средств с кошелька.

#### Пример запроса:
```json
POST /api/v1/wallets/<WALLET_UUID>/operation
Content-Type: application/json

{
  "operationType": "DEPOSIT", // или "WITHDRAW"
  "amount": 1000
}

### GET `/api/v1/wallets/<WALLET_UUID>`

получает баланс кошелька


### Технологии:

Python3, Django, PostgreSQL, Poetry, Docker Compose, Pytest

### Тестирование:

Использован Pytest для написания интеграционных тестов и создания тестовой бд.

```
Запустить тесты можно командой: pytest из директории /wallet

Структура проекта
/app
  /tests              # Директория с тестами
      api.py          # Тесты для API
```

### Запуск проекта на локальной машине:

- Клонировать репозиторий:
```
https://github.com/ElenaGlu/wallet.git
cd wallet
```
```
sudo docker compose up --build
```
