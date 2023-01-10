from selenium import webdriver

from selenium.webdriver.common.keys import Keys

import time

from selenium.webdriver.chrome.service import Service

chrome_executable = Service(executable_path='D:\python-selenium\chromedriver.exe', log_path='NUL')
driver = webdriver.Chrome(service=chrome_executable)


driver.get('https://dx.doi.org/')


driver.maximize_window()

time.sleep(200)