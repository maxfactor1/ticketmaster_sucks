from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

option = webdriver.ChromeOptions()
option.add_argument(" - incognito")

browser = webdriver.Chrome(executable_path='/Users/mbuehl01/Downloads/chromedriver', chrome_options=option)

browser.get("http://settlement.livenation.com/")

# Wait 3 seconds for page to load
timeout = 3
try:
    WebDriverWait(browser, timeout).until(EC.visibility_of_element_located((By.XPATH, "//img[@class='howTo-9b7f69e4528bc57d25cb1f7ee1996124']")))
except TimeoutException:
    print("Timed out waiting for page to load")
    browser.quit()

# find_elements_by_xpath returns an array of selenium objects.
# events_element = browser.find_elements_by_xpath("//[@class='eventsSection-be329ef68095bbb58c8729d2b4abf0a6']")
events_element = browser.find_elements_by_xpath("//[starts-with(@class, 'eventsSection-'])")

# use list comprehension to get the actual repo titles and not the selenium objects.
events = [x.text for x in events_element]
# print out all the titles.
print('events:')
print(events, '\n')

browser.quit()
