import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from time import sleep

@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://paulocoliveira.github.io/mypages/jobapplication.html")
    sleep(3)
    yield driver
    driver.quit()

def test_happy_path(driver):  # que é o driver que vem da função de setup em cima
    full_name = driver.find_element(By.ID, "fullName") #identifiquei o elemento
    full_name.send_keys("Kendall Roy") #para preencher o campo

    email = driver.find_element(By.ID, "email")
    email.send_keys("succession@gmail.com")

    phone_number = driver.find_element(By.ID, "phoneNumber")
    phone_number.send_keys("123456789")

    Select(driver.find_element(By.ID, "desiredPosition")).select_by_visible_text("Manager")

    remote = driver.find_element(By.ID, "location1") #se quisesse, poderia colocar o location2 que é a outra opção que aparece. 
    remote.click()

    years = driver.find_element(By.ID, "experienceYears")
    years.send_keys("17")

    html = driver.find_element(By.ID, "skill1")
    html.click()

    js = driver.find_element(By.ID, "skill3")
    js.click()

    button = driver.find_element(By.CSS_SELECTOR, "button")
    button.click()

    message = driver.find_element(By.ID, "successMessage").text

    sleep(1)

    assert "Submission successful!" == message  # para confirmar qual a mensagem que foi informada.

    sleep(1)

def test_only_name(driver):  #para fazer só o nome
    full_name = driver.find_element(By.ID, "fullName")
    full_name.send_keys("Kendall Roy")

    button = driver.find_element(By.CSS_SELECTOR, "button")
    button.click()

    message = driver.find_element(By.ID, "successMessage").text

    sleep(1)

    assert "Submission successful!" == message

    sleep(1)

def test_without_filling(driver):  #sem preencher o formulário
    button = driver.find_element(By.CSS_SELECTOR, "button")
    button.click()

    message = driver.find_element(By.ID, "successMessage").text

    sleep(1)

    assert "Submission successful!" == message

    sleep(1)

