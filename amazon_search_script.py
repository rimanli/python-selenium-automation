from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome(executable_path='/Users/royalimanli/Project_S360/python-selenium-automation/chromedriver')
driver.get('https://www.storespace.com/')

driver.find_element(By.XPATH, "//a[@href='https://www.storespace.com/find-storage']").click()

driver.find_element(By.ID, '').send_keys('Dallas, TX')