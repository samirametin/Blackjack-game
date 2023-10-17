from random import randint

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
computer_cards = []
players_cards = []


def deal_card():
    i = randint(0, 13)
    chosen_card = cards[i]
    return chosen_card


def calculating_score(arr):
    return sum(arr)


players_cards.append(deal_card())
players_cards.append(deal_card())
p_score = calculating_score(players_cards)
print(f"Your cards: {players_cards}, current score: {p_score}")
