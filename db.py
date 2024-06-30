from typing import List

from model.calendar import Event
import storage


class DBException(Exception):
    pass


class EventDB:
    def __init__(self):
        self._storage = storage.LocalStorage()

    def create(self, event: Event) -> str:
        try:
            return self._storage.create(event)  # create in storage
        except Exception as ex:
            raise DBException(f"failed CREATE operation with: {ex}")

    def list(self) -> List[Event]:
        try:
            return self._storage.list()  # list in storage
        except Exception as ex:
            raise DBException(f"failed LIST operation with: {ex}")

    def read(self, _id: str) -> Event:
        try:
            return self._storage.read(_id)  # read in storage by _id
        except Exception as ex:
            raise DBException(f"failed READ operation with: {ex}")

    def update(self, _id: str, event: Event):
        try:
            return self._storage.update(_id, event)  # update in storage by _id
        except Exception as ex:
            raise DBException(f"failed UPDATE operation with: {ex}")

    def delete(self, _id: str):
        try:
            return self._storage.delete(_id)  # delete in storage by _id
        except Exception as ex:
            raise DBException(f"failed DELETE operation with: {ex}")
