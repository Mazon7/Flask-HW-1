'''
Requirements:
— maximum title length — 30 symbols
— maximum text length — 200 symbols
— can not add more than one event per day
'''
from typing import List
from datetime import datetime
from model.calendar import Event, UUID
import db


TITLE_LIMIT = 30
TEXT_LIMIT = 200


class LogicException(Exception):
    pass


class CalendarLogic:
    def __init__(self):
        self._event_db = ''

    @staticmethod
    def validate_event(event: Event):
        if event is None:
            raise Exception('event is None')
        if event.title is None or (len(event.title) == 0 or len(event.title) > TITLE_LIMIT):
            raise Exception(
                f'Title is not within a range of 0-{TITLE_LIMIT} symbols')
        if event.text is None or (len(event.text) == 0 or len(event.text) > TEXT_LIMIT):
            raise Exception(
                f'Text is not within a range of 0-{TEXT_LIMIT} symbols')

    @staticmethod
    def event_number_check(event: Event):
        # TODO: update condition
        if 'check that this date is already in the list of events':
            raise Exception(f'Can not create event for {event.date}!')

    def create(self, event: Event) -> str:
        self.validate_event(event)
        try:
            return ''  # create in db
        except Exception as ex:
            raise LogicException(f"failed CREATE operation with: {ex}")

    def list(self) -> List[Event]:
        try:
            return ''  # list in db
        except Exception as ex:
            raise LogicException(f"failed LIST operation with: {ex}")

    def read(self, _id: UUID) -> Event:
        try:
            return ''  # read in db by _id
        except Exception as ex:
            raise LogicException(f"failed READ operation with: {ex}")

    def update(self, _id: UUID, event: Event):
        self.validate_event(event)
        try:
            return ''  # update in db by _id
        except Exception as ex:
            raise LogicException(f"failed UPDATE operation with: {ex}")

    def remove(self, _id: UUID):
        try:
            return ''  # delete in db by _id
        except Exception as ex:
            raise LogicException(f"failed DELETE operation with: {ex}")
