from lib2to3.pgen2 import driver
from multiprocessing.connection import wait
from time import sleep
from selenium import webdriver

urlue = "https://www.moneytrans.eu/france/en/login/"
username = "holahola"
password = "Holahola"
email = "maria.erazo@mail.udp.cl"
name ="hola"

driver = webdriver.Chrome("chromedriver")

# Logear en pagina chilena
driver.get(urlue)
