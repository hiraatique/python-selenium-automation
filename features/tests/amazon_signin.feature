# Created by hiraatique at 5/11/23
Feature: Amazon sign-in page

  Scenario: Logged out user directed to sign-in page when clicking on Returns and Orders
    Given Open amazon page
    When Click on orders
    When Verify sign-in header
    Then Verify input field is present



