import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


serv_obj = Service("C:\webdriver3\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
driver.get("https://www.demoblaze.com/")

def click_signin():
    driver.find_element(By.ID, "signin2").click()
    time.sleep(1)

def clear_boxes():
    driver.find_element(By.ID, "sign-username").clear()
    time.sleep(1)
    driver.find_element(By.ID, "sign-password").clear()
    time.sleep(1)

#testing out sign up features
#the first test will be using an email that already is associated with an account on the site
click_signin()
driver.find_element(By.ID, "sign-username").send_keys("gburn6494@gmail.com")
time.sleep(1)
driver.find_element(By.ID, "sign-password").send_keys("AnotherTest")
time.sleep(1)
driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div[3]/button[2]").click()
time.sleep(3)

#Testing the popup that will appear and will display the correct message
popup4 = driver.switch_to.alert
popup_title4 = popup4.text
exp_title4 = "This user already exists."
if popup_title4 == exp_title4:
    print("Text from popup is as expected")
else:
    print("Login test failed")

popup4.accept()
time.sleep(3)

# Now I will test what happens when I press sign up without having filled in the username
# or password boxes
driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div[3]/button[1]").click()
time.sleep(2)
click_signin()
clear_boxes()


driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div[3]/button[2]").click()
time.sleep(1)

popup5 = driver.switch_to.alert
popup_title5 = popup5.text
exp_title5 = "Please fill out Username and Password."
if popup_title5 == exp_title5:
    print("Text from popup is as expected")
else:
    print("Login test failed")

popup5.accept()
time.sleep(1)

#Now I will try testing the desired flow
driver.find_element(By.ID, "sign-username").send_keys("GavinPythonTest")
time.sleep(1)
driver.find_element(By.ID, "sign-password").send_keys("PythonTests")
time.sleep(1)
driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div[3]/button[2]").click()
time.sleep(3)

popup6 = driver.switch_to.alert
popup_title6 = popup5.text
exp_title6 = "Sign up successful."
if popup_title6 == exp_title6:
    print("Text from popup is as expected")
else:
    print("Login test failed")

popup6.accept()
time.sleep(1)

#After creating the account, I will now sign in using the credentials
driver.find_element(By.ID, "login2").click()
time.sleep(1)
driver.find_element(By.ID, "loginusername").send_keys("GavinPythonTest")
time.sleep(1)
driver.find_element(By.ID, "loginpassword").send_keys("PythonTests")
time.sleep(1)
driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div[3]/button[2]").click()
time.sleep(2)


driver.close()