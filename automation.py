from selenium import webdriver 
chrome = webdriver.Chrome('./chromedriver')
#usr/local/bon () global 
chrome.maximize_window()
chrome.get("https://www.seleniumeasy.com/test/input-form-demo.html")
assert("selenium easy demo" in chrome.title)
btn = chrome.find_element_by_class_name('btn-default')
print(get_attribute("innerhtml")) # $0 -> btn-

assert 'Show Message' in chrome.page_source

#putting our own input in single field input
chrome.find_element_by_id("user-meesage")
user_msg.clear()
user_msg.send_keys("COOL")

btn.click()

#getting text in that singlw field input
output_msg = chrome.find_element_by_id("display")
assert"COOL" in output_msg.text

chrome.find_element_by_css_selector('#get-id > .btn')

chrome.close() #quit()