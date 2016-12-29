from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from tkinter import filedialog
from tkinter import Tk
from time import sleep    


driver = webdriver.Firefox()
counter = 1
driver.get("https://www.google.com/?gws_rd=ssl")
driver.execute_script("window.open('');")
driver.switch_to_window(driver.window_handles[counter])
counter+=1
driver.get("https://www.google.com/?gws_rd=ssl")