### Installation

Clone or download the project code：
```shell
git clone https://github.com/wangleiz166/cs551n-lw-assessment.git
```
Go to the project catalogue：
```shell
cd app
```
Create and activate a Python virtual environment：
```shell
python3 -m venv .venv
source .venv/bin/activate
```
Install the Python dependencies required for the project：
```shell
pip install -r requirements.txt
```
Initialise and import data
```shell
python3 arse_csv.py
```
Running the application (codio run as an example)
```shell
export FLASK_APP=app.py

python3 -m flask run -h 0.0.0.0
```

### Use
When using the staff project, you can perform the following tasks.

1. View staff information: On the staff list page, view the name, position, department and job number of all staff.
2. View staff details: Click the Details button on the staff list to view staff details, including age, gender, job role, job satisfaction, etc.
3. AI Analysis: Clicking on the 'Analysis' button on the employee details page will send all the information about the employee to openai, which will provide openai with advice on work and life.
In summary, the staff project is a web application developed using Flask and SQLite that includes employee information management and artificial intelligence features that can be used to present and manage employee information and provide work and life advice to employees. The staff project can be easily deployed and used across different operating systems and computers by using github and render for versioning and deployment.

Translated with www.DeepL.com/Translator (free version)

render-url: https://lw-staff.onrender.com/
