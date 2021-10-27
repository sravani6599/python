print("game")
p1=str(input("player1,Enter rock/paper/scissors:"))
p2=str(input("player2:Enter rock/paper/scissors:"))
def rock_paper_scissors(player1,player2):
    while player1==player2:
        print("match is tied")
        player1 = str(input("player1,Enter rock/paper/scissors:"))
        player2 = str(input("player2:Enter rock/paper/scissors:"))
    if player1 == "rock" and player2 == "paper" :
        print("player2 wins")
    elif player1 == "paper" and player2 == "rock":
        print("player1  wins")
    elif player1 == "paper" and player2 == "scissors":
        print("player2  wins")
    elif player1 == "rock" and player2 == "scissors":
        print("player1  wins")
    elif player1 == "scissors" and player2 == "rock":
        print("player1  wins")
    elif player1 == "scissors" and player2 == "paper":
        print("player1  wins")
rock_paper_scissors(p1,p2)


