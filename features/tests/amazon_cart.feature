# Created by hiraatique at 5/11/23
Feature: Test case scenario for verifying empty cart

  Scenario: User can navigate to empty cart
    Given Open amazon page
    When  Click on cart icon
    Then  Empty cart page is shown
