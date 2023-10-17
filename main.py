from random import choises

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
computer_cards = []
players_cards = []


def deal_card():
    list = choises(cards, k=2)


def calculating_score(arr):
    return sum(arr)


players_cards = deal_card()
computer_cards = deal_card()
p_score = calculating_score(players_cards)
c_score = calculating_score(computer_cards)
print(f"Your cards: {players_cards}, current score: {p_score}")
print(f"Computer's first card: {computer_cards[0]}")
