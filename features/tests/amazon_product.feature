# Created by hiraatique at 5/20/23
Feature: Test case for Add Product


  Scenario: User can add product in cart
   Given Open amazon page
    When Search for Kook Glass Carafe Pitchers
    And Click on the first product
    And Click on Add to cart button
    And Click on cart icon
    Then Verify cart has 1 item