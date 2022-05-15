from lib2to3.pgen2 import driver
from multiprocessing.connection import wait
from time import sleep
from selenium import webdriver

urlue = "https://www.smartagrihubs.eu/forgot-password"
username = "holahola"
password = "Holahola"
email = "maria.erazo@mail.udp.cl"
name ="hola"

driver = webdriver.Chrome("chromedriver")

driver.get(urlue)

driver.find_element_by_xpath("//*[@id=\"_email\"]").send_keys(email)

driver.find_element_by_xpath("//*[@id=\"_submit\"]").click()

print("Revisa el correo se ha enviado una nueva contraseña a él")

