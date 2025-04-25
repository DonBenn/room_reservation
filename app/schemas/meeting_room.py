from typing import Optional

from pydantic import BaseModel, Field, validator


class MeetingRoomCreate(BaseModel):
    name: str = Field(
        ..., max_length=100,
        title='Полное имя', description='Можно вводить в любом регистре'
    )
    description: Optional[str]

    @validator('name')
    # Первый параметр функции-валидатора должен называться строго cls.
    # Вторым параметром идет проверяемое значение, его можно назвать как угодно.
    # Декоратор @classmethod ставить нельзя, иначе валидатор не сработает.
    def name_cant_be_numeric(cls, value: str):
        # Проверяем, не состоит ли строка исключительно из цифр:
        # if value.isnumeric():
        #     # При ошибке валидации можно выбросить
        #     # ValueError, TypeError или AssertionError.
        #     # В нашем случае подходит ValueError.
        #     # В аргумент передаём сообщение об ошибке.
        #     raise ValueError('Имя не может быть числом')
        if len(value) > 100:
            raise ValueError('Слишком длинное имя, не более 100 символов')
        # Если проверка пройдена, возвращаем значение поля.
        return value