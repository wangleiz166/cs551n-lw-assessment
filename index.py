import sqlite3
import openai
from flask import Flask, render_template , request

app = Flask(__name__)

def title():
    title = 'staff'
    return title

def get_index_rows(page, page_size):
    # open the connection to the database
    conn = sqlite3.connect('staff_information.db')
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    offset = (page - 1) * page_size
    cur.execute("select * from staff_information limit ? offset ?", (page_size, offset))
    rows = cur.fetchall()

    # count the total number of rows in the table
    cur.execute("select count(*) from staff_information")
    total_rows = cur.fetchone()[0]
    
    # calculate the total number of pages
    total_pages = (total_rows + page_size - 1) // page_size

    # calculate the page numbers to display in the pagination links
    if total_pages <= 10:
        pages = range(1, total_pages + 1)
    else:
        if page <= 5:
            pages = range(1, 11)
        elif page >= total_pages - 4:
            pages = range(total_pages - 9, total_pages + 1)
        else:
            pages = range(page - 5, page + 6)

    # create a dictionary with pagination information
    pagination = {
        'has_prev': page > 1,
        'prev_num': page - 1 if page > 1 else None,
        'page': page,
        'pages': pages,
        'next_num': page + 1 if page < total_pages else None,
        'has_next': page < total_pages,
        'total_pages': total_pages
    }

    conn.close()

    return rows, pagination

@app.route('/')
def index():
    get_title = title()
    page = request.args.get('page', 1, type=int)
    page_size = 10
    rows, pagination = get_index_rows(page, page_size)
    return render_template('index.html', title=get_title, rows=rows, pagination=pagination)


def get_detail(id):
    # open the connection to the database
    conn = sqlite3.connect('staff_information.db')
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    cur.execute("""
            select * from staff_information as a left join staff_privacy_information as b 
            on a.employeeid = b.employeeid  where a.employeeid = ? 
        """, (id,))
    row = cur.fetchone()
    conn.close()
    return row

@app.route('/detail')
def detail():
    get_title = title()
    id = request.args.get('id')
    detail_re = get_detail(id)
    return render_template('detail.html', title=get_title,detail_row=detail_re)

@app.route('/chatgpt')
def chatgpt():
    get_title = title()
    id = request.args.get('id')
    detail_re = get_chatgpt(id)
    return render_template('chat_detail.html', title=get_title,detail_row=detail_re)

def get_chatgpt(id):
    detail_re = get_detail(id)
    fields = ['age', 'attrition', 'businesstravel', 'department', 'distancefromhome', 
            'education', 'educationfield', 'employeecount', 'gender', 'joblevel', 
            'jobrole', 'maritalstatus', 'monthlyincome', 'numcompaniesworked', 
            'over18', 'percentsalaryhike', 'standardhours', 'stockoptionlevel', 
            'totalworkingyears', 'trainingtimeslastyear', 'yearsatcompany', 
            'yearssincelastpromotion', 'yearswithcurrmanager', 'environmentsatisfaction', 
            'jobsatisfaction', 'worklifebalance', 'performancerating']
    detail_string = '\n'.join([f"{field.capitalize().replace('_', ' ')}: {detail_re[field]}" for field in fields])
    detail_string += "\nBased on the information above How to better help this employee with his work life and how to talk to the departing employee?"

    return generate_text(detail_string)



openai.api_key = "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"

def generate_text(prompt):
    completions = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )

    message = completions.choices[0].text
    return message.strip()    