## Сервис резервирования переговорных комнат

### Описание 
Асинхронное API приложение предоставляет возможность бронировать помещения на определённый период времени. 
У пользователя есть возможность забронировать свободное помещение, при этом приложение проверяет, 
не забронировал ли уже кто-то это помещение и свободно ли всё время, на которое бронируется эта переговорка. 
Реализованы CRUD-операции для модели комнат (Meeting Rooms) и для их резервации (Reservations), 
а также для регистрации и авторизации пользователей. 


### Используемые технологии:

* FastAPI, SQLAlchemy, Alembic, Uvicorn, FastAPI Users, Pydantic

### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:
```
git clone git@github.com:DonBenn/room_reservation.git
```

```
cd room_reservation
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv venv
```

* Если у вас Linux/macOS

    ```
    source venv/bin/activate
    ```

* Если у вас windows

    ```
    source venv/scripts/activate
    ```

Установить зависимости из файла requirements.txt:

```
python3 -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

Создайте файл .evn:
```
touch .evn
```

В файле `.evn` Создайте переменные указанные в файле `env.example`


**Команды для создания и инициализации бд:**

* Создание базы данных
 
В корневой директории проекта выполните команду:
```
alembic init --template async alembic
```

* Создание миграций
```
alembic revision --autogenerate -m "First migration"
```

* Применение миграций
```
alembic upgrade head
```

* Команда для запуска:

```
uvicorn app.main:app --reload

```


### Автор

Bessonov Denis (https://github.com/DonBenn)
