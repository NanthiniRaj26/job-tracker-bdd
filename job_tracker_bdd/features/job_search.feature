Feature: Job Search Automation

  Scenario: Search for Python Selenium jobs
    Given I launch the Edge browser
    When I open the job portal
    And I search for "Python Selenium Tester" in "Chennai"
    Then I should see a list of job results
