# Created by royalimanli at 9/24/22
Feature: Verify that cart is empty
  # Enter feature description here

  Scenario: User cart is empty
    Given Open amazon page
    When Clicks on the cart icon
    Then Verifies that Your Amazon Cart is empty