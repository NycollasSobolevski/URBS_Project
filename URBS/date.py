from datetime import date

def dates():
    DataAtual = date.today()
    max = DataAtual.strftime('%d/%m/%y').split('/')
    min = date(DataAtual.year,DataAtual.month - 1,DataAtual.day +1).strftime('%d/%m/%y').split('/')
    resMin = f'{min[0]}/{min[1]}/20{min[2]}'
    resMax = f'{max[0]}/{max[1]}/20{max[2]}'
    return resMin, resMax
