from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
driverLocation = '/Users/himanshu/Coding Stuff/PYcharm file/chituuudemo/driver/chromedriver' #if windows
driver = webdriver.Chrome(driverLocation)
driver.get('http://arithmetic.zetamac.com/game?key=a7220a92')
element = driver.find_element_by_id('game')
print(element)
