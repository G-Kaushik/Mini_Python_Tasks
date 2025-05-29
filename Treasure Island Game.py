print(r'''
********************************************************
                            _.--.
                        _.-'_:-'||
                    _.-'_.-::::'||
               _.-:'_.-::::::'  ||
             .'`-.-:::::::'     ||
            /.'`;|:::::::'      ||_
           ||   ||::::::'     _.;._'-._
           ||   ||:::::'  _.-!oo @.!-._'-.
           \'.  ||:::::.-!()oo @!()@.-'_.|
            '.'-;|:.-'.&$@.& ()$%-'o.'\U||
              `>'-.!@%()@'@_%-'_.-o _.|'||
               ||-._'-.@.-'_.-' _.-o  |'||
               ||=[ '-._.-\U/.-'    o |'||
               || '-.]=|| |'|      o  |'||
               ||      || |'|        _| ';
               ||      || |'|    _.-'_.-'
               |'-._   || |'|_.-'_.-'
               '-._'-.|| |' `_.-'
                    '-.||_/.-'
*********************************************************                    
''')
print("Welcome to the Game of Treasure Island.")
print("Your mission is to find the treasure.")
choice = input('''You are at a cross road. Where do you want to go? 
         Type "left" or "right" 
         ''')
if choice == "left" or choice == "Left":
    choice_lake = input('''You reached to a lake. There is an island in the middle of the lake. 
        Type 'wait' to wait for a boat. Type 'swim' to swim across. 
        ''')
    if choice_lake == "wait" or choice_lake == "Wait":
        choice_island = input(''' You arrived at the island unharmed. There is a house with three doors. 
                One red, one yellow and one blue. Which colour do you choose? 
                ''')
        if choice_island == "red" or choice_island == "Red":
            print("It's a room with bombs. Game Over.")
        elif choice_island == "yellow" or choice_island == "Yellow":
            print("You found the treasure! You Win!")
        elif choice_island == "blue" or choice_island == "Blue":
            print("You enter a room full of fake treasure. Game Over.")
        else:
            print("Please type the correct format")
    elif choice_lake == "swim" or choice_lake == "Swim":
        print("You got eaten by sharks. Game Over.")
    else:
        print("Please type the correct format")
elif choice == "right" or choice == "Right":
    print("You got lost in the forest. Game Over.")
else:
    print("Please type the correct format")