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
cd cs551n-lw-assessment
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

##Test
Run the behave command to see the results
```shell
behave
```
![image](https://github.com/wangleiz166/studyInAberdeen/blob/main/%E5%BE%AE%E4%BF%A1%E5%9B%BE%E7%89%87_20230304012443.png)

##Test installation process notes
1.Installing selenium
```shell
pip install selenium
```
2.Install a suitable browser for your linux environment and install a stable version. Please note that you will need root or administrator privileges to install the package.
```shell
wget -q -O - https://dl.google.com/linux/linux_signing_key.pub | sudo apt-key add -
echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" | sudo tee /etc/apt/sources.list.d/google-chrome.list
sudo apt-get update
sudo apt-get install google-chrome-stable
```

3.Check the version of your browser
```shell
google-chrome --version
```
![image](https://github.com/wangleiz166/studyInAberdeen/blob/main/%E5%BE%AE%E4%BF%A1%E6%88%AA%E5%9B%BE_20230304012716.png)

4.Visit https://sites.google.com/chromium.org/driver/downloads to find a corresponding version of the chrome driver to download
![image](https://github.com/wangleiz166/studyInAberdeen/blob/main/%E5%BE%AE%E4%BF%A1%E6%88%AA%E5%9B%BE_20230226215954.png)

5.Move the downloaded chromedriver file to the /usr/local/bin/ directory and give it executable permissions. This can be done using the following command.
```shell
sudo mv ~/Downloads/chromedriver /usr/local/bin/
sudo chmod +x /usr/local/bin/chromedriver
```
6.Start environment on top of codio

7.Run the behave command to see the results
