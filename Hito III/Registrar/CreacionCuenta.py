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

urleuR = "https://www.smartagrihubs.eu/register"

driver.get(urleuR)

driver.find_element_by_xpath("//*[@id=\"registration_form__firstname\"]").send_keys(name)
driver.find_element_by_xpath("//*[@id=\"registration_form__lastname\"]").send_keys(name)
driver.find_element_by_xpath("//*[@id=\"registration_form__email\"]").send_keys(email)
driver.find_element_by_xpath("//*[@id=\"registration_form__username\"]").send_keys(username)
driver.find_element_by_xpath("//*[@id=\"registration_form__password\"]").send_keys(password)

driver.find_element_by_xpath("//*[@id=\"registration_form_termsAccepted\"]").click()

driver.find_element_by_xpath("//*[@id=\"registration_form__submit\"]").click()

print("Se ha enviado un correo de verificación por favor autoricelo")