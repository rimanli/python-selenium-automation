from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

@given('Open amazon page')
def open_amazon(context):
    context.driver.get('https://amazon.com/')



@when('Search for coffee')
def search_product(context):
    context.driver.find_element(By.ID, 'twotabsearchtextbox').send_keys('coffee')
    context.driver.find_element(By.ID, 'nav-search-submit-button').click()