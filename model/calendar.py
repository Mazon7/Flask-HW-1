# from datetime import datetime
# from uuid import UUID, uuid4


class Event:
    id: str
    date: str
    title: str
    text: str
    # class wich is better for FOR JSON data type
    # # def __init__(self, id: UUID, date: datetime, title: str, text: str):
    #     self.id = id
    #     self.date = date
    #     self.title = title
    #     self.text = text
