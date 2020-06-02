from selenium import webdriver
import json
import time

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
time.sleep(8)
teachers = driver.find_elements_by_class_name("owl-item")
lis = []
for i in range(len(teachers)):
    tmp = '//*[@id="slider02"]/div/div/div['+str(i+1)+']/div'
    test = driver.find_element_by_xpath(tmp)
    test2 = test.find_elements_by_xpath('a')[0] 
    if len(test2.find_elements_by_id("total")) > 0:
        test3 = test2.find_element_by_id("total") 
        star = test3.get_attribute("textContent")[1:-2]
        lis.append(int(star))
    else:
        lis.append(0)
maxIdx = lis.index(max(lis))+1
maxIdxstr = '//*[@id="slider02"]/div/div/div['+str(maxIdx)+']/div'
teacher_page = driver.find_element_by_xpath(maxIdxstr)
teacher_button = teacher_page.find_elements_by_xpath('a')[1]
teacher_button.click()
time.sleep(5)
reservation_button = driver.find_element_by_xpath('//*[@id="submitBox"]/button')
reservation_button.click()