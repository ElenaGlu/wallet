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
Запустить тесты можно командой: pytest

 Структура проекта
/tests                # Директория с тестами
    /api              # Тесты для API
```

### Запуск проекта на локальной машине:

- Клонировать репозиторий:
```
https://github.com/ElenaGlu/wallet.git
cd wallet
```

### Запустите проект:

```
sudo docker compose up --build
```
