'''
Requirements:
— maximum title length — 30 symbols
— maximum text length — 200 symbols
— can not add more than one event per day
'''
from typing import List
from model.calendar import Event
import db


TITLE_LIMIT = 30
TEXT_LIMIT = 200


class LogicException(Exception):
    pass


class CalendarLogic:
    def __init__(self):
        self._event_db = db.EventDB()

    @staticmethod
    def _validate_event(event: Event):
        if event is None:
            raise Exception('event is None')
        if event.title is None or (len(event.title) == 0 or len(event.title) > TITLE_LIMIT):
            raise Exception(
                f'Title is not within a range of 0-{TITLE_LIMIT} symbols')
        if event.text is None or (len(event.text) == 0 or len(event.text) > TEXT_LIMIT):
            raise Exception(
                f'Text is not within a range of 0-{TEXT_LIMIT} symbols')

    # @staticmethod
    def _event_number_check(self, event):
        # TODO: update conditions
        events = self._event_db.list()

        # Do not consider event's date if you update it, so that user can update with the same date
        for existed_event in events:
            if existed_event.id == event.id:
                events.remove(existed_event)
                break

        for existed_event in events:
            if existed_event.date == event.date:
                # if 'check that this date is already in the list of events':
                raise Exception(f'Can not create event for {event.date}!')

    def create(self, event: Event) -> str:
        self._validate_event(event)
        self._event_number_check(event)
        try:
            return self._event_db.create(event)  # create in d
        except Exception as ex:
            raise LogicException(f"failed CREATE operation with: {ex}")

    def list(self) -> List[Event]:
        try:
            return self._event_db.list()  # list in db
        except Exception as ex:
            raise LogicException(f"failed LIST operation with: {ex}")

    def read(self, _id: str) -> Event:
        try:
            return self._event_db.read(_id)  # read in db by _id
        except Exception as ex:
            raise LogicException(f"failed READ operation with: {ex}")

    def update(self, _id: str, event: Event):
        self._validate_event(event)
        self._event_number_check(event)
        try:
            return self._event_db.update(_id, event)  # update in db by _id
        except Exception as ex:
            raise LogicException(f"failed UPDATE operation with: {ex}")

    def delete(self, _id: str):
        try:
            return self._event_db.delete(_id)  # delete in db by _id
        except Exception as ex:
            raise LogicException(f"failed DELETE operation with: {ex}")
