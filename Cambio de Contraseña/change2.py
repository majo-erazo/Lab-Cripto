from lib2to3.pgen2 import driver
from multiprocessing.connection import wait
from time import sleep
from selenium import webdriver

urlch = "https://www.psicoperspectivas.cl/index.php/psicoperspectivas/user/changePassword"
username = "holahola"
password = "Holahola"
newpassword = "nuevoHolahola"
email = "maria.erazo@mail.udp.cl"
name ="hola"

driver = webdriver.Chrome("chromedriver")

driver.find_element_by_xpath("//*[@id=\"oldPassword\"]").send_keys(password)
driver.find_element_by_xpath("//*[@id=\"password\"]").send_keys(newpassword)
driver.find_element_by_xpath("//*[@id=\"password2\"]").send_keys(newpassword)

driver.find_element_by_xpath("//*[@id=\"content\"]/form/p[2]/input[1]").click()
