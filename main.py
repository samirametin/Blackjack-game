from random import choices

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
computer_cards = []
players_cards = []


def deal_card(num):
    return choices(cards, k=num)


def calculating_score(arr):
    return sum(arr)


players_cards = deal_card(2)
computer_cards = deal_card(2)
if 11 in computer_cards and 10 in computer_cards:
    print("Computer wins.")
elif 11 in players_cards and 10 in players_cards:
    print("Player wins. ")
p_score = calculating_score(players_cards)
c_score = calculating_score(computer_cards)
print(f"Your cards: {players_cards}, current score: {p_score}")
print(f"Computer's first card: {computer_cards[0]}")
should_pass = input("Type 'y' to get another card, type 'n' to pass. ")
if should_pass == "n":
    if p_score > c_score:
        print("Computer went over. Computer lose.")
    elif p_score < c_score:
        print("You went over. You lose.")
    else:
        print("It is draw.")
elif should_pass == "y":
    players_cards += deal_card(1)
