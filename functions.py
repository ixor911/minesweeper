import os
import random
clear = lambda: os.system('cls')

# X, Y, amount_bombs
difficulty1 = [10, 8, 10]
difficulty2 = [18, 14, 40]
difficulty3 = [24, 20, 99]


def choose_difficulty():
    while True:
        ans = input("Choose difficulty:\n"
                    "1. Easy\n"
                    "2. Medium\n"
                    "3. Hard\n")
        clear()

        if ans in ['1', '2', '3']:
            return int(ans)
        else:
            input("Validation error\n"
                  "Continue?\n")
            clear()


def set_minefield(difficulty):
    minefield = []
    user_field = []

    if difficulty == 1:
        for i in range(0, difficulty1[0] + 1):
            line = []
            user_line = []
            for j in range(0, difficulty1[1] + 1):
                line.append(0)
                user_line.append('#')
            minefield.append(line)
            user_field.append(user_line)
    elif difficulty == 2:
        for i in range(0, difficulty2[0] + 1):
            line = []
            user_line = []
            for j in range(0, difficulty2[1] + 1):
                line.append(0)
                user_line.append('#')
            minefield.append(line)
            user_field.append(user_line)
    elif difficulty == 3:
        for i in range(0, difficulty3[0] + 1):
            line = []
            user_line = []
            for j in range(0, difficulty3[1] + 1):
                user_line.append('#')
                line.append(0)
            minefield.append(line)
            user_field.append(user_line)
    else:
        print("Error in set_minefield")

    return minefield, user_field


def set_bombs(minefield, chance, difficulty):
    left_bombs = difficulty[2]
    while True:
        for i in range(0, difficulty[0]):
            for j in range(0, difficulty[1]):
                if random.randint(0, 100) < chance * 100 and minefield[i][j] != "B" and left_bombs > 0:
                    minefield[i][j] = "B"
                    left_bombs -= 1
                elif left_bombs == 0:
                    return minefield


def set_bombs_by_difficulty(difficulty, minefield):
    if difficulty == 1:
        chance = difficulty1[2] / (difficulty1[0] * difficulty1[1])
        minefield = set_bombs(minefield, chance, difficulty1)
    elif difficulty == 2:
        chance = difficulty2[2] / (difficulty2[0] * difficulty2[1])
        minefield = set_bombs(minefield, chance, difficulty2)
    elif difficulty == 3:
        chance = difficulty2[2] / (difficulty2[0] * difficulty2[1])
        minefield = set_bombs(minefield, chance, difficulty2)
    else:
        print("Error in set_bombs")

    return minefield


def set_numbers_around_bombs(minefield):
    for i in range(0, len(minefield)):
        for j in range(0, len(minefield[i])):
            if minefield[i][j] == "B":
                try:
                    minefield[i - 1][j - 1] += 1
                except:
                    pass

                try:
                    minefield[i - 1][j] += 1
                except:
                    pass

                try:
                    minefield[i - 1][j + 1] += 1
                except:
                    pass

                try:
                    minefield[i][j - 1] += 1
                except:
                    pass

                try:
                    minefield[i][j + 1] += 1
                except:
                    pass

                try:
                    minefield[i + 1][j - 1] += 1
                except:
                    pass

                try:
                    minefield[i + 1][j] += 1
                except:
                    pass

                try:
                    minefield[i + 1][j + 1] += 1
                except:
                    pass

    return minefield


def show_minefield(minefield):
    for i in range(0, len(minefield) - 1):
        for j in range(0, len(minefield[i]) - 1):
            print(minefield[i][j], end=" ")
        print()


def start_game():
    clear()

    difficulty = choose_difficulty()
    minefield, user_field = set_minefield(difficulty)
    minefield = set_bombs_by_difficulty(difficulty, minefield)
    minefield = set_numbers_around_bombs(minefield)

    show_minefield(user_field)









