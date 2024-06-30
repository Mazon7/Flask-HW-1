from typing import List

from model.calendar import Event
import uuid


class StorageException(Exception):
    pass


class LocalStorage:
    def __init__(self):
        self._storage = {}

    def create(self, event: Event) -> str:
        event.id = uuid.uuid4().hex
        self._storage[event.id] = event
        return event.id

    def list(self) -> List[Event]:
        return list(self._storage.values())

    def read(self, _id: str) -> Event:
        if _id not in self._storage:
            raise StorageException(f"{_id} not found in storage")
        return self._storage[_id]

    def update(self, _id: str, event: Event):
        if _id not in self._storage:
            raise StorageException(f"{_id} not found in storage")
        event.id = _id
        self._storage[event.id] = event

    def delete(self, _id: str):
        if _id not in self._storage:
            raise StorageException(f"{_id} not found in storage")
        del self._storage[_id]
