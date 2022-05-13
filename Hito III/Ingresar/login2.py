from lib2to3.pgen2 import driver
from multiprocessing.connection import wait
from time import sleep
from selenium import webdriver

urlch = "https://www.psicoperspectivas.cl/index.php/psicoperspectivas/login"
username = "holahola"
password = "Holahola"
email = "maria.erazo@mail.udp.cl"
name ="hola"

driver = webdriver.Chrome("chromedriver")

# Logear en pagina chilena
driver.get(urlch)

driver.find_element_by_name("username").send_keys(username)
driver.find_element_by_name("password").send_keys(password)

driver.find_element_by_xpath("//*[@id=\"content\"]/form/table/tbody/tr[4]/td[2]/input").click()

print("logeado correctamente")