import time


from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome("C:\\Users\\ishamishra\\Downloads\\chromedriver_win32\\chromedriver.exe")

driver.get("https://ishanmishra-trials7401.orangehrmlive.com/")
driver.maximize_window()
time.sleep(5)


Username = driver.find_element(By.ID,"txtUsername").send_keys("Admin")
time.sleep(3)


Password = driver.find_element(By.ID,"txtPassword").send_keys("An@T3UAh0f")
time.sleep(3)

Login = driver.find_element_by_xpath('//*[@id="divLogin"]/div[2]/div/form/div[3]/button').click()
time.sleep(10)
# driver.minimize_window()

# driver.maximize_window()

homepage = driver.find_element(By.ID,"user-dropdown").click()
time.sleep(5)
driver.find_element(By.ID,"aboutDisplayLink").click()
time.sleep(20)
driver.find_element(By.ID,"heartbeatSubmitBtn").click()
driver.close()




