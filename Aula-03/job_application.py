from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from time import sleep

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://paulocoliveira.github.io/mypages/jobapplication.html")

sleep(3)

#identifiquei o elemento
full_name = driver.find_element(By.ID, "fullName")
#para preencher o campo
full_name.send_keys("Thalita Lisboa")

email = driver.find_element(By.ID, "email")
email.send_keys("teste@gmail.com")

phone_number = driver.find_element(By.ID, "phoneNumber")
phone_number.send_keys("123456789")

Select(driver.find_element(By.ID, "desiredPosition")).select_by_visible_text("Manager")

remote = driver.find_element(By.ID, "location1")  #se quisesse, poderia colocar o location2 que é a outra opção que aparece. 
remote.click()

years = driver.find_element(By.ID, "experienceYears")
years.send_keys("13")

skill1 = driver.find_element(By.ID, "skill1")
skill1.click()

skill3 = driver.find_element(By.ID, "skill3")
skill3.click()

button = driver.find_element(By.CSS_SELECTOR, "button")
button.click()

message = driver.find_element(By.ID, "successMessage").text

sleep(1)

assert "Submission successful!" in message # para confirmar qual a mensagem que foi informada. 

sleep(3)
driver.quit()
