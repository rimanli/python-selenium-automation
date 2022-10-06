from selenium.webdriver.common.by import By
from behave import given, when, then

@then('search results for coffee are shown')
def verify_search_results(context):
    expected_result = '"coffee"'
    actual_result = context.driver.find_element(By.XPATH, "//span[@class='a-color-state a-text-bold']").text
    assert expected_result == actual_result, f'Error! Expected {expected_result}, but got {actual_result}'



@then('Verifies that Your Amazon Cart is empty')
def verify_search_results(context):
    expected_result = '"Your Amazon Cart is empty"'
    actual_result = context.driver.find_element(By.CSS_SELECTOR, "#sc-active-cart h1").text()
    assert expected_result == actual_result, f'Error! Expected {expected_result}, but got {actual_result}'