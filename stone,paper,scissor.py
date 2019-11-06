import random
player1 = input("Select r, p or s")
player2 = ""

computer = random.randint(1,3)
if computer == 1:
    player2 = "r"
elif computer == 2:
    player2 = "p"
else:
    player2 = "s"

print("Computer Selected : ", player2)

if player1 == player2:
    print("DRAW")
elif player1 == "r" and player2 == "s":
    print("player 1 wins")
elif player1 == "s" and player2 == "r":
    print("player 2 wins")
elif player1 == "r" and player3 == "p":
    print("player 2 wins")
elif player1 == "p" and player2 == "r":
    print("player 1 wins")
elif player1 == "p" and player2 == "s":
    print("player 2 wins")
elif player1 == "s" and player2 == "p":
    print("player 2 wins")


