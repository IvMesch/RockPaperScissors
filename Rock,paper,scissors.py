import random

options = ["scissors", "rock", "paper"]
command = ["!exit", "!rating"]

player_name = input("Enter your name:")
player_score = 0
print(f"Hello, {player_name}")
player_option = ""

file_ = open("rating.txt", 'r')
for line in file_:
    player = line.split()
    for item in range(len(player) - 1) :
        if item == player_name:
            player_score = player[i + 1]
file_.close()

new_options = str(input())
if new_options != '':
    options = new_options.split(",")
print("Okay, let's start")

while player_option != "!exit":
    player_option = str(input())
    if player_option in command:
        
        if (player_option == "!exit"):
            file_ = open("rating.txt", "a")
            data_for_save = [player_name, player_score]
            file_.writelines(str(data_for_save))
            print("Bye!")
            exit()            
        elif (player_option == "!rating"):
            print(f"Your rating: {player_score}") 
    
    elif player_option in options:
        
        tmp = []
        comp_option = random.choice(options)
        
        if options.index(player_option) < len(options) // 2:
            for option in range(options.index(player_option),options.index(player_option) + len(options) // 2 + 1):
                tmp.append(options[option])
                for index in range(len(tmp) - 1, 0, -1):
                    options.insert(options.index(player_option),options.pop(index)) 
        
        elif options.index(player_option) > len(options) // 2:
            for option in range(options.index(player_option) - len(options) // 2 - 1, options.index(player_option)):
                tmp.append(options[option])
                for index in range(len(tmp) -1, 0, -1):
                    options.insert(options.index(player_option),options.pop(index))
        
        if player_option == comp_option:
            player_score += 50
            print(f"There is a draw ({comp_option})")
        
        elif options.index(player_option) < options.index(comp_option):        
            print(f"Sorry, but computer chose {comp_option}")
        
        elif options.index(player_option) > options.index(comp_option):
            player_score += 100 
            print(f"Well done. Computer chose {comp_option} and failed")
    
    else:
        print("Invalid input")
