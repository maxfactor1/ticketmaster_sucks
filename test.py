from selenium import webdriver 
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.common.exceptions import TimeoutException
import filecmp

option = webdriver.ChromeOptions()
#option.add_argument(" - incognito")
option.add_argument('headless')

#print(option)
browser = webdriver.Chrome(executable_path='/Users/mbuehl01/Downloads/chromedriver', chrome_options=option)

browser.get("http://settlement.livenation.com/")

# Wait 20 seconds for page to load
timeout = 10
try:
    WebDriverWait(browser, timeout).until(EC.visibility_of_element_located((By.XPATH, "//*[starts-with(@class, 'LNFooter-')]")))
except TimeoutException:
    print("Timed out waiting for page to load")
    browser.quit()
    quit()

events_element = browser.find_elements_by_xpath("//*[starts-with(@class, 'eventsSection-')]")

events = [x.text for x in events_element]
f1=open("/tmp/before", "rw")
f2=open("/tmp/after", "rw")

for event in events:
	print event.encode('utf-8').strip()

before=f1.read()
after=f2.read()

#if before != after:
#	for event.encode('utf-8').strip() in events:
#	        f1.write("%s\n" % event)

f1.close()
f2.close()    

browser.quit()
