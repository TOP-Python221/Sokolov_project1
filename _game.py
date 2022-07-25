"""Модуль отрисовки игрового поля, и непосредственно партии игры"""

# FIXME: в Архитектуре у вас совсем другая структура данных для работы с полями, в виде матрицы — именно её вы должны проверять и именно для неё должны писать код. А здесь у вас плоская структура данных
board = range(1, 10)


# функция вывода на экран графического поля игры
def draw_board(board):
    print("-------------")
    for i in range(3):
        print("|", board[0 + i * 3], "|", board[1 + i * 3], "|", board[2 + i * 3], "|")
        print("-------------")


draw_board(board)


# функция изменяющая список board
def take_input(player_token):
    """Принимает параметр крестик или нолик """
    valid = False
    while not valid:
        player_answer = input("Выберите клетку " + player_token + "?")
        try:
            player_answer = int(player_answer)
        # удостоверяемся что клетка не занята и ограничиваемвыбор пользователя от 1 до9
        except:
            print("Вы точно ввели число?")
            continue
        if player_answer >= 1 and player_answer <= 9:
            if str(board[player_answer - 1]) not in "XO":
                board[player_answer - 1] = player_token
                valid = True
            else:
                print("Клетка занята")
        else:
            print("Некорректный ввод. Введите число от 1 до 9 что бы сделать ход")


# Проверка выигрышной комбинации
def check_win(board):
    """Функция прверяет выгрышную комбинацию после чего определяет победителя"""
    win_coord = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6),
                 (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
    for each in win_coord:
        if board[each[0]] == board[each[1]] == board[each[2]]:
            return board[each[0]]
        return False
