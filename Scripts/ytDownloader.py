import os
try:
	from selenium import webdriver
	import time
except ImportError:
	os.system('python -m pip install selenium')
	from selenium import webdriver
	import time
# options = webdriver.ChromeOptions()
# options.add_argument('--ignore-certificate-errors')
# options.add_argument("--test-type")
# options.binary_location = "/usr/bin/chromium"
driver = webdriver.Chrome("C:\\Users\\Abhishek\\Downloads\\BhromorDowload\\chromedriver_win32")
driver.get('http://abhi-laksh.000webhostapp.com/')

elem = driver.find_element_by_id("searchToggler")
# click radio button
python_button.click()

# # type text
# text_area = driver.find_element_by_id('textarea')
# text_area.send_keys("print('Hello World')")

# # click submit button
# submit_button = driver.find_elements_by_xpath('//*[@id="editor"]/table/tbody/tr[3]/td/table/tbody/tr/td/div/table/tbody/tr/td[3]/input')[0]
# submit_button.click()