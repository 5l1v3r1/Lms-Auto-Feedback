from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome()
driver.get("https://karnatakalms.com/home")

input=driver.find_element_by_xpath('//*[@id="homebody"]/div[2]/div/button[2]').click()

input=driver.find_element_by_xpath('//*[@id="userid"]')
input.send_keys('ug1919191') #enter your valid user-id

input=driver.find_element_by_xpath('//*[@id="password"]')
input.send_keys('msdhoni') #enter your valid password

time.sleep(2)

dropdown = Select(driver.find_element_by_name("OrgCodeDrop"))
dropdown.select_by_value("TU") #I enter tumkur university value select your university value

#Bangalore University-"BUB"
#Bengaluru City University-"BCU"
#Bengaluru North University-"BNU"
#Davanagere University-"DU"
#Gulbarga University-"GU"
#Government Engineering Colleges-"GEC"
#Government Polytechnics-"GP"
#Kuvempu University-"KU"
#Karnataka University-"KUD"
#Karnataka State Women University-"KSAWU"
#Mangalore University-"MU"
#Rani Chennamma University-"RCU"
#University of Mysore-"UOM"
#Vijayanagara Shri Krishnadevaraya University-"VSKU"
#All University-"TLSMASTER"
#Test University-"ENTMob"
#New Test University-"KNTU"

input=driver.find_element_by_xpath('/html/body/app-root/app-layout-full/div[1]/main/div/app-login/div/div/div/div/div[2]/div/div[1]/form/div[4]/div/button').click()
time.sleep(9)

input=driver.find_element_by_xpath('/html/body/app-root/app-layout-full/header/button/div').click()
time.sleep(3)

input=driver.find_element_by_xpath('//*[@id="asidemenu"]/ul/li[3]/a/span/b').click()
time.sleep(2)

input=driver.find_element_by_xpath('/html/body/app-root/app-layout-full/div[1]/main/div/app-graviances/div[2]/div/div/form/div[1]/button').click()
time.sleep(2)

dropdown = Select(driver.find_element_by_id("inputType"))
dropdown.select_by_value("FeedBack")

input=driver.find_element_by_xpath('/html/body/app-root/app-layout-full/div[1]/main/div/app-graviances/div[3]/div/div/div[2]/app-graviances-editor/form/div/div[2]/div/div/textarea')
input.send_keys('One of the best student friendly website the study materials was awesome') #change your needed line for feedback

input=driver.find_element_by_xpath('/html/body/app-root/app-layout-full/div[1]/main/div/app-graviances/div[3]/div/div/div[2]/app-graviances-editor/div/div/button[1]').click()

time.sleep(5)

driver.close()


