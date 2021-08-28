# Assignment 2 - Text Based Game
# Name: Mark Alexander
# Student ID: 1504992

import sys
import os
import time
import random

PlayerIcon = "O"
Wall =  "▋"
Enemy = "X"
Spike = "▲"
Safe =  " "
Winner = "$"

Y00 = [1,1,1,1,1,1]
Y01 = [1,0,0,0,0,1]
Y02 = [1,3,2,3,2,1]
Y03 = [1,0,2,0,0,1]
Y04 = [1,0,0,2,0,1]
Y05 = [1,2,0,0,0,1]
Y06 = [1,2,2,2,0,1]
Y07 = [1,0,0,0,0,1]
Y08 = [1,3,2,2,2,1]
Y09 = [1,0,0,0,2,1]
Y10 = [1,2,2,3,2,1]
Y11 = [1,4,4,4,4,1]

XIndex = [Y00,Y01,Y02,Y03,Y04,Y05,Y06,Y07,Y08,Y09,Y10,Y11] # X axis on the Map.
PlayerPos = [1,2] # Player Postition 
XIndex[PlayerPos[0]][PlayerPos[1]] = PlayerIcon #Placing the Player's Character.

def print_slow(str): #FUNCTION TO PRINT STRINGS SLOW
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.01)
def print_slower(str): #FUNCTION TO PRINT STRINGS SLOWER
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.05)
def print_superslow(str): #FUNCTION TO PRINT STRINGS SUPERSLOW
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(1)

def titlescreen(): #FUNCTION TO PRINT THE TITLESCREEN
    print("")
    os.system('cls')
    print_slow("""
##################################################
#                                                #""")
    print_slower("\n# WELCOME TO HONEY QUEST [ONE]: The Sticky Thief #")
    print_slow("""\n#                                                #
################################################## 
#                    MAIN MENU                   #
#                  --- Play ---                  #       
#                  --- Help ---                  #       
#                  --- Quit ---                  #
############################################""")
    print_slower("######")
    titlescreen_options()

def titlescreen_options(): #FUNCTION OF COMMANDS THE USER CAN ENTER AT THE TITLESCREEN
    print("")
    option = input("\nUserConsole>")
    while option.lower() not in ['play','help','quit', 'mainmenu',]:
            print("Please enter a vaild command")
            option = input("> ")
    if option.lower() == ("play"):
        start_game()
    elif option.lower() == ("help"):
        help_menu_titlescreen()
    elif option.lower() == ("mainmenu"):
        title_screen()
    elif option.lower() == ("quit"):
        print_slow(">Exiting")
        print_superslow("...")
        print(" >Successful")
        sys.exit()

def help_menu_titlescreen(): #FUNCTION TO BRING UP THE HELP-MENU IN THE TITLESCREEN
    print("")
    os.system('cls')
    print('\n\t-- CONTROLS: --')
    print(' -> W to move FORWARD')
    print(' -> A to move LEFT')
    print(' -> S to move BACK')
    print(' -> D to move RIGHT')
    print('\n\t-- BATTLES: --')
    print(' -> "attack" = Type this command during battles to ATTACK')
    print(' -> "heal" = Type this command during battles to HEAL')
    print('\n\t-- MAP LEGEND: --')
    print(' -> "O" = Player Icon')
    print(' -> "X" = Enemy Icon')
    print(' -> "▲" = Spike Icon')
    print(' -> "$" = End Goal')
    print('\n\t-- OTHER: --')
    print(' -> "Help" = Opens Help Menu')
    print(' -> "MainMenu" = Return to Titlescreen at anytime')

    close_menu = input("\nTo close menu type 'Y':")
    close_menu = close_menu.upper()
    while close_menu != 'Y':
        close_menu = input("\nTo close menu type 'Y':")
        close_menu = close_menu.upper()
    if close_menu == "Y":
        titlescreen()
    

def help_menu_ingame(): #FUNCTION TO BRING UP THE HELP-MENU WHILE MOVING IN THE MAP
    print("")
    os.system('cls')
    print('\n\t-- CONTROLS: --')
    print(' -> W to move FORWARD')
    print(' -> A to move LEFT')
    print(' -> S to move BACK')
    print(' -> D to move RIGHT')
    print('\n\t-- BATTLES: --')
    print(' -> "attack" = Type this command during battles to ATTACK')
    print(' -> "heal" = Type this command during battles to HEAL')
    print('\n\t-- MAP LEGEND: --')
    print(' -> "O" = Player Icon')
    print(' -> "X" = Enemy Icon')
    print(' -> "▲" = Spike Icon')
    print(' -> "?" = Random Item')
    print(' -> "$" = End Goal')
    print('\n\t-- OTHER: --')
    print(' -> "Help" = Opens Help Menu')
    print(' -> "MainMenu" = Return to Titlescreen at anytime')

    close_menu = input("\nTo close menu type 'Y':")
    close_menu = close_menu.upper()
    while close_menu != 'Y':
        close_menu = input("\nTo close menu type 'Y':")
        close_menu = close_menu.upper()
    if close_menu == "Y":
        Moving_Player()

def help_menu_inbattle(): #FUNCTION TO BRING UP THE HELP-MENU IN A BATTLE
    print("")
    os.system('cls')
    print('\n\t-- CONTROLS: --')
    print(' -> W to move FORWARD')
    print(' -> A to move LEFT')
    print(' -> S to move BACK')
    print(' -> D to move RIGHT')
    print('\n\t-- BATTLES: --')
    print(' -> "attack" = Type this command during battles to ATTACK')
    print(' -> "heal" = Type this command during battles to HEAL')
    print('\n\t-- MAP LEGEND: --')
    print(' -> "O" = Player Icon')
    print(' -> "X" = Enemy Icon')
    print(' -> "▲" = Spike Icon')
    print(' -> "?" = Random Item')
    print(' -> "$" = End Goal')
    print('\n\t-- OTHER: --')
    print(' -> "Help" = Opens Help Menu')
    print(' -> "MainMenu" = Return to Titlescreen at anytime')

    close_menu = input("\nTo close menu type 'Y':")
    close_menu = close_menu.upper()
    while close_menu != 'Y':
        close_menu = input("\nTo close menu type 'Y':")
        close_menu = close_menu.upper()
    if close_menu == "Y":
        Battle()
    
def start_game(): #FUNCTION TO START THE GAME
    print("")
    os.system('cls')
    Skip_Story = input(">Skip story? Y/N:")
    Skip_Story = Skip_Story.upper()
    while Skip_Story not in ["Y", "N"]:
        print("Please enter a vaild command")
        Skip_Story = input(">Skip story? Y/N:")
        Skip_Story = Skip_Story.upper()
    if Skip_Story == "N":
        os.system('cls')
        print("\n[UNKNOWN VOICE]")
        print_slower(""" "MR. BEAR WAKE UP!!" """)
        Reply = input("\n\n(Press 'ENTER' to reply)")
        print("\n[YOU]")
        print_slower("*Still sleeping*")
        print_slower("   ")
        os.system('cls')
        print("\n[UNKNOWN VOICE]")
        print_slower(""" "MR. BEAR THIS IS SERIOUS!!!" """)
        Reply = input("\n\n(Press 'ENTER' to reply)")
        print("\n[YOU]")
        print_slower("*Still sleeping*")
        print_slower("   ")
        os.system('cls')
        print("\n[UNKNOWN VOICE]")
        print_slower(""" "I have honey..." """)
        Reply = input("\n\n(Press 'ENTER' to reply)")
        print("\n[YOU]")
        print_slower("*You awake for the honey...*")
        print_slower("   ")
        os.system('cls')
        print("\n[FOX FRANK]")
        print_slower(""" "Ben Bear... I have bad news I don't actually have honey... NINJAS STOLE IT" """)
        Reply = input("\n\n(Press 'ENTER' to reply)")
        print("\n[YOU]")
        print_slower(""" "SOMEONE DID WHAT?! WHERE ARE THEY?!" """)
        print_slower("   ")
        os.system('cls')
        print("\n[FOX FRANK]")
        print_slower(""" "They marked the honey on this map for you as '$'. Sounds like a trap if you ask me, or like an idea for an assignment in a programming fundamentals class..." """)
        Reply = input("\n\n(Press 'ENTER' to reply)")
        print("\n[YOU]")
        print_slower(""" "Well then what are we waiting for? I need my honey back for breakfast" """)
        print_slower("   ")
        os.system('cls')
        print("\n\tHONEY QUEST [ONE]: The Sticky Thief")
        print("\t\tHOW TO PLAY:")
        print('------------------------------------------------')
        print('\n\t-- CONTROLS: --')
        print(' -> W to move FORWARD')
        print(' -> A to move LEFT')
        print(' -> S to move BACK')
        print(' -> D to move RIGHT')
        print('\n\t-- BATTLES: --')
        print(' -> "attack" = Type this command during battles to ATTACK')
        print(' -> "heal" = Type this command during battles to HEAL')
        print('\n\t-- MAP LEGEND: --')
        print(' -> "O" = Player Icon')
        print(' -> "X" = Enemy Icon')
        print(' -> "▲" = Spike Icon')
        print(' -> "$" = End Goal')
        print('\n\t-- OTHER: --')
        print(' -> "Help" = Opens Help Menu')
        print(' -> "MainMenu" = Return to Titlescreen at anytime')
        print('\n------------------------------------------------')
        Continue = input("\n\n(Press 'ENTER' to Continue)")
        os.system('cls')
        print("""\n>>>Battle Sequence Explained:

-> As you travel through the map to find the missing honey, you will encounter battles along the way. 

-> During each battle you will need to fight a Ninja. They are trying to stop you!!!! (Marked as a 'X' on the map)

-> At the start of each new battle, both you and the Ninja will start with three health points each.
""")
        Continue = input("\n\n(Press 'ENTER' to Continue)")
        os.system('cls')
        print("""-> The battle is broken into battle phases. During each battle phase you will need to make one of two choices. To either heal and increase your health by one, or attack and inflict one damage to the Ninjas health.

-> At each battle phase, you will get to choose first and the Ninja will choose second.

-> The object of the battle is to reduce the Ninja health to zero before yours is reduced to zero.  
But be careful, if your health is reduced to zero before the Ninjas, then the Ninja has won the battle, you will die and the game will end.  

---->Good luck in your journey, and remember.......choose wisely.
""")
        Continue = input("\n\n(Press 'ENTER' to Continue)")
        print("\n-----------------")
        print_slow(">Loading map")
        print_superslow("...")
        print("\n-----------------")
        print("")
        PlayerPos[0] = 1
        PlayerPos[1] = 2
        Moving_Player()
    os.system('cls')
    print("\tHONEY QUEST [ONE]: The Sticky Thief")
    print("\t\tHOW TO PLAY:")
    print('------------------------------------------------')
    print('\n\t-- CONTROLS: --')
    print(' -> W to move FORWARD')
    print(' -> A to move LEFT')
    print(' -> S to move BACK')
    print(' -> D to move RIGHT')
    print('\n\t-- BATTLES: --')
    print(' -> "attack" = Type this command during battles to ATTACK')
    print(' -> "heal" = Type this command during battles to HEAL')
    print('\n\t-- MAP LEGEND: --')
    print(' -> "O" = Player Icon')
    print(' -> "X" = Enemy Icon')
    print(' -> "▲" = Spike Icon')
    print(' -> "$" = End Goal')
    print('\n\t-- OTHER: --')
    print(' -> "Help" = Opens Help Menu')
    print(' -> "MainMenu" = Return to Titlescreen at anytime')
    print('\n------------------------------------------------')
    Continue = input("\n\n(Press 'ENTER' to Continue)")
    os.system('cls')
    print("""\n>>>Battle Sequence Explained:

-> As you travel through the map to find the missing honey, you will encounter battles along the way. 

-> During each battle you will need to fight a Ninja. They are trying to stop you!!!! (Marked as a 'X' on the map)

-> At the start of each new battle, both you and the Ninja will start with three health points each.
""")
    Continue = input("\n\n(Press 'ENTER' to Continue)")
    os.system('cls')
    print("""\n-> The battle is broken into battle phases. During each battle phase you will need to make one of two choices. To either heal and increase your health by one, or attack and inflict one damage to the Ninjas health.

-> At each battle phase, you will get to choose first and the Ninja will choose second.

-> The object of the battle is to reduce the Ninja health to zero before yours is reduced to zero.  
But be careful, if your health is reduced to zero before the Ninjas, then the Ninja has won the battle, you will die and the game will end.  

---->Good luck in your journey, and remember.......choose wisely.
""")
    Continue = input("\n\n(Press 'ENTER' to Continue)")
    print("\n-----------------")
    print_slow(">Loading map")
    print_superslow("...")
    print("\n-----------------")
    print("")
    PlayerPos[0] = 1
    PlayerPos[1] = 2
    Moving_Player()
       
def Print_Map(): #FUNCTION TO PRINT THE MAP
    print("")
    os.system('cls')
    print("")
    for row in range(len(XIndex)):
        line = 0
        line = XIndex[row]
        for col in range(len(XIndex[row])): 
            if(row == PlayerPos[0] and col == PlayerPos[1]): 
                print(PlayerIcon, end = " ")
            elif (XIndex[row][col] == 1): 
                print(Wall, end = " ")
            elif (XIndex[row][col] == 2): 
                print(Spike, end = " ")
            elif (XIndex[row][col] == 3): 
                print(Enemy, end = " ")
            elif (XIndex[row][col] == 4): 
                print(Winner, end = " ")
            else:
                print(Safe, end = " ")
        print("")
    return

def Moving_Player(): #FUNCTION TO MOVE (THE PLAYER = 'O') AROUND THE MAP.
    print("")
    Print_Map()
    moving = 1
    while moving == 1:
        print("""
 _______________________________
|                               |
| Where would you like to move? |
|_______________________________| """)
        SelectedSpace = input("\nUserConsole>")
        SelectedSpace = SelectedSpace.upper()

        if SelectedSpace == "W":
            PlayerPos[0] = PlayerPos[0] - 1            
            if XIndex[PlayerPos[0]][PlayerPos[1]] == 1:
                print_slow(""" ______________________________
|                              |
| A Wall Blocks This Direction |
|______________________________| """)
                PlayerPos[0] = PlayerPos[0] + 1
            elif XIndex[PlayerPos[0]][PlayerPos[1]] == 2:
                Game_Over()
            elif XIndex[PlayerPos[0]][PlayerPos[1]] == 3:
                Battle()
            elif XIndex[PlayerPos[0]][PlayerPos[1]] == 4:
                Win()
           

        elif SelectedSpace == "A":
            PlayerPos[1] = PlayerPos[1] - 1
            if XIndex[PlayerPos[0]][PlayerPos[1]] == 1:
                print_slow(""" ______________________________
|                              |
| A Wall Blocks This Direction |
|______________________________| """)
                PlayerPos[1] = PlayerPos[1] + 1
            elif XIndex[PlayerPos[0]][PlayerPos[1]] == 2:
                Game_Over()
            elif XIndex[PlayerPos[0]][PlayerPos[1]] == 3:
                Battle()
            elif XIndex[PlayerPos[0]][PlayerPos[1]] == 4:
                Win()
            

        elif SelectedSpace == "S":
            PlayerPos[0] = PlayerPos[0] + 1
            if XIndex[PlayerPos[0]][PlayerPos[1]] == 1:
                print_slow(""" ______________________________
|                              |
| A Wall Blocks This Direction |
|______________________________| """)
                PlayerPos[0] = PlayerPos[0] - 1
            elif XIndex[PlayerPos[0]][PlayerPos[1]] == 2:
                Game_Over()
            elif XIndex[PlayerPos[0]][PlayerPos[1]] == 3:
                Battle()
            elif XIndex[PlayerPos[0]][PlayerPos[1]] == 4:
                Win()
            
            
    
        elif SelectedSpace == "D":
            PlayerPos[1] = PlayerPos[1] + 1
            if XIndex[PlayerPos[0]][PlayerPos[1]] == 1:
                print_slow(""" ______________________________
|                              |
| A Wall Blocks This Direction |
|______________________________| """)
                PlayerPos[1] = PlayerPos[1] - 1
            elif XIndex[PlayerPos[0]][PlayerPos[1]] == 2:
                Game_Over()
            elif XIndex[PlayerPos[0]][PlayerPos[1]] == 3:
                Battle()
            elif XIndex[PlayerPos[0]][PlayerPos[1]] == 4:
                Win()

        elif SelectedSpace == "MAINMENU":
            titlescreen()

        elif SelectedSpace == "HELP":
            help_menu_ingame()
    
        Print_Map()
    
def Battle(): #FUNCTION FOR BATTLES WHEN THE PLAYER ENCOUNTERS A 'X' ON THE MAP.
    print("")
    os.system('cls')
    Enemy_Health = 3
    Player_Health = 3
    Enemy_Ability = ["attack", "heal", "miss"]
    Player_Moves = ["attack", "heal", "mainmenu", "help", "cheat"]
    Random_Lines = ["\tTHE NINJA THINKS ABOUT HIS NEXT MOVE...", "\tTHE NINJA TAKES A MOMENT TO THINK...","\tTHE NINJA ACKNOWLEDGES YOUR MOVE AND DECIDES..."]
    while Enemy_Health >= 0 and Player_Health >= 0:
        EnemyMove = random.choice(Enemy_Ability)
        EnemyHealthBar = "❤"*Enemy_Health
        PlayerHealthBar = "❤"*Player_Health
        os.system('cls')
        print("""
__________________________________________________________________________________
             __      ___     _     _____   _____   _      ___      __            
  ___   ___  \ \    | _ )   /_\   |_   _| |_   _| | |    | __|    / /  ___   ___ 
 |___| |___|  > >   | _ \  / _ \    | |     | |   | |__  | _|    < <  |___| |___|
             /_/    |___/ /_/ \_\   |_|     |_|   |____| |___|    \_\            
__________________________________________________________________________________""")
        print("""
        (ง︡'-'︠)ง
 -------------------------
> NINJA HEALTH: %s         
 -------------------------""" % (EnemyHealthBar))
        print("""
         ʕ•́ᴥ•̀ʔ
 ------------------------
> YOUR HEALTH: %s         
 ------------------------""" % (PlayerHealthBar))
        SelectedAbility = input("UserConsole>")
        SelectedAbility = SelectedAbility.lower()
        while SelectedAbility not in Player_Moves:
            print("""\n<INVAILD COMMAND> The avaliable commands to the PLAYER are:
    --> 'attack' 
    --> 'heal' 
    --> 'help' 
    --> 'mainmenu'
""")
            SelectedAbility = input("UserConsole>")
            SelectedAbility = SelectedAbility.lower()
            if SelectedAbility in Player_Moves:
                break
        if SelectedAbility == "attack": #PLAYER ATTACKS
            Enemy_Health = Enemy_Health - 1
            print("\n\t>You ATTACK! The NINJA will take ONE damage!")   
        elif SelectedAbility == "heal": #PLAYER HEALS
            Player_Health = Player_Health + 1
            print("\n\t>YOU HEALED! Now at %d HP!" % (Player_Health))
        elif SelectedAbility == "mainmenu": #PLAYER CAN LEAVE THE BATTLE AND RETURN TO THE MAINMENU
            titlescreen()
        elif SelectedAbility == "help": #PLAYER CAN LEAVE THE BATTLE AND OPEN UP THE HELP-MENU
            help_menu_inbattle()
        elif SelectedAbility == "cheat": #PLAYER CAN USE THIS CHEAT TO WIN INSTANTLY 
            print_slower("\n\t>You CHEAT and INSTANTLY WIN THIS BATTLE!")
            Enemy_Health = -1
        print("")
        print_slower(random.choice(Random_Lines))  #RANDOM MOVES DECIDED BY THE COMPUTER
        if EnemyMove == "attack": #ENEMY ATTACK HITS THE PLAYER
            Player_Health = Player_Health - 1
            print("\n\t>The Ninja ATTACKS, YOU will lose ONE health!!")
        elif EnemyMove == "heal": #ENEMY DECIDES TO HEAL
            Enemy_Health = Enemy_Health + 1
            print("\n\t>The Ninja HEALED! Now at %d HP!" % (Enemy_Health))                
        elif EnemyMove == "miss": #ENEMY MISSED THE ATTACK
            print("\n\t>The Ninja MISSED his attack...")
        Continue = input("\n(Press 'ENTER' to Resolve)")
        
    if Player_Health == 0:
        Game_Over()
    if Enemy_Health <= 0:
        os.system('cls')
        print("""
                 __     __   __   ___    _   _    __        __  ___   _   _   _      __                
                 \ \    \ \ / /  / _ \  | | | |   \ \      / / |_ _| | \ | | | |    / /                
  _____   _____   \ \    \ V /  | | | | | | | |    \ \ /\ / /   | |  |  \| | | |   / /   _____   _____ 
 |_____| |_____|  / /     | |   | |_| | | |_| |     \ V  V /    | |  | |\  | |_|   \ \  |_____| |_____|
                 /_/      |_|    \___/   \___/       \_/\_/    |___| |_| \_| (_)    \_\                
                                                                                                       
""")
        print(">You defeat the NINJA with %d HEALTH REMAINING!" % (Player_Health))
        print_slower(">Returning to map")
        print_superslow("...")
        Moving_Player()

def Game_Over(): #FUNCTION IF THE PLAYERS HEALTH = 0, OR HITS A SPIKE '▲' ON THE MAP.
    print("")
    os.system('cls')
    print("\n-----------------------------------------------------------------------")
    print("-----------------------------------------------------------------------")
    print("-----------------------------------------------------------------------")
    print_slow("""
   ____      _      __  __   _____      ___   __     __  _____   ____     
  / ___|    / \    |  \/  | | ____|    / _ \  \ \   / / | ____| |  _ \     
 | |  _    / _ \   | |\/| | |  _|     | | | |  \ \ / /  |  _|   | |_) |   
 | |_| |  / ___ \  | |  | | | |___    | |_| |   \ V /   | |___  |  _ <     
  \____| /_/   \_\ |_|  |_| |_____|    \___/     \_/    |_____| |_| \_\   
  
                        ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▄▄██████▄
                        ▒▒▒▒▒▒▒▒▒▒▄▄████████████▄
                        ▒▒▒▒▒▒▄▄██████████████████
                        ▒▒▒▄████▀▀▀██▀██▌███▀▀▀████
                        ▒▒▐▀████▌▀██▌▀▐█▌████▌█████▌
                        ▒▒█▒▒▀██▀▀▐█▐█▌█▌▀▀██▌██████
                        ▒▒█▒▒▒▒████████████████████▌
                        ▒▒▒▌▒▒▒▒█████░░░░░░░██████▀
                        ▒▒▒▀▄▓▓▓▒███░░░░░░█████▀▀
                        ▒▒▒▒▀░▓▓▒▐█████████▀▀▒
                        ▒▒▒▒▒░░▒▒▐█████▀▀▒▒▒▒▒▒
                        ▒▒░░░░░▀▀▀▀▀▀▒▒▒▒▒▒▒▒▒
                        ▒▒▒░░░░░░░░▒▒                                          """)
    print("\n-----------------------------------------------------------------------")
    print("-----------------------------------------------------------------------")
    print("-----------------------------------------------------------------------")
    print_slow(">Returning To The Titlescreen")
    print_superslow("......")
    print("")
    titlescreen()

def Win(): #FUNCTION IF THE PLAYER WINS BY HITTING A '$' ON THE MAP.
    print("")
    os.system('cls')
    print("[YOU]")
    print_slower("*You have returned home with your honey after defeating the ninjas... you feel a bit tired... you decide to sleep!*")
    print_slower("   ")
    print("\n[UNKNOWN VOICE]")
    print_slower(""" "MR. BEAR WAKE UP!!" """)
    print("\n[YOU]")
    print_slower("*Still sleeping*")
    print("\n[UNKNOWN VOICE]")
    print_slower(""" "MR. BEAR THIS IS SERIOUS!!!" """)
    print("\n[YOU]")
    print_slower("*Still sleeping*")
    print_slower("   ")
    print("\n[UNKNOWN VOICE]")
    print_slower(""" "I have honey..." """)
    print("\n[YOU]")
    print_slower("*You awake for the honey...*")
    print_slower("   ")
    print("\n[FOX FRANK]")
    print_slower(""" "Ben Bear... I have bad news I don't actually have honey... NINJAS STOLE IT AGAIN........." """)
    print("\n[YOU]")
    print_slower(""" "Sounds like Mark has to program and design HONEY QUEST [TWO]!" """)
    print_slower("   ")
    print_slow("""
  _____   _                       _              _____                
 |_   _| | |__     __ _   _ __   | | __  ___    |  ___|   ___    _ __ 
   | |   | '_ \   / _` | | '_ \  | |/ / / __|   | |_     / _ \  | '__|
   | |   | | | | | (_| | | | | | |   <  \__ \   |  _|   | (_) | | |   
   |_|   |_| |_|  \__,_| |_| |_| |_|\_\ |___/   |_|      \___/  |_|
  ____    _                   _                     _   _   _ 
 |  _ \  | |   __ _   _   _  (_)  _ __     __ _    | | | | | |
 | |_) | | |  / _` | | | | | | | | '_ \   / _` |   | | | | | |
 |  __/  | | | (_| | | |_| | | | | | | | | (_| |   |_| |_| |_|
 |_|     |_|  \__,_|  \__, | |_| |_| |_|  \__, |   (_) (_) (_)
                      |___/               |___/               
""")
    print("\n>To return to the mainmenu type 'Y', else enter any other key to exit HONEY QUEST [ONE]!")
    leave = input("UserConsole>")
    leave = leave.upper()
    if leave == "Y":
        print_slow(">Returning To The Titlescreen")
        print_superslow("......")
        print("")
        titlescreen()
    else:
        print_slower("\n>Thanks for playing!")
        print_superslow("...")
        sys.exit()

# REMOVE "#" TO CHECK EACH FUNCTION

#Battle()
#Game_Over()
#Win()
titlescreen()
#help_menu()
#help_menu_ingame()
#help_menu_inbattle()
#Print_Map()
#start_game()
        
        


    
