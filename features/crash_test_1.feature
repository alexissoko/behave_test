Feature: message of error for user coord

  Scenario: wrong coorinates are provided
    Given we have behave app on server
    When the app is running for the test
    Then the coordinate input field shows error
