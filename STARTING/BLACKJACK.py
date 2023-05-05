import random


def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


is_game_over = False

user_cards = []
computer_cards = []
deal_card()

for c in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())
print(user_cards)
print(computer_cards)


def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)


while not is_game_over:
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
    print(f"Your cards are {user_cards} and your current score is {user_score}")
    print(f"computer's first card is {computer_cards[0]}")
    if user_score == 0 or computer_score == 0 or user_score > 21:
        is_game_over = True

    else:
        draw = input('Type y to draw another card otherwise type n')
        if draw == 'y':
            user_cards.append(deal_card())
        else:
            is_game_over = True
            if 21 > user_score > computer_score:
                print()
