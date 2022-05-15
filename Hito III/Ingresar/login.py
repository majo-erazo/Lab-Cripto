from lib2to3.pgen2 import driver
from multiprocessing.connection import wait
from time import sleep
from selenium import webdriver

urlue = "https://www.smartagrihubs.eu/login"
username = "holahola"
password = "Holahola"
email = "maria.erazo@mail.udp.cl"
name ="hola"

driver = webdriver.Chrome("chromedriver")

# Logear en pagina chilena
driver.get(urlue)

driver.find_element_by_xpath("//*[@id=\"_username\"]").send_keys(username)
driver.find_element_by_xpath("//*[@id=\"_password\"]").send_keys(password)

driver.find_element_by_xpath("//*[@id=\"_submit\"]").click()
