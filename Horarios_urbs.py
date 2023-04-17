from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


def init():
    try:
        txt = open("data/Linhas_de_Onibus.txt", "w")
    except:
        txt = open("data/Linhas_de_Onibus.txt", "x")
        txt = open("data/Linhas_de_Onibus.txt","w")
    Coptions = webdriver.ChromeOptions()
    Coptions.add_argument("--headless")
    driver = webdriver.Chrome()

    url = 'https://www.urbs.curitiba.pr.gov.br/horario-de-onibus'
    driver.get(url)
    driver.remove_all_credentials
    driver.delete_all_cookies

    selectLinha = '/html/body/div[3]/div/div[2]/div[1]/div/div/div[1]/select[1]'
    select = Select(driver.find_element(by=By.XPATH, value=selectLinha)).options
    # for i in select:
    #     print(i.text)
    #     txt.write(i.text + "\n")
    # txt.close


init()