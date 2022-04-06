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
# selecting the Add employee Function
driver.find_element(By.XPATH,'//*[@id="menu_pim_addEmployee"]/span[2]').click()
time.sleep(55)

# enetering the First Name
driver.find_element(By.CSS_SELECTOR,"#first-name-box").send_keys("Ishan")
time.sleep(2)
# Entering the Last Name
driver.find_element(By.XPATH,'//*[@id="last-name-box"]').send_keys("Mishra")
time.sleep(5)
#Select the country
driver.find_element(By.XPATH,'//*[@id="modal-holder"]/div/div/div/div[2]/form/oxd-decorator/div/div[2]/div/div[2]/div/div[2]/div/div[1]/button/div/div/div').click()
driver.find_element(By.XPATH,'//*[@id="bs-select-1-7"]/span').click()
time.sleep(3)
driver.find_element(By.ID,"modal-save-button").click()
time.sleep(50)
driver.find_element(By.XPATH,'//*[@id="pimPersonalDetailsForm"]/materializecss-decorator[3]/div/sf-decorator[1]/div/span[1]/span[1]/i').click()
time.sleep(10)
driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div[2]/section/div[2]/ui-view/div[2]/div/form/materializecss-decorator[3]/div/sf-decorator[1]/div/span[1]/span[1]/div/div/div/div/div/div[3]/button[1]').click()
time.sleep(3)
#driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
#time.sleep(2)
driver.find_element(By.XPATH,'//*[@id="wizard-nav-button-section"]/button[2]').click()
time.sleep(30)
driver.find_element(By.XPATH,'//*[@id="employement_details_tab"]/form/div/oxd-decorator[1]/div/div[10]/div/div[1]/button').click()
time.sleep(10)
driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div[2]/section/div[2]/ui-view/div[2]/div/form/div/oxd-decorator[1]/div/div[10]/div/div[1]/div/div/ul/li[3]/a').click()
time.sleep(5)
driver.find_element(By.XPATH,'//*[@id="employement_details_tab"]/custom-fields-panel/div/form/oxd-decorator[1]/div/div[1]/div/div[1]/button').click()
driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div[2]/section/div[2]/ui-view/div[2]/div/custom-fields-panel/div/form/oxd-decorator[1]/div/div[1]/div/div[1]/div/div/ul/li[3]/a/span').click()
driver.find_element(By.XPATH,'//*[@id="employement_details_tab"]/custom-fields-panel/div/form/oxd-decorator[1]/div/div[2]/div/div[1]/button').click()
driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div[2]/section/div[2]/ui-view/div[2]/div/custom-fields-panel/div/form/oxd-decorator[1]/div/div[2]/div/div[1]/div/div/ul/li[3]/a').click()
driver.find_element(By.XPATH,'//*[@id="employement_details_tab"]/custom-fields-panel/div/form/oxd-decorator[1]/div/div[3]/div/div[1]/button').click()
driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div[2]/section/div[2]/ui-view/div[2]/div/custom-fields-panel/div/form/oxd-decorator[1]/div/div[3]/div/div[1]/div/div/ul/li[3]/a/span').click()
time.sleep(5)
driver.find_element(By.XPATH,'//*[@id="wizard-nav-button-section"]/button[3]').click()
time.sleep(10)







