from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome(executable_path='/Users/royalimanli/Project_S360/python-selenium-automation/chromedriver')

driver.get('https://www.amazon.com/')
driver.find_element(By.XPATH, "//a[@href= '/gp/css/order-history?ref_=nav_orders_first']").click()
driver.find_element(By.ID, 'ap_email').send_keys('imanlirr@gmail.com')
assert driver.find_element(By.ID, 'ap_email').is_displayed(), 'Email shown'

expected_result = 'Sign In'
actual_result = driver.find_element(By.XPATH, "//h1[@class='a-spacing-small']").text
assert expected_result != actual_result, f'Error: Expected {expected_result}, but got {actual_result}'

print('Test case passed')
driver.quit()

