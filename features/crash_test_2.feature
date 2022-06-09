Feature: wrong input type from user

  Scenario: wrong coorinates data types are provided
    Given we have behave app deployed
    When the app is up and running
    Then we get bad request from server
