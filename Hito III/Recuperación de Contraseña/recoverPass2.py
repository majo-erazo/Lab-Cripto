
from lib2to3.pgen2 import driver
from multiprocessing.connection import wait
from time import sleep
from selenium import webdriver

urlch = "https://www.psicoperspectivas.cl/index.php/psicoperspectivas/login/lostPassword"
username = "holahola"
password = "Holahola"
newpassword = "nuevoHolahola"
email = "maria.erazo@mail.udp.cl"
name ="hola"

driver = webdriver.Chrome("chromedriver")
driver.get(urlch)

driver.find_element_by_xpath("//*[@id=\"content\"]/form/table/tbody/tr/td[2]/input").send_keys(email)

driver.find_element_by_xpath("//*[@id=\"content\"]/form/p[2]/input").click()
print("Revisa el correo se ha enviado una nueva contraseña a él")