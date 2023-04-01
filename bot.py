import telebot
import urbs
from Palavras_secretas import secretos

CHAVE_API = secretos.api_key

bot = telebot.TeleBot(CHAVE_API)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, """
    O que deseja hoje?
    /saldo     - Consultar Saldo
    /historico - Consultar Historico
    """)

@bot.message_handler(commands=['saldo'])
def saldo(message):
    bot.reply_to(message,'Insira seu CPF:')
    @bot.message_handler(func=lambda m:True)
    def consulta_S(message):
        if secretos.certify_cpf(message.text):
            resposta = urbs.saldo(message.text)
            resposta = f'''
            {resposta[3]}
            Saldo Usuario: {resposta[0]}
            Saldo Comum: {resposta[1]}
            Total de passagens: {resposta[2]}
            '''
            bot.reply_to(message,resposta)
        else:
            bot.reply_to(message,'CPF invalido!\n Digite outro ou contate o ADM')
            


@bot.message_handler(commands=['historico'])
def historic(message):
    bot.reply_to(message,'Insira seu CPF:')
    @bot.message_handler(func=lambda m:True)
    def consulta_H(message):
        if secretos.certify_cpf(message.text):
            resposta = urbs.historico(message.text)
            resposta = f'''
            {resposta[0]}
            {resposta[1]}'''
            bot.reply_to(message,resposta)
        else:
            bot.reply_to(message,'CPF invalido!\n Digite outro ou contate o ADM')
             
        




bot.infinity_polling()