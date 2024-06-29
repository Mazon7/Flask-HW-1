from flask import Flask, request
import uuid

from model import calendar

app = Flask(__name__)


API_ROOT = "/api/v1"
CALENDAR_API_ROOT = API_ROOT + "/calednar"


@app.route(CALENDAR_API_ROOT + "/", methods=['POST'])
def create():
    try:
        data = request.get_data().decode('utf-8')
        event = ''
        _id = ''
        return f"new id: {_id}", 201
    except Exception as ex:
        return f"failed to CREATE event with: {ex}", 404


@app.route(CALENDAR_API_ROOT + "/", methods=['GET'])
def list():
    try:
        events = ''
        raw_event = ""
        for event in events:
            raw_events += ''
        return raw_events, 200
    except Exception as ex:
        return f"failed to LIST events with: {ex}", 404


@app.route(CALENDAR_API_ROOT + "/<_id>/", methods=['GET'])
def read(_id: uuid.UUID):
    try:
        data = request.get_data().decode('utf-8')
        event = ''
        _id = ''
        return f"new id: {_id}", 200
    except Exception as ex:
        return f"failed to READ event with: {ex}", 404


@app.route(CALENDAR_API_ROOT + "/<_id>/", methods=['PUT'])
def update(_id: uuid.UUID):
    try:
        data = request.get_data().decode('utf-8')
        event = ''
        _id = ''
        return f"new id: {_id}", 200
    except Exception as ex:
        return f"failed to UPDATE event with: {ex}", 404


@app.route(CALENDAR_API_ROOT + "/<_id>/", methods=['DELETE'])
def delete(_id: uuid.UUID):
    try:
        # _calendar_logic().delete(_id)
        return "deleted", 200
    except Exception as ex:
        return f"failed to DELETE event with: {ex}", 404
