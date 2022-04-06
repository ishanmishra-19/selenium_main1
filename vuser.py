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
# selecting the pim module
driver.find_element(By.ID,"menu_pim_viewPimModule").click()
time.sleep(2)
driver.find_element(By.ID,"menu_pim_viewEmployeeList").click()
time.sleep(5)
# Searching
search = driver.find_element(by=By.ID, value='employee_name_quick_filter_employee_list_value')
search.clear()
search.send_keys("ishan mishra")
time.sleep(15)
driver.find_element(by=By.XPATH, value='//*[@id="employeeListTable"]/tbody/tr/td[3]').click()