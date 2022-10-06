from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome(executable_path='/Users/royalimanli/Project_S360/python-selenium-automation/chromedriver')

driver.get('https://www.amazon.com/')
driver.find_element(By.CSS_SELECTOR, '#nav-cart-count-container > span.nav-cart-icon.nav-sprite').click()

expected_result = 'Your Amazon Cart is empty'
actual_result = driver.find_element(By.CSS_SELECTOR, "#sc-active-cart h1").text()
assert expected_result != actual_result, f'Error: Expected {expected_result}, but got {actual_result}'

print('Test case passed')
driver.quit()