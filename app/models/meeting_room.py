from sqlalchemy import Column, String, Text

from app.core.db import Base


class MeetingRoom(Base):
    name = Column(String(100), unique=True, nullable=False)
    # Новый атрибут модели. Значение nullable по умолчанию равно True,
    # поэтому его можно не указывать.
    description = Column(Text)