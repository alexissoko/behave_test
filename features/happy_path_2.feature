Feature: hoover happy path 2

  Scenario: another input as from description
    Given we have behave app online and valid coord yet
    When the app is loaded still on server
    Then the result is again the expected
