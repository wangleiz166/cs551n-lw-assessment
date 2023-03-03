# Staff Application Project

## What is it?
This is a web application for managing employee information and analyzing their work-related issues using artificial intelligence. The application allows users to view a list of employees and their details, as well as perform an analysis on their information using a chatbot powered by GPT.

The application is built using Python and Flask, and uses a SQLite database to store the employee information. The front-end is designed using Bootstrap and Jinja2 templates.

The GPT chatbot is powered by OpenAI's GPT-3 API, which provides natural language processing and machine learning capabilities. The chatbot can provide personalized advice to employees based on their information, and can help managers identify and address issues related to employee satisfaction, productivity, and retention.

The application is intended for use by HR managers and other personnel involved in employee management and engagement. It provides a convenient and efficient way to track employee information and gain insights into their needs and concerns.

## Main Features

1. View Staff Information: On the Staff List page, view the name, position, department, and employee ID of all staff members.
2. View staff details: Click the Details button on the staff list to view staff details, including age, gender, job role, job satisfaction, etc.
3. AI Analysis: Clicking on the 'Analysis' button on the employee details page will send all the information about the employee to openai, which will provide openai with advice on work and life.


## Installation

Clone or download the project code：
```shell
git clone https://github.com/wangleiz166/cs551n-lw-assessment.git
```
Go to the project catalogue：
```shell
cd cs551n-lw-assessmentp
```
install and set the local version of Python to 3.7.0 using the pyenv version manager.
```shell
pyenv install 3.7.0
pyenv local 3.7.0
```

Create and activate a Python virtual environment：
```shell
python3 -m venv .venv
source .venv/bin/activate
```
Install the Python dependencies required for the project：
```shell
pip install --upgrade pip
pip install flask
pip install openai
```
Initialise and import data
```shell
python3 arse_csv.py
```

## Running the application

#### Codio Running the application
```shell
export FLASK_APP=staff.py

python3 -m flask run -h 0.0.0.0
```

#### Local operation Running the application
```shell
export FLASK_APP=staff.py

python3 -m flask run
```
#### Render Running the application
1.Open address https://render.com/ Register Login

2.Click Dashboard Click "NEW" , "Web Service"

3.Connect our repository

4.Fill in as follows（eg:）

    name:  lw-staff
    Environment: Python3
    Build command: $ pip install -r requirements.txt
    Start command: $ gunicorn staff:app

5.Click 'Create Web Service'

6.Until build successfully

7.Access：https://lw-staff.onrender.com/
