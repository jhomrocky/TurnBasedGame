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

