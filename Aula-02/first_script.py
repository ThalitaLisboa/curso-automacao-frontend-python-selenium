from selenium import webdriver
from time import sleep

#Instancia o webdriver para o browser que quero
browser = webdriver.Chrome()

#Digo qual é a página para abrir o site
browser.get("https://www.uol.com.br")

#Para maximizar a janela
browser.maximize_window()

sleep (5) # para poder visualizar a tela do site por mais tempo, no caso 5seg. Não é uma boa prática

#Para imprimir no console o titulo da aba
title = browser.title

print(title)

#Para encerrar o drive
browser.quit()