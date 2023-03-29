from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import secretos

#argumentos para iniciar a tela minimizada
opt = webdriver.ChromeOptions()
opt.add_argument("--headless")

driver = webdriver.Chrome(chrome_options=opt)


driver.get("https://sbe.curitiba.pr.gov.br/sbe-web/login/login.html")
driver.fullscreen_window
driver.remove_all_credentials
driver.delete_cookie
title = driver.title

fechar_comunicado = driver.find_element(by=By.XPATH, value="/html/body/div[2]/table[2]/tbody/tr/td[2]/div/div[2]/input").click()

user_login = secretos.login
user_pass = secretos.senha
pass_price = 6.00

login = driver.find_element(by=By.XPATH, value='/html/body/center/table/tbody/tr/td/center/form/div/div[2]/div[1]/ul/li[1]/span[1]/input')
login = login.send_keys(user_login)
passw = driver.find_element(by=By.XPATH, value='/html/body/center/table/tbody/tr/td/center/form/div/div[2]/div[1]/ul/li[1]/span[2]/input')
passw = passw.send_keys(user_pass)
enter = driver.find_element(by=By.XPATH, value='/html/body/center/table/tbody/tr/td/center/form/div/div[2]/div[1]/ul/li[2]/input')
enter.click()

action = driver.find_element(by=By.XPATH, value='/html/body/center/table/tbody/tr[7]/td/div/center/table[2]/tbody/tr/td[1]/div[2]/div/p[2]/a')
action.click()

#acessando cartao
action = driver.find_element(by=By.XPATH, value='/html/body/center/table/tbody/tr[7]/td/div/center/form/table/tbody/tr[1]/td[2]/input')
action.send_keys(secretos.login)
#listando cartoes
slct = Select(driver.find_element(by=By.ID, value='cartao'))
slct.first_selected_option
#proseguindo na pagina
driver.find_element(by=By.XPATH, value='/html/body/center/table/tbody/tr[7]/td/div/center/form/table/tbody/tr[4]/td/input').click()

#acessando dados no cartao (passagem comum e passagem de usuario)
card_data = driver.find_element(by=By.XPATH, value='/html/body/center/table/tbody/tr[7]/td/div/center/form/table/tbody/tr[6]/td/table/tbody/tr[1]/td[2]')
card_data2 = driver.find_element(by=By.XPATH, value='/html/body/center/table/tbody/tr[7]/td/div/center/form/table/tbody/tr[6]/td/table/tbody/tr[3]/td[2]')
user_cash = float(card_data.text.removeprefix('R$ ').removesuffix(' *').replace(',','.'))
commom_cash = float(card_data2.text.removeprefix('R$ ').removesuffix(' *').replace(',','.'))
print(commom_cash,user_cash)

print(f"Passagens disoniveis:  {(int(commom_cash/pass_price) + int(user_cash/6))}")



# time.sleep(5)