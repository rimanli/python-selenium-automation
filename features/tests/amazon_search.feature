# Created by royalimanli at 9/24/22
Feature: Test for amazon search
  # Enter feature description here

  Scenario: User can search for a product
    Given Open amazon page
    When Search for coffee
    Then Search results for coffee are shown