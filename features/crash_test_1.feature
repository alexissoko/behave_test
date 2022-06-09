Feature: message of error for user coord

  Scenario: woring coorinates are provided
    Given we have behave app on server
    When the app is running for the test
    Then app returns error on input
