from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

#Instancia o webdriver para o browser que quero
browser = webdriver.Chrome()

#Digo qual é a página para abrir o site
browser.get("https://ecommerce-playground.lambdatest.io/index.php?route=account/login")

#Para maximizar a janela
browser.maximize_window()

sleep (3) # para poder visualizar a tela do site por mais tempo, no caso 3 seg. Não é uma boa prática

#Por ID
browser.find_element(By.ID, "input-email")

#Por nome
pwd = browser.find_element(By.NAME, "password")


#Para abrir outro site
browser.get("https://www.lambdatest.com/selenium-playground/ajax-form-submit-demo")

#Para maximizar a janela
browser.maximize_window()

sleep (3) # para poder visualizar a tela do site por mais tempo, no caso 3 seg. Não é uma boa prática

#Por nome de classe
browser.find_element(By.CLASS_NAME, "btn-dark")

#Accessing site 3
browser.get("https://www.lambdatest.com/selenium-playground/")

browser.maximize_window()

sleep(3)

#By LINK_TEXT
browser.find_element(By.LINK_TEXT, "Ajax Form Submit")

#By PARTIAL_LINK_TEXT
browser.find_element(By.PARTIAL_LINK_TEXT, "Codes")

#By TAG_NAME
browser.find_elements(By.TAG_NAME, "a")



#Para imprimir no console o titulo da aba
title = browser.title

print(title)

#Para encerrar o drive
browser.quit()