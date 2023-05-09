import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


serv_obj = Service("C:\webdriver3\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
driver.get("https://www.demoblaze.com/")

#Testing contact feature
driver.find_element(By.XPATH, "/html/body/nav/div[1]/ul/li[2]/a").click()
time.sleep(1)
driver.find_element(By.ID, "recipient-email").send_keys("gburn6394@gmail.com")
time.sleep(1)
driver.find_element(By.ID, "recipient-name").send_keys("GB testing")
time.sleep(1)
driver.find_element(By.ID, "message-text").send_keys("This is for testing purposes")
time.sleep(1)
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[3]/button[2]").click()
time.sleep(1)

#Testing the popup that will appear
popup3 = driver.switch_to.alert
popup_title3 = popup3.text
exp_title3 = "Thanks for the message!!"
if popup_title3 == exp_title3:
    print("Text from popup is as expected")
else:
    print("Login test failed")

popup3.accept()

#Testing the close functionality on the contact page
driver.find_element(By.XPATH, "/html/body/nav/div[1]/ul/li[2]/a").click()
time.sleep(1)
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[3]/button[1]").click()
time.sleep(1)

driver.close()
