# slot_machine.py

import random

def spin():
    symbols = ['🍒', '🍒', '🍒', '🍊', '🍊', '🍇', '🍇', '🔔', '7️⃣', '🌟']
    return random.choice(symbols)

def play_slot_machine():
    print("Welcome to the Python Slot Machine!")
    coins = 1000

    while True:
        print(f"You have {coins} coins.")
        bet = int(input("Enter your bet (0 to quit): "))
        
        if bet == 0:
            break
            print("You ended the game with {coins} coins.")
            print("Thank you for playing!")
            print("the creator's github is at htpps://github.com/paulbadmanthereal")
        elif bet > coins:
            print("Insufficient coins. Please enter a valid bet.")
            continue
        
        input("Press Enter to spin the reels...")
        reel1 = spin()
        reel2 = spin()
        reel3 = spin()
        print(f"{reel1} | {reel2} | {reel3}")
        
        if reel1 == reel2 == reel3 == '🌟':
            print("Jackpot! You win 1000 times your bet!")
            coins += bet * 1000
        elif reel1 == reel2 == reel3:
            print("Three symbols match! You win 10 times your bet!")
            coins += bet * 10
        elif reel1 == reel2 or reel1 == reel3 or reel2 == reel3:
            print("Two symbols match! You win twice your bet!")
            coins += bet * 2
        else:
            print("No match. You lose your bet.")
            coins -= bet
        
        if coins == 0:
            print("You've run out of coins. Game over!")
            break
    
    print(f"You ended the game with {coins} coins.")
    print("Thank you for playing!")
    print("the creator's github is at htpps://github.com/paulbadmanthereal")

if __name__ == "__main__":
    play_slot_machine()