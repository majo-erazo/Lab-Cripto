from lib2to3.pgen2 import driver
from selenium import webdriver

driver = webdriver.Chrome("chromedriver")

email = "maria.erazo@mail.udp.cl"
username = "Holahola"
password = "Holahola"
email = "maria.erazo@mail.udp.cl"
name ="hola"

#Crear una cuenta en pagina EU
#driver.get(urleu)

urleuR = "https://www.moneytrans.eu/france/en/register/"

driver.get(urleuR)

driver.find_element_by_name("email").send_keys(email)
driver.find_element_by_name("confirmEmail").send_keys(email)

driver.find_element_by_id("wt-cli-accept-btn").click()
driver.find_element_by_id("emailRegistrationButton").click()

driver.find_elements_by_xpath("/html/")