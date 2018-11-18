teams = ["yes", "no"]
lakers_players = ["rondo", "kuzma", "lebron", "ingram"]
 
name = raw_input("What is your name?")
if len(name) > 0:
  print("Hello, " + name + ". Welcome to the NBA!")
  print("")
else:
  print("That is not a name.")
  exit()
 
response = ""
while response not in teams:
    response = raw_input("Do you want to be drafted to the lakers?")
    if response == "yes":
        print("Which Laker will you pass to in the last 10 seconds?")
        print("")
    elif response == "no":
        print("You made a smart move. You will most likely make it to the playoffs now.")
        exit()
    else: 
        print("That is not a response.")
        exit()
 
response = ""
while response not in lakers_players:
    print("At the top of the key, you see rondo.")
    print("")
    print("Posting up, you see lebron.")
    print("")
    print("There is a smaller defender gaurding kuzma")
    print("")
    print("ingram looks at and calls for the ball")
    print("")
    response = raw_input("Who do you pass to?")
    if response == "rondo":
        print("Rondo gets passed the defender but passes it to Lebron instead of scoring. You lose, next time shoot yourself " + name + ".")
        exit()
    elif response == "kuzma":
        print("Kuzma shoots over the defender and makes the shot. Congradulations, you win!")
        exit()
    elif response == "lebron":
        print("Lebron misses the shot but gets fouled. Unfortunately, he misses both crutical free-throws and loses you the game. Never pass to Lebron again.")
        exit()
    elif response == "ingram":
        print("Ingram fakes out the defender and drives in for the game-winning layup. Congradulations " + name + " you won!")
        exit()
    else:
        print("That is not an option, he's on the bench.")
        exit()