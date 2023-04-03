from selenium import webdriver
from selenium.webdriver.common.by import By
import time

browser = webdriver.Firefox()
browser.get("https://ava.ufms.br/login/index.php")

with open(r'C:\Users\felip\PycharmProjects\loginAVA\login.txt', encoding='utf-8') as login:
    arquivo = login.read()
    info = arquivo.split('\n')
    print(info)

time.sleep(5)

username = browser.find_element(By.ID, "username")
password = browser.find_element(By.ID, "password")

username.send_keys(info[0])
password.send_keys(info[1])

login_attempt = browser.find_element(By.XPATH, "//*[@type='submit']")

login_attempt.submit()
