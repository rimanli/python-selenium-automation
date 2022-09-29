from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome(executable_path='/Users/royalimanli/Project_S360/python-selenium-automation/chromedriver')

driver.get('https://www.amazon.com/ap/signin?_encoding=UTF8&accountStatusPolicy=P1&openid.assoc_handle=usflex&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.mode=checkid_setup&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&openid.ns.pape=http%3A%2F%2Fspecs.openid.net%2Fextensions%2Fpape%2F1.0&openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2Fgp%2Fcss%2Forder-history%3Fie%3DUTF8%26ref_%3Dnav_orders_first&pageId=webcs-yourorder&showRmrMe=1')

#Amazon logo
driver.find_element(By.XPATH, "//i[@class='a-icon a-icon-logo']")

#Continue button
driver.find_element(By.ID, "continue")

#Need help link
driver.find_element(By.XPATH, "//span[@class='a-expander-prompt']")

#Create your Amazon account button
driver.find_element(By.XPATH, "//a[@class='a-button-text']")

#Email field
driver.find_element(By.XPATH, "//a[@class='a-button-text']")

#Conditions of use link
driver.find_element(By.XPATH, "//div[@id='legalTextRow']//a[contains(@href, 'ap_signin_notification')]")

#Privacy Notice link
driver.find_element(By.XPATH, "//*[@href='/ref=ap_desktop_footer_privacy_notice'] //a[@class='a-link-normal']")




