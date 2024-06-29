from datetime import datetime, date
from uuid import UUID


class Event:
    def __init__(self, id: UUID, date: datetime, title: str, text: str):
        self.id = id
        self.date = date
        self.title = title
        self.text = text
