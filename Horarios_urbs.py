from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import DB as db

def init():
    # Abrindo o txt, se caso ele nao existir iremos criar um
    # try:
    #     txt = open("data/Linhas_de_Onibus.txt", "w")
    # except:
    #     txt = open("data/Linhas_de_Onibus.txt", "x")
    #     txt = open("data/Linhas_de_Onibus.txt","w")

    #config do webdriver

    driver = webdriver.Chrome()     #abrindo navegador 
    driver.minimize_window()        # minimizando janela

    url = 'https://www.urbs.curitiba.pr.gov.br/horario-de-onibus'
    driver.get(url)
    driver.remove_all_credentials
    driver.delete_all_cookies
    return driver

def SearchLinhas():
    driver = init()
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
    
    linhasOnibus = []
    #tratando a lista
    for i in range(len(result)):
        linha = result[i].split("[")
        linhasOnibus.append(linha)
    for i in range(len(linhasOnibus)):
        linhasOnibus[i][1] = linhasOnibus[i][1].replace(']','')
    return linhasOnibus

#Funcao que procura os horarios de determinado onibus 'value' é o codigo da linha do mesmo
def timeSearch(value, driver):
    # Localizando o select da pagina  que responde a linha de onibus e selecionando a linha escolhida
    slct = Select(driver.find_element(by=By.ID, value='compHritLinha')).select_by_value(str(value))
    # localizando o select que responde ao tipo de dia e selecionando o tipo 'TODOS'
    Select(driver.find_element(by=By.ID, value='compHritDia')).select_by_visible_text("TODOS")
    # enviando os dados do select 
    driver.find_element(by=By.XPATH,value='/html/body/div[3]/div/div[2]/div[1]/div/div/div[1]/input').click()
    # pegando a tabela que contenha os horarios da linha selecionada
    horarios = driver.find_elements(by=By.CLASS_NAME,value='bg-white')
    
    result = []
    for i in horarios:
        result.append(i.text)

    return result

# Funcao que da insert no banco de dados de horarios
def UpdateDB():
    #abre o navegador
    driver = init()
    #procura todas as linhas de onibus disponiveis no DB
    linhas = db.search('linhas')
    for j in linhas:
        #pesquisa o horario pelo código da linha de onibus de acordo com o banco 
        listapagina = timeSearch(j[1], driver)

        for i in range(len(listapagina)):
            data = listapagina[i].split('\n')   #separando os dados recebidos do site
            ponto = data[0]                     #ponto do onibus
            dia = data[2]                       #tipo de dia (DIA UTIL, SABADO ou DOMINGO)
            horario = data[3:(len(data)-1)]     #Horario 
            # print(f" \n {str(ponto)}\n {dia}\n {horario}")
            for i in horario:
                db.insert('horario', f"'{str(ponto)}','{dia}','{i}',{j[0]}")
                print()
