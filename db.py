from model.calendar import Event, UUID
from typing import List


class DBException(Exception):
    pass


class EventDB:
    def __init__(self):
        self._event = 'storage object'

    def create(self, event: Event) -> str:
        try:
            return ''  # create in storage
        except Exception as ex:
            raise DBException(f"failed CREATE operation with: {ex}")

    def list(self) -> List[Event]:
        try:
            return ''  # list in storage
        except Exception as ex:
            raise DBException(f"failed LIST operation with: {ex}")

    def read(self, _id: UUID) -> Event:
        try:
            return ''  # read in storage by _id
        except Exception as ex:
            raise DBException(f"failed READ operation with: {ex}")

    def update(self, _id: UUID, event: Event):
        try:
            return ''  # update in storage by _id
        except Exception as ex:
            raise DBException(f"failed UPDATE operation with: {ex}")

    def remove(self, _id: UUID):
        try:
            return ''  # delete in storage by _id
        except Exception as ex:
            raise DBException(f"failed DELETE operation with: {ex}")
