
board = list(range(1, 10))

def pole(board):
    print('-' * 13)
    for i in range(3):
        print(f'| {board[0 + i * 3]} | {board[1 + i * 3]} | {board[2 + i * 3]} |')
        print('-' * 13)


def vvod(XO):
    valid = False
    while not valid:
        player_answer = input("Куда поставим " + XO + "? ")
        try:
            player_answer = int(player_answer)
        except ValueError:
            print("Некорректный ввод.")
            continue
        if 1 <= player_answer <= 9:
            if str(board[player_answer - 1]) not in "XO":
                board[player_answer - 1] = XO
                valid = True
            else:
                print("Клетка занята!")
        else:
            print("Некорректный ввод. Введите число от 1 до 9.")
def check_win(board):
    victories = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
    for each in victories:
        if board[each[0]] == board[each[1]] == board[each[2]]:
            return board[each[0]]
    return False
def main(board):
    counter = 0
    win = False
    while not win:
        pole(board)
        if counter % 2 == 0:
            vvod("X")
        else:
            vvod("O")
        counter += 1

        tmp = check_win(board)
        if tmp:
            print(tmp, "выиграл!")
            win = True
            break
        if counter == 9:
            print("Ничья!")
            break
    pole(board)


main(board)


