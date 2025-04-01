## _Веб-Приложение wallet_

приложение принимает запрос вида:

- POST api/v1/wallets/<WALLET_UUID>/operation
{
operationType: DEPOSIT or WITHDRAW,
amount: 1000
}
и выполняет логику по изменению счета в базе данных

- GET api/v1/wallets/{WALLET_UUID}
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
