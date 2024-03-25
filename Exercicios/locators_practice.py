from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

#Instancia o webdriver para o browser que quero
browser = webdriver.Chrome()

#Digo qual é a página para abrir o site
browser.get("https://authx.globoid.globo.com/6870/login?url=https%3A%2F%2Fid.globo.com%2Fauth%2Frealms%2Fglobo.com%2Flogin-actions%2Fauthenticate%3Fsession_code%3DJ7kd-46abQLEXlhnDdEV2OdSjvklD8aP5MnV-1Dynmg%26execution%3D8feb8053-1729-44f9-bfa0-783a70e68d14%26client_id%3Dbarra%2540apps.globoid%26tab_id%3D0FSmxzr9gcU%26request-context%3Dobxkvd&error=&request-context=obxkvd")

#Para maximizar a janela
browser.maximize_window()

sleep (3) # para poder visualizar a tela do site por mais tempo, no caso 3 seg. Não é uma boa prática

#Por ID
browser.find_element(By.ID, ":r0:")




#Para imprimir no console o titulo da aba
title = browser.title
print(title)

#Para encerrar o drive
browser.quit()
