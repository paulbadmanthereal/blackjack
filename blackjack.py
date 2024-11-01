import random

# Card values
card_values = {
    'Ace': 11,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    '10': 10,
    'Jack': 10,
    'Queen': 10,
    'King': 10
}

# Function to calculate the total value of a hand
def calculate_hand_value(hand):
    total = sum(card_values[card] for card in hand)
    if 'Ace' in hand and total > 21:
        total -= 10
    return total

# Function to play a game of Blackjack
def play_blackjack():
    deck = list(card_values.keys()) * 4
    random.shuffle(deck)
    print("Welcome to Python Blackjack!")
    print("the creator's github is at htpps://github.com/paulbadmanthereal")

    player_hand = []
    dealer_hand = []

    # Deal initial cards
    player_hand.append(deck.pop())
    dealer_hand.append(deck.pop())
    player_hand.append(deck.pop())
    dealer_hand.append(deck.pop())

    # Player's turn
    while True:
        print(f"Your hand: {player_hand}")
        print(f"Dealer's upcard: {dealer_hand[0]}")

        choice = input("Do you want to hit or stand? ").lower()
        if choice == 'hit':
            player_hand.append(deck.pop())
            player_total = calculate_hand_value(player_hand)
            if player_total > 21:
                print(f"Your hand: {player_hand}")
                print("Bust! You lose.")
                return
        elif choice == 'stand':
            break
        else:
            print("Invalid choice. Please enter 'hit' or 'stand'.")

    # Dealer's turn
    dealer_total = calculate_hand_value(dealer_hand)
    while dealer_total < 17:
        dealer_hand.append(deck.pop())
        dealer_total = calculate_hand_value(dealer_hand)

    # Determine the winner
    player_total = calculate_hand_value(player_hand)
    print(f"Your hand: {player_hand}")
    print(f"Dealer's hand: {dealer_hand}")
    if dealer_total > 21:
        print("Dealer busts! You win.")
    elif player_total > dealer_total:
        print("You win!")
        print("Thanks for playing.")
    elif player_total < dealer_total:
        print("Dealer wins!")
        print("Thanks for playing.")
    else:
        print("It's a tie!")
        print("Thanks for playing.")

# Start the game
while True:
    play_blackjack()
    play_again = input("Do you want to play again? (yes/no) ").lower()
    if play_again != 'yes':
        break