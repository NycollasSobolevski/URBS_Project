import telebot
import secretos
import urbs

bot = telebot.TeleBot(secretos.api_key)
resposta = ''

def apel(bot, update):
    msg = update.message.reply_text('Qual o seu apelido?')
    bot.register_next_step_handler(msg, nome_de_uma_funcao)
    bot.send_message(chat_id = update.message.chat_id, text = f"Uau, seu apelido é {resposta}" )


def nome_de_uma_funcao(message):
# Guardando a resposta do usuario em uma variavel
    resposta = message.text
    print(resposta)
cpf =''
@bot.message_handler(commands=["opcao1"])
def Saldo(mensagem):
    bot.send_message(mensagem.chat.id, f"Digite seu CPF")


    # aprender como receber uma mensagem
    #TODO: 1puxar funcao de consultar saldo
    if secretos.certify_cpf(cpf):
        saldo = urbs.saldo(cpf)
        bot.send_message(mensagem.chat.id, f"{saldo[len(saldo)-1]} seu saldo é de {saldo[:3]}")
    else:
        bot.send_message(mensagem.chat.id, f"CPF invalido no banco de dados, digite novamente ou contate o ADMIN")


def Save_cpf(message):
  # Guardando a resposta do usuario em uma variavel
  cpf = message.text




@bot.message_handler(commands=['opcao2'])
def Historico(msg):
    #TODO: puxar funcao de consultar saldo
    bot.send_message(msg.chat.id, f"[name] seu Historico: [historico]")

def verify(msg):
    return True

@bot.message_handler(func=verify)
def responder(msg):
    text = """
    Escolha uma opção para continuar (Clique no item):
     /opcao1 - Consultar saldo
     /opcao2 - Consultar Historico
    Responder qualquer outra coisa não vai funcionar, clique em uma das opções
    """
    bot.reply_to(msg,text)

bot.polling()