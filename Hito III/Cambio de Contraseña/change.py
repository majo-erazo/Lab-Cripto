from lib2to3.pgen2 import driver
from multiprocessing.connection import wait
from time import sleep
from selenium import webdriver

urlue = "https://www.smartagrihubs.eu/login"
username = "holahola"
password = "Holahola"
email = "maria.erazo@mail.udp.cl"
name ="hola"
newpassword = "HOLAhola"

driver = webdriver.Chrome("chromedriver")

driver.get(urlue)

driver.find_element_by_xpath("//*[@id=\"_username\"]").send_keys(username)
driver.find_element_by_xpath("//*[@id=\"_password\"]").send_keys(password)

driver.find_element_by_xpath("//*[@id=\"_submit\"]").click()

driver.get("https://www.smartagrihubs.eu/portal/settings/profile")

driver.find_element_by_xpath("//*[@id=\"password\"]/div[1]/label/input").send_keys(password) #aqui va la contraseña actual
driver.find_element_by_xpath("//*[@id=\"password\"]/div[2]/label/input").send_keys(newpassword) #contraseña nueva
driver.find_element_by_xpath("//*[@id=\"password\"]/div[3]/label/input").send_keys(newpassword) #repetir contraseña nueva

driver.find_element_by_xpath("//*[@id=\"content\"]/section/div/div/div/div/div/div[3]/form[1]/div/div[5]/input").click()