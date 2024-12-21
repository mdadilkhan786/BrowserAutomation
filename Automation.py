from selenium import webdriver
from time import sleep 
driver = webdriver.Chrome()
driver.get("https://facebook.com")
sleep(500)
email= driver.find_element("id","email")
password = driver.find_element("id","pass")
email.send_keys(" ")
sleep(500)
password.send_keys(" ")
button = driver.find_element("name","login")
sleep(500000)
button.click()
sleep(10)



