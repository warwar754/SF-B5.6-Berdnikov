# Полe
field = (
    f"  0 1 2\n0 - - -\n1 - - -\n2 - - -\n")
# Список выйгрышных комбинаций
win_game = [[["0", "0"], ["1", "1"], ["2", "2"]],
            [["0", "2"], ["1", "1"], ["2", "0"]],
            [["0", "0"], ["0", "1"], ["0", "2"]],
            [["1", "0"], ["1", "1"], ["1", "2"]],
            [["2", "0"], ["2", "1"], ["2", "2"]],
            [["0", "0"], ["1", "0"], ["2", "0"]],
            [["0", "1"], ["1", "1"], ["2", "1"]],
            [["0", "2"], ["1", "2"], ["2", "2"]], ]

# Список ходов
players_moves = []
# номер хода
move = 0
# Ходы игроков
player_A = []
player_B = []


def game(func):
    def wrapper():
        global field
        global move
        move += 1
        print(f"{field} ход №{move}")
        if move % 2 == 0:
            field = list(field)
            value_move = func()
            player_A.append(value_move)
            b = (field.index(value_move[0], 8)) + \
                ((int(value_move[1]) * 2) + 2)
            field = (list(field))
            field.pop(b)
            field.insert(b, "X")
            field = "".join(field)
        elif move % 2 == 1:
            field = list(field)
            value_move = func()
            player_B.append(value_move)
            b = (field.index(value_move[0], 8)) + \
                ((int(value_move[1]) * 2) + 2)
            field = (list(field))
            field.pop(b)
            field.insert(b, "O")
            field = "".join(field)
    return wrapper


@game
# ввод значения поля
def moves():
    list_moves = []
    while True:
        while True:
            line = input("Введи номер строки. От 0 до 2\n")
            if line.isdigit() and 0 <= int(line) < 3:
                list_moves.append(line)
                break
            else:
                print(
                    'Номер должен состоять из целого положительного числа! И в промежутке от 0 до 2')
        while True:
            column = input("Введи номер столца. От 0 до 2\n")
            if column.isdigit() and 0 <= int(column) < 3:
                list_moves.append(column)
                break
            else:
                print(
                    'Номер должен состоять из целого положительного числа! И в промежутке от 0 до 2')
        # Проверка был ли такой ход
        if list_moves in players_moves:
            list_moves = []
            print("".join(field))
            print("Такой ход уже был")
        else:
            players_moves.append(list_moves)
            break
    return list_moves


while True:
    # Проверка Кто выйграл
    if player_A in win_game:
        print("Победил Первый игрок")
        break
    elif player_B in win_game:
        print("Победил второй игрок")
        break
    elif move == 9:
        print("Победила дружба")
        break
    else:
        moves()
