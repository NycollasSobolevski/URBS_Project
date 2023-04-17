from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

import DB as db
def init():
    # Abrindo o txt, se caso ele nao existir iremos criar um
    # try:
    #     txt = open("data/Linhas_de_Onibus.txt", "w")
    # except:
    #     txt = open("data/Linhas_de_Onibus.txt", "x")
    #     txt = open("data/Linhas_de_Onibus.txt","w")

    #config do webdriver
    Coptions = webdriver.ChromeOptions()
    Coptions.add_argument("--headless")
    driver = webdriver.Chrome()

    url = 'https://www.urbs.curitiba.pr.gov.br/horario-de-onibus'
    driver.get(url)
    driver.remove_all_credentials
    driver.delete_all_cookies

    # Selecionando 'select' existente na pagina na qual contem a lista de linhas (de onibus) disponiveis
    selectLinha = '/html/body/div[3]/div/div[2]/div[1]/div/div/div[1]/select[1]'
    select = Select(driver.find_element(by=By.XPATH, value=selectLinha)).options
    
    #Escrevendo todas as linhas disponiveis no site da URBS em um .txt
    # for i in select:
    #     txt.write(i.text + "\n")
    # txt.close
    
    # Adicionando em uma lista para retornar
    result = []
    for i in select:
        result.append(i.text)
    return result

linhasOnibus = []
linhasFunc = init()
#tratando a lista
for i in range(len(linhasFunc)):
    linha = linhasFunc[i].split("[")
    linhasOnibus.append(linha)
for i in range(len(linhasOnibus)):
    linhasOnibus[i][1] = linhasOnibus[i][1].replace(']','')

# #Adicionando no Database
# for i in linhasOnibus:
#     print(i[1] + " - " + i[0])
#     db.insert('linhas',f"'{str(i[1])}','{str(i[0])}'")


