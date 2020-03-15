from chatterbot.trainers import ChatterBotCorpusTrainer, ListTrainer
from chatterbot import ChatBot

# bot = ChatBot('Irineu')
# bot = ChatBot(
#     'Irineu',
#     storage_adapter='chatterbot.storage.SQLStorageAdapter',
#     database_uri='sqlite:///database.sqlite3'
# )

# conversa = ListTrainer(bot)
# conversa.train([
#     'Oi?',
#     'Eae',
#     'Qual o seu nome?',
#     'Irineu, você não sabe e nem eu',
#     'Prazer em te conhecer',
#     'Igualmente meu patrão',
# ])
# while True:
#     try:
#         resposta = bot.get_response(input("Usuário: "))
#         if float(resposta.confidence) > 0.5:
#             print("Irineu: ", resposta)
#         else:
#             print("Eu não entendi :(")
#     except(KeyboardInterrupt, EOFError, SystemExit):
#         break
from spacy.cli import train

bot = ChatBot('Irineu')

conversa = [
    'Oi?',
    'Eae',
    'Qual o seu nome?',
    'Irineu, você não sabe e nem eu!',
    'Prazer em te conhecer',
    'Igualmente',
]

# trainer = ListTrainer(bot)
# trainer.train(conversa)

trainer = ChatterBotCorpusTrainer(bot)

# Treino baseado no corpus em Portugues
trainer.train("chatterbot.corpus.Portuguese")

print('Olá, meu nome é Irineu, em que posso ajudá-lo?')
while True:
    quest = input('Você: ')
    response = bot.get_response(quest)
    print('Irineu: ', response)