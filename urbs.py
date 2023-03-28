from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()


driver.get("https://sbe.curitiba.pr.gov.br/sbe-web/login/login.html")
driver.fullscreen_window
driver.remove_all_credentials
driver.delete_cookie
title = driver.title

fechar_comunicado = driver.find_element(by=By.XPATH, value="/html/body/div[2]/table[2]/tbody/tr/td[2]/div/div[2]/input").click()

user_login = ''
user_pass = ''

login = driver.find_element(by=By.XPATH, value='//*[@id="nomeUsuario"]')
login = login.send_keys(user_login)
passw = driver.find_element(by=By.XPATH, value='')
passw = passw.send_keys(user_pass)
