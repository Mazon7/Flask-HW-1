from flask import Flask, request
import uuid

from model.calendar import Event
import logic

app = Flask(__name__)

_calendar_logic = logic.CalendarLogic()


class ApiException(Exception):
    pass


def _from_raw(raw_event: str) -> Event:
    parts = raw_event.split('|')
    if len(parts) == 3:
        event = Event()
        event.id = None
        event.date = parts[0]
        event.title = parts[1]
        event.text = parts[2]
        return event
    elif len(parts) == 4:
        event = Event()
        event.id = parts[0]
        event.date = parts[1]
        event.title = parts[2]
        event.text = parts[3]
        return event
    else:
        raise ApiException(f"invalid RAW event data {raw_event}")


def _to_raw(event: Event) -> str:
    if event.id is None:
        return f"{event.date}|{event.title}|{event.text}|"
    else:
        return f"{event.id}|{event.date}|{event.title}|{event.text}"


API_ROOT = "/api/v1"
CALENDAR_API_ROOT = API_ROOT + "/calendar"


@app.route(CALENDAR_API_ROOT + "/", methods=['POST'])
def create():
    try:
        data = request.get_data().decode('utf-8')
        event = _from_raw(data)
        _id = _calendar_logic.create(event)
        return f"new id: {_id}", 201
    except Exception as ex:
        return f"failed to CREATE event with: {ex}", 404


@app.route(CALENDAR_API_ROOT + "/", methods=['GET'])
def list():
    try:
        events = _calendar_logic.list()
        raw_events = ""
        for event in events:
            raw_events += _to_raw(event) + '\n'
        return raw_events, 200
    except Exception as ex:
        return f"failed to LIST events with: {ex}", 404


@app.route(CALENDAR_API_ROOT + "/<_id>/", methods=['GET'])
def read(_id: str):
    try:
        event = _calendar_logic.read(_id)
        raw_event = _to_raw(event)
        return raw_event, 200
    except Exception as ex:
        return f"failed to READ event with: {ex}", 404


@app.route(CALENDAR_API_ROOT + "/<_id>/", methods=['PUT'])
def update(_id: str):
    try:
        data = request.get_data().decode('utf-8')
        event = _from_raw(data)
        _calendar_logic.update(_id, event)
        return f"updated", 200
    except Exception as ex:
        return f"failed to UPDATE event with: {ex}", 404


@app.route(CALENDAR_API_ROOT + "/<_id>/", methods=['DELETE'])
def delete(_id: str):
    try:
        _calendar_logic.delete(_id)
        return "deleted", 200
    except Exception as ex:
        return f"failed to DELETE event with: {ex}", 404
