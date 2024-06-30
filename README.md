# Guide

### Setup and Installation
- Clone the repo
- Navigate to the root directory of the project
- Activate the virtual environment. Check how to [here](https://docs.python.org/3/library/venv.html).
- Install all dependacies from `requirements.txt` file by running the command `pip install -r requirements.txt` in the terminal

### Run app
- In the terminal run the following command: `flask run`
- <font color="red">*Be aware that the app runs in the debug mode. You can change it in the file `server.py`*</font>

### How to test
Use the following curl commands in the terminal to test:

**CREATE Event:**

`curl --location 'localhost:5000/api/v1/calendar' 
--header 'Content-Type: text/plain' \
--data 'YYYY-MM-DD|<title>|<text>|'`

**LIST all Events:**

`curl --location 'localhost:5000/api/v1/calendar'`

**GET Event by id:**

`curl --location 'localhost:5000/api/v1/calendar/<id>'`

**UPDATE Event by id:**

`curl --location --request PUT 'localhost:5000/api/v1/calendar/<id>' \
--header 'Content-Type: text/plain' \
--data '<id>|YYYY-MM-DD|<title>|<text>'`

**DELETE Event by id:**

`curl --location --request DELETE 'localhost:5000/api/v1/calendar/'<id>'`

Where:
```
id - string of UUID format
date - string of the 'YYYY-MM-DD' format
title - string from 0 to 30 symbols
text - string from 0 to 200 symbols
```

