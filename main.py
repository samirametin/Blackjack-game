from random import choices

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
computer_cards = []
players_cards = []


def deal_card(num):
    return choices(cards, k=num)


def calculating_score(arr):
    return sum(arr)


def ending(p_score, c_score):
    print(f"Your final hand: {players_cards}, final score: {p_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {c_score}")
    if p_score > c_score:
        print("Computer went over. Computer lose.")
    elif p_score < c_score:
        print("You went over. You lose.")
    else:
        print("It is draw.")


players_cards = deal_card(2)
computer_cards = deal_card(2)
p_score = calculating_score(players_cards)
c_score = calculating_score(computer_cards)
if 11 in computer_cards and 10 in computer_cards:
    print(f"Computers final hand is {computer_cards}. Computer wins.")
elif 11 in players_cards and 10 in players_cards:
    print(f"Players final hand is {players_cards}. Player wins. ")
print(f"Your cards: {players_cards}, current score: {p_score}")
print(f"Computer's first card: {computer_cards[0]}")
should_pass = input("Type 'y' to get another card, type 'n' to pass. ")
if should_pass == "n":
    ending(p_score, c_score)
elif should_pass == "y":
    players_cards += deal_card(1)
    p_score = calculating_score(players_cards)
    c_score = calculating_score(computer_cards)
    print(f"Your cards: {players_cards}, current score: {p_score}")
    print(f"Computer's first card: {computer_cards[0]}")
    ending(p_score, c_score)
