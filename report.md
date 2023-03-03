# Staff program

## Introduction

staff Application to display a list of employee information. This project was developed using Flask framework for Python, SQLite database and Bootstrap front-end framework.

## design

### Database Design

The application uses a SQLite database to store employee information data. The specific database design is as follows:

#### staff_information Table

| Listings               | Type     | describe                 |
| ------------------| --------|----------------------|
| employeeid         | INTEGER | EmployeesID               |
| lastname           | TEXT    | Employee Surname             |
| firstname          | TEXT    | Employee Name             |
| gender             | TEXT    | Employee Sex             |
| email              | TEXT    | Employee Email             |
| phonenumber        | TEXT    | Employee Phone number         |
| city               | TEXT    | Employee City             |
| state              | TEXT    | Employee state               |
| zip                | TEXT    | Employee Zip Code             |
| username           | TEXT    | Employee Username           |
| password           | TEXT    | Employee Password             |
| department         | TEXT    | Employee department         |
| jobtitle           | TEXT    | Employee jobtitle             |
| employeestatus     | TEXT    | Employee Employment Status         |
| dateofhire         | TEXT    | Employee Employment date         |
| dateoftermination  | TEXT    | Employee departure date         |
| age                | INTEGER | Employee age             |
| maritalstatus      | TEXT    | Employee Marital Status         |
| education          | TEXT    | Employee Education Level         |
| joblevel           | INTEGER | Employee Position Level         |
| jobrole            | TEXT    | Employee Job Roles         |
| jobroletype        | TEXT    | Employee Position Type         |
| businessunit       | TEXT    | Employee's business unit     |
| managementlevel    | INTEGER | Employee Management Level         |
| travel             | TEXT    | Employee Travel         |

#### staff_privacy_information Table

| Listings                        | Type     | describe                 |
| ---------------------------| --------|----------------------|
| employeeid                  | INTEGER | Employee ID               |
| attrition                   | TEXT    | Whether an employee leaves         |
| distancefromhome            | INTEGER | Distance between employee's home and company     |
| educationfield              | TEXT    | Employee's field of study         |
| monthlyincome               | INTEGER | Employee monthly income           |
| numcompaniesworked          | INTEGER | Number of companies the employee has worked for |
| over18                      | TEXT    | Whether the employee is at least 18 years old     |
| percentsalaryhike           | INTEGER | Employee Salary Increase Percentage   |
| standardhours               | INTEGER | Standard working hours for employees         |
| stockoptionlevel            | INTEGER | Employee Stock Option Levels     |
| totalworkingyears           | INTEGER | Employees' working years         |
| trainingtimeslastyear       | INTEGER | Number of training sessions for employees in the previous year |
| yearsatcompany              | INTEGER | Number of years an employee has worked at the company   |
| yearsincurrentrole          | INTEGER | Number of years the employee has worked in the current position |
| yearssincelastpromotion     | INTEGER | Number of years since the employee's last promotion |
| yearswithcurrmanager        | INTEGER | Number of years an employee has worked with their current manager |

### Front-end design

The application is designed using the Bootstrap front-end framework and includes the following pages:

- index.html：For displaying the list of employees.
- detail.html：For displaying employee details.
- chat_detail.html：For displaying feedback results from chatbots.

### Back-end design

The application is designed using Python's Flask framework and includes the following components:

- Flask应用程序：Used to process HTTP requests and responses.
- SQLite数据库：Used to store employee information and employee privacy information data.
- OpenAI库：For natural language processing and generating intelligent chat logs.

### Development

In developing the staff project, we accomplished the following tasks:

Write the front-end code: Designed the employee information display page and chatbot page using Bootstrap front-end framework.
Implementing back-end logic: Implemented back-end logic using the Flask framework, including handling HTTP requests and responses, connecting to SQLite databases, and calling the OpenAI API for artificial intelligence interaction.
Writing test cases: Used Behave to conduct automated testing and wrote test cases to test the functionality and performance of the application.
### Implementation
When deploying the staff project, we accomplished the following tasks.

Installed dependencies: Installed and configured Python dependencies for Flask, Flask Paginate, Behave, Selenium, and Gunicorn using Pyenv and virtual environment management tools.
Initialize the database: Initialized the SQLite database using the parse_csy.py script and imported employee information data and employee privacy information data.
Start the application: Run the Flask application using Gunicorn, ensuring it runs continuously in the background.
Access the application: Access the application URL in a web browser to view employee information and engage in intelligent conversations with the chatbot.

#### Unit Testing
The project uses Behave and Selenium for automated testing, which can be run using the following commands.

behave

The test cases are located under the features folder.
