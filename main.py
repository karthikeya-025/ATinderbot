import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_driver_path = "C:\devolopment\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get("https://tinder.com/")
driver.maximize_window()
loginbtn = driver.find_element(By.XPATH,value='//*[@id="o41285377"]/div/div[1]/div/main/div[1]/div/div/div/div/header')
login = loginbtn.find_element(By.XPATH,value='//*[@id="o41285377"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a')
login.click()
time.sleep(5)
more_options = driver.find_element(By.XPATH,value='//*[@id="o-1687095699"]/div/div/div[1]/div/div[3]/span/button')
more_options.click()
time.sleep(5)
login_with_facebook = driver.find_element(By.XPATH,value='//*[@id="o-1687095699"]/div/div/div[1]/div/div[3]/span/div[2]')
loginfb = login_with_facebook.find_element(By.XPATH,value='//*[@id="o-1687095699"]/div/div/div[1]/div/div[3]/span/div[2]/button/span[2]')
loginfb.click()
time.sleep(12)
driver.switch_to.window(driver.window_handles[1])
time.sleep(2)
email = driver.find_element(By.XPATH,value='//*[@id="email"]')
email.send_keys("use env variable")
password = driver.find_element(By.XPATH,value='//*[@id="pass"]')
password.send_keys("*******")
password.send_keys(Keys.ENTER)
driver.switch_to.window(driver.window_handles[0])
time.sleep(10)
accept = driver.find_element(By.XPATH,value='//*[@id="o-1687095699"]/div/div/div/div/div[3]/button[1]')
accept.click()
enable = driver.find_element(By.XPATH,value='//*[@id="o-1687095699"]/div/div/div/div/div[3]/button[1]')
enable.click()
accept_cookies = driver.find_element(By.XPATH,value='//*[@id="o41285377"]/div/div[2]/div/div/div[1]/button')
accept_cookies.click()
time.sleep(25)

dislike = driver.find_element(By.XPATH,value='//*[@id="Tinder"]/body')
count = 0 
while count <= 50:
    time.sleep(3)
    dislike.send_keys(Keys.ARROW_LEFT)
    print("Clicked!")
    count += 1