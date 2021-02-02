from classes.player import Player


# What can we do in this game, how does it begin

game_on = True

player1 = Player()

while game_on:

    print("game start")
    print("you find yourself.... (leading an empire, fighting monsters?)")

    player1.choose_action()
    choice = input("Choose action:")

    if choice == 1:
        ...

    elif choice == 2:
        ...

    elif choice == 3:
        ...
