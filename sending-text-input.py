from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

url = "https://www.google.com"

browser = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

browser.get(url)

inputElem = browser.find_element(By.NAME, 'q')
inputElem.send_keys("\"deonb.me\"")
inputElem.submit()

element = WebDriverWait(browser, 10).until(ec.visibility_of_element_located((By.XPATH, '//*[@id="dimg_1"]'))).click()

element = WebDriverWait(browser, 10).until(ec.visibility_of_element_located((By.XPATH, '//*[@href="https://www.linkedin.com/in/deon-j-butler?trk=public_profile_browsemap"]'))).click()
