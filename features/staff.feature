Feature: staff
""" 
Confirm that we can browse the staff related pages on our site
"""

Scenario: success for visiting staff and staff details pages
    Given:I navigate to the staff page
    When:I click on the link to staff details
    Then:I should see the details for that staff

