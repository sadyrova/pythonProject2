import random

roll = random.randint(1, 30)


def play_game(money):
    print("Добро пожаловать в казино! У вас 1000 долларов. Удачи!")

    while True:
        bet = int(input('Ваша ставка: '))
        number = int(input('Число: '))
        print(f"Выпало число {abs(roll)}!")
        if roll == number:
            money = bet * 2
            print(f'Поздравляем! Вы выиграли {money} $.!\n Ваше состояние {money} $.\n')
        else:
            money -= bet
            print(f'Вы не угадали, \nВаше состояние {money} $.\n')

        choice = input("Хотите продолжить игру? (да/нет) ")
        if choice.lower() == "нет":
            print("Спасибо за игру! До свидания!")
            break

        if money <= 0:
            print("Вы проиграли все деньги. До свидания!")
            break

