'''
Script description:Number race
Dev: 
Date: 13-09-2024
'''

from random import randint
import os
statues_menu = True


def main_menu():
    global statues_opts
    statues_opts = True
    print("::: MAIN MENU")
    print("[1]. Start game")
    print("[2]. Help")
    print("[3]. Exit")
    
    while statues_opts:
        opt = int(input("Press any option: "))
        if opt < 1 or opt > 3:
          print("Error. Press any option between 1 and 3")
        else:
            statues_opts = False
    return opt

while statues_menu:
    os.system('Clear')
    op = main_menu()
    if op == 1:
        os.system('clear')
        print("::: Welcome to number race:::")
        
        players = int(input("Press number of players [1:4]"))
        
        print("::: Level menu :::")
        print("[1]. Basic")
        print("[1]. Intermediate") 
        print("[1]. Advance")
        print("[1]. Expert")
        opt = int(input("Press any option: "))
        
        if opt == 1:
            pos = 20
        elif opt == 2:
            pos = 30
        elif opt == 3:
            pos = 50
        else:
            pos = 100
            
        #Star Game
        statues_game = True
        roll_count = 0
        roll_acum = 0
        while statues_game:
            os.system('clear')
            key = input("Press any key to roll dice...")
            dice1 = randint(1,6)
            dice2 = randint(1,6)

            print(f"Dice 1: {dice1}")
            print(f"Dice 2: {dice2}")
            total = dice1 + dice2
            print(f"Total roll: {total}")
            
            roll_count += 1 #roll_count = roll_count +1
            roll_acum +=  total
            print(f"Total game: {roll_acum}")
            
            if roll_acum >= pos:
                print(":::YOU WIN, CONGRATULATIONS:::")
                statues_game = False
                
            os.system('pause')
            
        print("STATITICS")
        print(f"Total rolls: {roll_count}")
        print(f"Total dices: {roll_acum}")
        
        key = input("Press any key to go to the main menu...")
    elif op == 2:  
        print("Help under construction")
        key = input("Press any key to go to the main menu..")
    else:
        print("See you later")
        key = input("Press any key to exit")
        break

