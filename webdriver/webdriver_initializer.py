import os

from selenium import webdriver
from selenium.webdriver import Chrome


options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.page_load_strategy = 'none'
options.binary_location = os.getcwd() + '/webdrivers/chromedriver.exe'

driver = Chrome(options=options)

with open('webdriver/webdriver_config.py', 'w+') as f:
    f.write(f'''driver_url = '{driver.command_executor._url}'
driver_session_id = '{driver.session_id}'
''')

driver.command_executor.keep_alive = True

print(driver.command_executor._url + '\n')

while input() != 'stop':
    pass

print('Webdriver interrupted')
