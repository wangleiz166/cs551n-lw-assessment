from behave import given, when, then
import sqlite3

@given(u'the staff database is available')
def staff_db_available(context):
    """
    Ensure that the staff database is available
    """
    conn = sqlite3.connect('staff_information.db')
    context.cursor = conn.cursor()

@when(u'I navigate to the staff details page with id {id}')
def navigate_to_staff_details(context, id):
    """
    Navigate to the staff details page for the specified id
    """
    context.browser.get(f'http://localhost:5000/detail?id={id}')

@then(u'I should see the staff details for id {id}')
def verify_staff_details(context, id):
    """
    Verify that the staff details for the specified id are displayed
    """
    expected_url = f'http://localhost:5000/detail?id={id}'
    expected_name = context.cursor.execute(f"SELECT firstname, lastname FROM staff_information WHERE employeeid = {id}").fetchone()
    expected_name = f"{expected_name[0]} {expected_name[1]}"

    assert context.browser.current_url == expected_url
    assert expected_name in context.browser.page_source

    context.cursor.close()
