import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


serv_obj = Service("C:\webdriver3\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
driver.get("https://www.demoblaze.com/")

#testing the login flow using an account that exists on the site
driver.find_element(By.ID, "login2").click()
time.sleep(1)
driver.find_element(By.ID, "loginusername").send_keys("gburn6394@gmail.com")
time.sleep(1)
driver.find_element(By.ID, "loginpassword").send_keys("Webtesting")
time.sleep(1)
driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div[3]/button[2]").click()
time.sleep(1)
#checked for the welcome button since that is only available one you login
welcomebtn = driver.find_element(By.ID, "nameofuser")
time.sleep(1)
print(welcomebtn.is_displayed())
driver.find_element(By.ID, "logout2").click()
time.sleep(1)
signup = driver.find_element(By.ID, "signin2")
time.sleep(1)
print(signup.is_displayed())

# Clicking the login button without entering any information
driver.find_element(By.ID, "login2").click()
time.sleep(1)
driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div[3]/button[2]").click()
time.sleep(1)
# Wait for the alert to be displayed and store it in a variable
popup = driver.switch_to.alert
popup_title = popup.text
exp_title = "Please fill out Username and Password."
if popup_title == exp_title:
    print("Text from popup is as expected")
else:
    print("Login test failed")

#Inputting the incorrect username and password
popup.accept()
time.sleep(1)
driver.find_element(By.ID, "loginusername").send_keys("notanemail")
time.sleep(1)
driver.find_element(By.ID, "loginpassword").send_keys("12345678")
time.sleep(1)
driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div[3]/button[2]").click()
time.sleep(1)

#Testing that I receive a popup telling me that tells me that my username or password is incorrect
popup2 = driver.switch_to.alert
popup_title2 = popup2.text
exp_title2 = "User does not exist."
if popup_title2 == exp_title2:
    print("Text from popup is as expected")
else:
    print("Login test failed")

popup2.accept()
driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div[3]/button[1]").click()
time.sleep(1)

driver.close()
