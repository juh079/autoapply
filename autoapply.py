from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.action_chains import ActionChains
from tkinter import filedialog
from tkinter import Tk



#driver.get("https://boards.greenhouse.io/aerofs/jobs/74273#.WGQdm7YrK1t")
Tk().withdraw()
websitesFile = filedialog.askopenfile(mode='r')
driver = webdriver.Chrome()
counter = 1
for site in websitesFile:
	driver.get(site)
	try:
		driver.find_element_by_id("first_name").send_keys("Justin")
	except NoSuchElementException:
		print("1")
	try:
		driver.find_element_by_id("last_name").send_keys("Huynh")
	except NoSuchElementException:
		print("2")
	try:
		driver.find_element_by_id("email").send_keys("juh079@ucsd.edu")
	except NoSuchElementException:
		print("3")
	try:
		driver.find_element_by_id("phone").send_keys("4088597044")
	except NoSuchElementException:
		print("4")
	try:
		driver.find_element_by_name("resume").send_keys("/Users/JHuynh/Desktop/autoapply/test.pdf")
	except NoSuchElementException:
		print("5")
	#try:
	driver.execute_script("window.open('');")
	driver.switch_to_window(driver.window_handles[counter])
	counter+=1
	#except WebDriverException:
	#	print("5645646465456")
#alternate ways to open new tabs, but these won't work with firefox driver
#	driver.find_element_by_tag_name('body').send_keys(Keys.COMMAND + 't') 
#	actions = ActionChains(driver)
#	actions.key_down(Keys.COMMAND)
#	actions.key_down('t')
#	actions.key_up(Keys.COMMAND)
#	actions.key_up('t')
#	actions.perform()