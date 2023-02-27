import csv
import sqlite3

# open the connection to the database
conn = sqlite3.connect('staff_information.db')
cur = conn.cursor()

# drop the data from the table so that if we rerun the file, we don't repeat values
conn.execute('DROP TABLE IF EXISTS staff_information')
print("table dropped successfully");
# create table again
cur.execute("""
    CREATE TABLE staff_information (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        employeeid INTEGER,
        age INTEGER,
        attrition TEXT,
        department TEXT,
        education INTEGER,
        educationfield TEXT,
        gender TEXT,
        joblevel INTEGER,
        jobrole TEXT,
        maritalstatus TEXT,
        monthlyincome INTEGER,
        numcompaniesworked INTEGER,
        over18 TEXT,
        percentsalaryhike INTEGER,
        standardhours INTEGER,
        stockoptionlevel INTEGER,
        totalworkingyears INTEGER,
        trainingtimeslastyear INTEGER,
        yearsatcompany INTEGER,
        yearssincelastpromotion INTEGER,
        yearswithcurrmanager INTEGER
    );
""")
print("table staff_information created successfully");


# drop the data from the table so that if we rerun the file, we don't repeat values
conn.execute('DROP TABLE IF EXISTS staff_privacy_information')
print("table dropped successfully");
# create table again
cur.execute("""
    CREATE TABLE staff_privacy_information (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        businesstravel TEXT,
        distancefromhome INTEGER,
        employeecount INTEGER,
        environmentsatisfaction INTEGER,
        jobsatisfaction INTEGER,
        worklifebalance INTEGER,
        performancerating INTEGER,
        employeeid INTEGER
    );
""")
print("table staff_privacy_information created successfully");


with open('staff_information/staff_information.csv', newline='') as f:
    reader = csv.reader(f, delimiter=",")
    next(reader) # skip the header line
    for row in reader:
        try:
            employeeid = int(row[0])
        except ValueError:
            employeeid = 0
        try:
            age = int(row[1])
        except ValueError:
            age = 0
        try:
            attrition = row[2]
        except ValueError:
            attrition = ""
        try:
            department = row[3]
        except ValueError:
            department = ""
        try:
            education = int(row[4])
        except ValueError:
            education = 0
        try:
            educationfield = row[5]
        except ValueError:
            educationfield = ""
        try:
            gender = row[6]
        except ValueError:
            gender = ""
        try:
            joblevel = int(row[7])
        except ValueError:
            joblevel = 0
        try:
            jobrole = row[8]
        except ValueError:
            jobrole = ""
        try:
            maritalstatus = row[9]
        except ValueError:
            maritalstatus = ""
        try:
            monthlyincome = int(row[10])
        except ValueError:
            monthlyincome = 0
        try:
            numcompaniesworked = int(row[11])
        except ValueError:
            numcompaniesworked = 0
        try:
            over18 = row[12]
        except ValueError:
            over18 = ""
        try:
            percentsalaryhike = int(row[13])
        except ValueError:
            percentsalaryhike = 0
        try:
            standardhours = int(row[14])
        except ValueError:
            standardhours = 0
        try:
            stockoptionlevel = int(row[15])
        except ValueError:
            stockoptionlevel = 0
        try:
            totalworkingyears = int(row[16])
        except ValueError:
            totalworkingyears = 0
        try:
            trainingtimeslastyear = int(row[17])
        except ValueError:
            trainingtimeslastyear = 0
        try:
            yearsatcompany = int(row[18])
        except ValueError:
            yearsatcompany = 0
        try:
            yearssincelastpromotion = int(row[19])
        except ValueError:
            yearssincelastpromotion = 0
        try:
            yearswithcurrmanager = int(row[20])
        except ValueError:
            yearswithcurrmanager = 0
            
        cur.execute('INSERT INTO staff_information (employeeid, age, attrition, department, education, educationfield, gender, joblevel, jobrole, maritalstatus, monthlyincome, numcompaniesworked, over18, percentsalaryhike, standardhours, stockoptionlevel, totalworkingyears, trainingtimeslastyear, yearsatcompany, yearssincelastpromotion, yearswithcurrmanager) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)', (employeeid, age, attrition, department, education, educationfield, gender, joblevel, jobrole, maritalstatus, monthlyincome, numcompaniesworked, over18, percentsalaryhike, standardhours, stockoptionlevel, totalworkingyears, trainingtimeslastyear, yearsatcompany, yearssincelastpromotion, yearswithcurrmanager))
        conn.commit()

print("data staff_information parsed successfully")

with open('staff_information/staff_privacy_information.csv', newline='') as f:
    reader = csv.reader(f, delimiter=",")
    next(reader) # skip the header line
    for row in reader:
        try:
            businesstravel = row[0]
        except ValueError:
            businesstravel = ""
        try:
            distancefromhome = int(row[1])
        except ValueError:
            distancefromhome = 0
        try:
            employeecount = int(row[2])
        except ValueError:
            employeecount = 0
        try:
            environmentsatisfaction = int(row[3])
        except ValueError:
            environmentsatisfaction = 0
        try:
            jobsatisfaction = int(row[4])
        except ValueError:
            jobsatisfaction = 0
        try:
            worklifebalance = int(row[5])
        except ValueError:
            worklifebalance = 0
        try:
            performancerating = int(row[6])
        except ValueError:
            performancerating = 0
        try:
            employeeid = int(row[7])
        except ValueError:
            employeeid = 0
            
        cur.execute('INSERT INTO staff_privacy_information (businesstravel, distancefromhome, employeecount, environmentsatisfaction, jobsatisfaction, worklifebalance, performancerating, employeeid) VALUES (?,?,?,?,?,?,?,?)', (businesstravel, distancefromhome, employeecount, environmentsatisfaction, jobsatisfaction, worklifebalance, performancerating, employeeid))
        conn.commit()

print("data staff_privacy_information parsed successfully")


conn.close()
        