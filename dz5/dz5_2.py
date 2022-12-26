# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой.
# За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход.
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""
from random import randint

player = 0
bot = 0
konfet = 150


def player_turn():
    global konfet
    global player
    player = int(input('Бери свои конфеты, друг(1-28) '))
    if player < 1 or player > 28 or player > konfet:
        player = int(input('Несколько не верный ввод, попробуй еще разок (1-28) '))
    konfet -= player
    print(f' ты взял {player} конфет, осталось {konfet}')
    if konfet == 0:
        return print(' ура победа!')
    bot_turn()


def bot_turn():
    global konfet
    global bot
    bot = konfet % 29 if konfet % 29 != 0 else randint(1, 28)
    konfet -= bot
    print(f'Бот взял {bot} конфет, осталось {konfet}')

    if konfet == 0:
        return print('Бот победил!')
    player_turn()


turn = randint(1, 2)
while konfet > 0:
    if turn == 1:
        player_turn()
    else:
        bot_turn()
