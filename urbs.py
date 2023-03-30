from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import secretos


#argumentos para iniciar a tela minimizada
def search_user(id):
    users = secretos.users
    user =''
    for i in users:
        if i[0] == id:
            user = i
    return user

def init(user):
    
    opt = webdriver.ChromeOptions()
    opt.add_argument("--headless")
    driver = webdriver.Chrome(chrome_options=opt)

    driver.get("https://sbe.curitiba.pr.gov.br/sbe-web/login/login.html")
    driver.fullscreen_window
    driver.remove_all_credentials
    driver.delete_cookie
    try:
        driver.find_element(by=By.XPATH, value="/html/body/div[2]/table[2]/tbody/tr/td[2]/div/div[2]/input").click()
    except:
        print('no comunicate')
    user = search_user(user)
    user_login = user[0]
    user_pass = user[1]

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
    return driver


def saldo(user):
    driver = init(user)
    #preco da passagem
    pass_price = 6.00
    #acessando dados no cartao (passagem comum e passagem de usuario)
    card_data = driver.find_element(by=By.XPATH, value='/html/body/center/table/tbody/tr[7]/td/div/center/form/table/tbody/tr[6]/td/table/tbody/tr[1]/td[2]')
    card_data2 = driver.find_element(by=By.XPATH, value='/html/body/center/table/tbody/tr[7]/td/div/center/form/table/tbody/tr[6]/td/table/tbody/tr[3]/td[2]')
    user_cash = float(card_data.text.removeprefix('R$ ').removesuffix(' *').replace(',','.'))
    commom_cash = float(card_data2.text.removeprefix('R$ ').removesuffix(' *').replace(',','.'))
    # print(commom_cash,user_cash)
    qtd_passagens = (int(commom_cash/pass_price) + int(user_cash/6))
    name = driver.find_element(by=By.XPATH, value='/html/body/center/table/tbody/tr[7]/td/div/center/form/table/tbody/tr[1]/td[2]').text
    return user_cash,commom_cash,qtd_passagens, name

def historico(user):
    driver = init(user)
    table = driver.find_elements(by=By.CLASS_NAME, value='reportResultNew')
    while len(table) <= 0:
        table = driver.find_elements(by=By.CLASS_NAME, value='reportResultNew')
        print('searching')
        time.sleep(0.5)

    table = table[0].find_element(by=By.TAG_NAME, value='tbody').text
    table = table.split('\n')

    name = driver.find_element(by=By.XPATH, value='/html/body/center/table/tbody/tr[7]/td/div/center/form/table/tbody/tr[1]/td[2]').text

    for i in range(len(table)):
        table[i] = table[i].replace(' -','').split(' ')
    # for i in table:
    #     print(i)
    return table, name
    


#MAIN
# init('13303655936')
# print(saldo('13303655936'))
# print(historico('11370672926'))