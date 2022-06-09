Feature: hoover happy path 2

  Scenario: another input as from description
    Given we have behave app online one more time
    When the app is running
    Then the result is zero this time
