
import random
import sys
while True:
        abobus = 0
        while (abobus == 0):
                player = int(input("1-камень,  2-ножницы, 3-бумага"))
                if (player == 1 or player == 2 or player == 3):
                    abobus = 1
                else:
                    print("ты куку?")
                    sys.exit()



        if player == 1:
                print("Вы выбрали камень.")
        if player == 2:
                print("Вы выбрали ножницы.")
        if player == 3:
                print("Вы выбрали бумагу.")
        cc = random.randint(1, 3)
        if cc == 1:
                print("Компьютер выбрал камень.")
        if cc == 2:
                print("Компьютер выбрал ножницы.")
        if cc == 3:
                print("Компьютер выбрал бумагу.")

        if player == cc:
                win = 0
        if player == 1 and cc == 2:
                win = 1
        if player == 1 and cc == 3:
                win = 2
        if player == 2 and cc == 1:
                win = 2
        if player == 2 and cc == 3:
                win = 1
        if player == 3 and cc == 1:
                win = 1
        if player == 3 and cc == 2:
                win = 2
        if win == 0:
                print("Ничья!")
        if win == 1:
                print("Победил игрок!")
        if win == 2:
                print("Победил компьютер!")
