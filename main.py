from selenium import webdriver
import json

driver = webdriver.Chrome("/usr/local/bin/chromedriver")
driver.get("https://accounts.dmm.com/service/login/password/=/path=DRVESRUMTh1dDFpZWkEHGQUIWxhTVgkWAxJHSUcWUkIWTlRUCxsNXV8MXxdQVwpbAwRVXQ9KEFgWBwofZxxOBhZUAG0NRzh0TVR2SXFBJVQw")

with open("info.json") as f:
    data = json.load(f)
id = driver.find_element_by_id("login_id")
id.send_keys(data["email"])
password = driver.find_element_by_id("password")
password.send_keys(data["pass"])

login_button = driver.find_element_by_xpath('//*[@id="loginbutton_script_on"]/span/input')
login_button.click()