"""
Turn-based game against the computer
User & computer have 3 moves (2 damage + 1 heal), computer more likely to heal at low HP
After each move, a message should be printed out that tells the user what just happened, and how much health the user and computer have. Once the user or the computer's health reaches 0, the game should end.

SUBGOALS
Make user/computer different classes with HP and move variables
When someone is defeated, make sure the game prints out that their health has reached 0, and not a negative number.
When the computer's health reaches a set amount (such as 35%), increase it's chance to cast heal.
Give each move a name.
"""
import sys
from random import randint
from time import sleep
# both user and computer start with 100 HP
user_hp = 100
computer_hp = 100


# for showing HP of both computer and user
def show_status():
    global user_hp, computer_hp
    if computer_hp > 0 and user_hp > 0:
        print("\nCurrent status:\nUser HP: %s\nComputer HP: %s\n" % (user_hp, computer_hp))
    elif computer_hp <= 0:
        computer_hp = 0
        print("Congratulations! The computer has %d hit points left. You won!" % computer_hp)
        replay_game = input("Play again? Y for yes, N for no: ")
        replay_game = replay_game.lower()
        if replay_game == 'y':
            play_game()
        else:
            print("Take care! Exiting...")
            sleep(2)
            sys.exit()
    elif user_hp <= 0:
        user_hp = 0
        print("Oh no! You have %d hit points left. You fainted :( Better luck next time!" % user_hp)
        replay_game = input("Play again? Y for yes, N for no: ")
        replay_game = replay_game.lower()
        if replay_game == 'y':
            play_game()
        else:
            print("Take care! Exiting...")
            sleep(2)
            sys.exit()


# for executing a hit/heal for user
def user_moves():
    global user_hp, computer_hp
    user_move_headbutt = randint(18, 25)  # low range, moderate damage
    user_move_kamehameha = randint(10, 35)  # high range, high damage (can also be very low)
    user_move_potion = randint(18, 25)
    print("What move would you like to use?")
    print("1 - Headbutt (low range of damage)")
    print("2 - Kamehameha (high range of damage)")
    print("3 - Drink Potion (heal)")
    user_move_choice = input("> ")
    if user_move_choice == '1':
        print("You used Headbutt! It did %d damage!" % user_move_headbutt)
        computer_hp -= user_move_headbutt
        show_status()
        computer_moves()
    elif user_move_choice == '2':
        print("You used Kamehameha! It did %d damage!" % user_move_kamehameha)
        computer_hp -= user_move_kamehameha
        show_status()
        computer_moves()
    elif user_move_choice == '3':
        print("You used a potion! You gained %d health." % user_move_potion)
        user_hp += user_move_potion
        show_status()
        computer_moves()
    else:
        print("Invalid input. Try again.")
        user_moves()


# for figuring out what move computer will use
def computer_moves():
    global user_hp, computer_hp
    print("Computer is thinking...")
    sleep(1)
    comp_move_calc = randint(1, 100)
    comp_move_punch = randint(18, 25)
    comp_move_hadoken = randint(10, 35)
    comp_move_heal = randint(18, 25)
    # if comp HP is under 35%, the probability it uses heal goes up to 60%
    if computer_hp > 35:  # 30% chance to use light hit, 30% chance for other hit, 40% chance to heal
        if comp_move_calc in range(1, 30):
            print("Computer used Punch! It did %d damage." % comp_move_punch)
            user_hp -= comp_move_punch
            show_status()
            user_moves()
        elif comp_move_calc in range(31, 60):
            print("Computer used Hadoken! It did %d damage." % comp_move_hadoken)
            user_hp -= comp_move_hadoken
            show_status()
            user_moves()
        else:
            print("Computer healed! It gained %d health." % comp_move_heal)
            computer_hp += comp_move_heal
            show_status()
            user_moves()
    elif 0 < computer_hp <= 35:  # if on low hp, chance to heal goes up to 60%
        if comp_move_calc in range(1, 20):
            print("Computer used punch! It did %d damage." % comp_move_punch)
            user_hp -= comp_move_punch
            show_status()
            user_moves()
        elif comp_move_calc in range(21, 40):
            print("Computer used Hadoken! It did %d damage." % comp_move_hadoken)
            user_hp -= comp_move_hadoken
            show_status()
            user_moves()
        else:
            print("Computer healed! It gained %d health." % comp_move_heal)
            computer_hp += comp_move_heal
            show_status()
            user_moves()


def play_game():
    user_moves()
    computer_moves()


print("Welcome! Rules are simple:\nTurn-based, you go first.\nYou and the computer both have 2 damage abilities and"
      " a heal.\nFirst person to 0 hit points loses! You both start at 100.\nBe careful, the computer has a higher"
      " chance to heal at lower1 hit points than at higher! Good luck :)")
play_game()

