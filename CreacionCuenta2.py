from lib2to3.pgen2 import driver
from multiprocessing.connection import wait
from time import sleep
from selenium import webdriver

urlch = "https://www.psicoperspectivas.cl/index.php/psicoperspectivas/login"
urleu = "https://www.moneytrans.eu/france/en/login/"
username = "Holahola"
password = "Holahola"
email = "maria.erazo@mail.udp.cl"
name ="hola"

driver = webdriver.Chrome("chromedriver")



#Crear una Cuenta en pagina chilena
#driver.get("https://www.psicoperspectivas.cl/index.php/psicoperspectivas/user/register?source=%2Findex.php%2Fpsicoperspectivas%2Fuser")
#sleep(2)

#driver.find_element_by_name("username").send_keys(username)
#driver.find_element_by_name("password").send_keys(password)
#driver.find_element_by_name("password2").send_keys(password)

#sleep(20)
#Capcha
#print("Escriba manualmente el capcha")

#driver.find_element_by_name("firstName").send_keys(name)
#driver.find_element_by_name("lastName").send_keys(name)
#driver.find_element_by_name("email").send_keys(email)

#driver.find_element_by_css_selector("input[type=\"submit\" i]").click()




# Logear en pagina chilena
driver.get(urlch)

driver.find_element_by_name("username").send_keys(username)
driver.find_element_by_name("password").send_keys(password)

driver.find_elements_by_class_name("button").click()

print("logeado correctamente")