import telebot
import urbs as urbs
from Secrets import secretos

CHAVE_API = secretos.api_key

bot = telebot.TeleBot(CHAVE_API)

global pesquisaSaldo ,pesquisaHistorico

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, """
    O que deseja hoje?
    /saldo     - Consultar Saldo
    /historico - Consultar Historico
    """)

@bot.message_handler(commands=['saldo'])
def saldo(message):
    global pesquisaSaldo ,pesquisaHistorico
    print("Saldo")
    pesquisaHistorico = False 
    pesquisaSaldo = True
    bot.reply_to(message,'Para consultar saldo\nInsira seu CPF:')
    if(pesquisaSaldo and not pesquisaHistorico):
        @bot.message_handler()
        def consulta_S(message):
            global pesquisaSaldo ,pesquisaHistorico
            if secretos.certify_cpf(message.text):
                bot.reply_to(message,"Procurando Saldo...")
                resposta = urbs.saldo(message.text)
                resposta = f'{resposta[3]}\n Saldo Usuario: {resposta[0]}\n Saldo Comum: {resposta[1]}\n Total de passagens: {resposta[2]}'
                bot.reply_to(message,resposta)
            else:
                bot.reply_to(message,'CPF invalido!\n Digite outro ou contate o ADM')
            pesquisaHistorico = False
            pesquisaSaldo = False

            
                


@bot.message_handler(commands=['historico'])
def historic(message):
    global pesquisaSaldo ,pesquisaHistorico
    print("Historic")
    pesquisaSaldo = False
    pesquisaHistorico = True
    bot.reply_to(message,'Para consultar o historico\nInsira seu CPF:')
    if(pesquisaHistorico and not pesquisaSaldo):
        @bot.message_handler()
        def consulta_H(message):
            global pesquisaSaldo ,pesquisaHistorico
            if secretos.certify_cpf(message.text):
                bot.reply_to(message,"Procurando Historico...")
                resposta = urbs.historico(message.text)
                resposta = f'''
                {resposta[0]}
                {resposta[1]}'''
                bot.reply_to(message,resposta)
            else:
                bot.reply_to(message,'CPF invalido!\n Digite outro ou contate o ADM')
            pesquisaSaldo = False
            pesquisaHistorico = False

             
        




bot.infinity_polling()