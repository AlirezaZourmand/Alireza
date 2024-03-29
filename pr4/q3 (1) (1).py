# -*- coding: utf-8 -*-
"""Card Game

Automatically generated by Colaboratory.
Original file is located at
https://colab.research.google.com/drive/1Qae81InDMn5k4x_eoTSzChiRhbxG9X5Y
"""

# Initialize scores and score lists
player1_score = 0
player2_score = 0
player1_score_list = []
player2_score_list = []

# Define function to create a dictionary from list of numbers
def create_card_dictionary(numbers):
    if len(numbers) != 3:
        raise ValueError("Invalid Command.")
    return {"A": numbers[0], "B": numbers[1], "C": numbers[2]}

# Define function to play the card game
def play_game(player1, player2, health1, health2, cards, rounds):
    for _ in range(rounds):
        card1, card2 = input("Enter your cards for this round: ").split()
        damage1 = cards[card1]
        damage2 = cards[card2]
        health1 -= damage1
        health2 -= damage2
        if damage1 > damage2:
            player1_score += 1
        elif damage2 > damage1:
            player2_score += 1
        player1_score_list.append(player1_score)
        player2_score_list.append(player2_score)

# Get input and start playing the game
try:
    player1, player2 = input("Enter player names: ").split()
    player1_health, player2_health = map(int, input("Enter player health points: ").split())
    card_damage = create_card_dictionary(list(map(int, input("Enter card damages: ").split())))
    play_game(player1, player2, player1_health, player2_health, card_damage, 3)
except Exception as e:
    print("Invalid Command.")
