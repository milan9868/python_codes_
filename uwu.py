from random import choice
from sys import exit as s_exit

choices = ["s", "w", "g"]

computer_choice = choice(choices)

player_choice = input("From Snake (s), Water (w) and Gun (g), you will pick...\n -> ")

if player_choice.lower() in ("s", "w", "g"):
    if player_choice == computer_choice:
        s_exit(f"Game is a tie. Computer picked {computer_choice} and you picked {player_choice}")
        
    elif computer_choice == "s":
        if player_choice == "w":
            s_exit(f"You lost. Computer picked {computer_choice} and you picked {player_choice}")
            
        exit(f"You win. Computer picked {computer_choice} and you picked {player_choice}")
        
    elif computer_choice == "w":
        if player_choice == "g":
            s_exit(f"You lost. Computer picked {computer_choice} and you picked {player_choice}")
            
        exit(f"You win. Computer picked {computer_choice} and you picked {player_choice}")
       
    elif computer_choice == "g":
         if player_choice == "s":
             s_exit(f"You lost. Computer picked {computer_choice} and you picked {player_choice}")
             
         exit(f"You win. Computer picked {computer_choice} and you picked {player_choice}")
         
s_exit("Invalid choice")