Feature: hoover happy path

  Scenario: same input as description
    Given we have behave app online and valid coord
    When the app is loaded on server
    Then the result is the expected
