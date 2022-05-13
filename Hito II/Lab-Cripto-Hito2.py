import _random
import time
from time import sleep
from tkinter import E, N, Button
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options

opts= Options()
opts.add_argument("Mozilla/5.0 (Windows NT 4.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2049.0 Safari/537.36")

Password = [""]
User = [""]
data = [""]
data.clear()
Password.clear()
User.clear()

archivo = open('Hito1Datos.txt', "r")

lines = archivo.readlines()
#print(lines)
N = 0
for i in range(len(lines)):
    #print(lines[i])
    data = lines[i].split(",")
    User.append(data[0])
    Password.append(data[1])
    N += 1

print(User,"\n")
print(Password,"\n")
archivo.close()
print(N)

driver = webdriver.Chrome('./chromedriver.exe')
x = 0

#print(User)
#print(Password)
#print(len(User))

for x in range(N):
    print("s0")
    print(x)
    driver.fullscreen_window
    driver.get('https://www.fide.cl/wp-login.php')
    #WebDriverWait(driver, 5).until(EC.presence_of_all_elements_located(By.XPATH,'//*[@id="login"]'))
    pruebaUser = driver.find_element(by=By.XPATH, value='//*[@id="user_login"]')
    print("s1")
    pruebaPass = driver.find_element(by=By.XPATH, value='//*[@id="user_pass"]')
    print("s2")
    input_buton = driver.find_element(by=By.XPATH, value='//*[@id="wp-submit"]')
    print(User[x],"\n")
    print(Password[x],"\n")
    print("s3")
    time.sleep(5)
    pruebaUser.send_keys(User[x])
    print("s4")
    time.sleep(5)
    pruebaPass.send_keys(Password[x])
    print("s5")
    #time.sleep(2)
    #input_buton.click()
    print("s6")
    
    driver.delete_all_cookies()
    #WebDriverWait(driver,1)
    #driver.save_screenshot('screenshot.png')
    