# Created by hiraatique at 6/9/23
Feature: homework 6

  Scenario:  User can open and close Amazon Privacy Notice
    Given Open Amazon T&C page
    When Store original windows
    And Click on Amazon Privacy Notice
    And Switch to the newly opened window
    Then Verify Amazon Privacy page is opened
    And User can close new window and switch back to original
    
