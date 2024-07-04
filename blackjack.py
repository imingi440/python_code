import random

# 카드 덱 생성
suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}

deck = [(rank, suit) for rank in ranks for suit in suits]

def deal_card(deck):
    card = random.choice(deck)
    deck.remove(card)
    return card

def calculate_hand_value(hand):
    value = sum(values[card[0]] for card in hand)
    num_aces = sum(1 for card in hand if card[0] == 'Ace')
    while value > 21 and num_aces:
        value -= 10
        num_aces -= 1
    return value

def display_hand(hand, name):
    hand_value = calculate_hand_value(hand)
    hand_description = ', '.join([f"{rank} of {suit}" for rank, suit in hand])
    print(f"{name}'s hand ({hand_value}): " + hand_description)

def blackjack():
    random.shuffle(deck)
    player_hand = [deal_card(deck), deal_card(deck)]
    dealer_hand = [deal_card(deck), deal_card(deck)]

    display_hand(player_hand, "Player")
    display_hand(dealer_hand[:1], "Dealer")

    while calculate_hand_value(player_hand) < 21:
        action = input("Do you want to hit or stand? (h/s): ")
        if action.lower() == 'h':
            player_hand.append(deal_card(deck))
            display_hand(player_hand, "Player")
        else:
            break

    player_value = calculate_hand_value(player_hand)
    dealer_value = calculate_hand_value(dealer_hand)

    if player_value > 21:
        print("Player busts! Dealer wins.")
        return

    print("\nDealer's turn...")
    display_hand(dealer_hand, "Dealer")
    while dealer_value < 17:
        dealer_hand.append(deal_card(deck))
        dealer_value = calculate_hand_value(dealer_hand)
        display_hand(dealer_hand, "Dealer")

    if dealer_value > 21 or player_value > dealer_value:
        print("Player wins!")
    elif player_value < dealer_value:
        print("Dealer wins!")
    else:
        print("It's a tie!")

if __name__ == "__main__":
    blackjack()
