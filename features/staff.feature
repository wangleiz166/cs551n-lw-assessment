Feature: staff
  """
  Confirm that we can browse the staff related pages on our site
  """

  Scenario: success for visiting staff and staff details pages
    Given the staff database is available
    When I navigate to the staff details page with id 1
    Then I should see the staff details for id 1
