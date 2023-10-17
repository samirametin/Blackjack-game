from random import choice

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
computer_cards = []
players_cards = []
is_game_over = False


def deal_card():
    card = choice(cards)
    return card


def calculating_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if sum(cards) > 21 and 11 in cards:
        cards.remove(11)
        cards.append(1)
    return sum(cards)


def ending(p_score, c_score):
    print(f"Your final hand: {players_cards}, final score: {p_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {c_score}")
    if p_score > c_score:
        print("Computer went over. Computer lose.")
    elif p_score < c_score:
        print("You went over. You lose.")
    else:
        print("It is draw.")


for _ in range(2):
    computer_cards.append(deal_card())
    players_cards.append(deal_card())

p_score = calculating_score(players_cards)
c_score = calculating_score(computer_cards)

if p_score == 0 or c_score == 0 or p_score > 21:
    is_game_over = True


p_score = calculating_score(players_cards)
c_score = calculating_score(computer_cards)
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
