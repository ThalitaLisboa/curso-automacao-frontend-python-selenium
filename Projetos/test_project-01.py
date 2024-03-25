import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from time import sleep

# Para abrir o site
@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.saucedemo.com/")
    sleep(3)
    yield driver
    driver.quit()

# Para fazer login no site
def test_login(driver):  # que é o driver que vem da função de setup em cima
    username = driver.find_element(By.ID, "user-name") #identifiquei o elemento
    username.send_keys("standard_user") #para preencher o campo

    password = driver.find_element(By.ID, "password")
    password.send_keys("secret_sauce")

    button = driver.find_element(By.ID, "login-button")
    button.click()
    sleep(2)

# Para adicionar os 6 produtos diferentes no carrinho
    button = driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack")
    button.click()

    button = driver.find_element(By.ID, "add-to-cart-sauce-labs-bike-light")
    button.click()

    button = driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt")
    button.click()

    button = driver.find_element(By.ID, "add-to-cart-sauce-labs-fleece-jacket")
    button.click()

    button = driver.find_element(By.ID, "add-to-cart-sauce-labs-onesie")
    button.click()

    button = driver.find_element(By.ID, "add-to-cart-test.allthethings()-t-shirt-(red)")
    button.click()
    sleep(3)

# Conferir que no carrinho tem a badge com todos produtos
    cart_badge = driver.find_element(By.CLASS_NAME, "shopping_cart_badge")    
    # Verifica se o texto dentro do span indica que há exatamente 6 itens no carrinho
    assert cart_badge.text == "6"


# Entrar no carrinho
    cart = driver.find_element(By.XPATH, "//a[@class='shopping_cart_link']")
    cart.click()
    sleep(3)

# Remover um dos intens do carrinho
    remove_button = driver.find_element(By.XPATH, "(//button[text()='Remove'])[1]")
    remove_button.click()
    sleep(2)

# Conferir que no carrinho tem a badge com 5 produtos
    cart_badge = driver.find_element(By.CLASS_NAME, "shopping_cart_badge")    
    # Verifica se o texto dentro do span indica que há exatamente 5 itens no carrinho
    assert cart_badge.text == "5"


# Clicar no botão Checkout
    cart = driver.find_element(By.XPATH, "//a[@class='shopping_cart_link']")
    cart.click()
    checkout_button = driver.find_element(By.XPATH, "//button[text()='Checkout']")
    checkout_button.click()
    sleep(2)
    
# Preencher os dados solicitados e clicar em Continue
    first_name = driver.find_element(By.ID, "first-name")
    first_name.send_keys("Kendall")
    last_name = driver.find_element(By.ID, "last-name")
    last_name.send_keys("Roy")
    postal_code = driver.find_element(By.ID, "postal-code")
    postal_code.send_keys("20270-040")
    continue_button = driver.find_element(By.ID, "continue")
    continue_button.click()
    sleep(2)

# Clicar no botão Finish
    finish_button = driver.find_element(By.ID, 'finish')
    finish_button.click()
    sleep(2)
    
# Conferir a mensagem “Thank you for your order!”
    message = driver.find_element(By.CLASS_NAME, 'complete-header').text

    sleep(2)

    assert "Thank you for your order!" == message  # para confirmar qual a mensagem que foi informada.