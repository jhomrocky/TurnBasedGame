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

from random import randint
# both user and computer start with 100 HP
user_hp = 100
computer_hp = 100



# for showing HP of both computer and user
def show_status():
    print("Current status:\nUser HP: %s\nComputer HP: %s" % (user_hp, computer_hp))

# for executing a hit/heal for user
def user_moves():


# for figuring out what move computer will use
def computer_move():
    global user_hp, computer_hp
# make sure to include if hp < 35% (or something) then up the probability to heal
    comp_move_calc = randint(1, 100)
    comp_light_hit_dmg = randint(18-25) # low range, moderate damage
    comp_heavy_hit_dmg = randint(10-35) # high range, high damage (can also be very low)
    comp_heal_amount = randint(18-25)
    # moves if comp hp > 35%
    if computer_hp > 35:
        # 30% chance to use light hit, 30% chance for other hit, 40% chance to heal
        if comp_move_calc in range(1,30):
            user_hp -= comp_light_hit_dmg
        elif comp_move_calc in range(31,60):
            user_hp -= comp_heavy_hit_dmg
        else:
            computer_hp += comp_heal_amount
    elif 0 < computer_hp < 35:
        if comp_move_calc in range(1, 20):
            user_hp -= comp_light_hit_dmg
        elif comp_move_calc in range(21, 40):
            user_hp -= comp_heavy_hit_dmg
        else:
            computer_hp += comp_heal_amount





