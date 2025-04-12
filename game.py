# game.py
import time
from helpers import printHand, points, random_card
from actions import hit, stand, double, bust, blackjack, dealer_strategy
from actions import isPair  # if needed for splits
from strategy import properStrategy, strat2command, pasttenseify

# Globals to track overall record
wins = 0
losses = 0
pushes = 0
money = 500

def recordAndBalance():
    """
    Print the overall record and current balance.
    """
    time.sleep(1)
    print(f"\nRecord: {wins}-{losses}-{pushes}")
    print(f"Balance: {money}\n")

def firstCard(hand):
    return [hand[0]]

def secondCard(hand):
    return [hand[1]]

def evaluate_winner(player_hand, dealer_hand, bet):
    """
    Compare the final points and update global wins/losses/pushes.
    """
    global wins, losses, pushes, money
    dealer_pts = points(dealer_hand)
    player_pts = points(player_hand)

    if bust(dealer_hand):
        time.sleep(1)
        print("\nDealer busted!")
        wins += 1
        money += bet
    else:
        time.sleep(1)
        if player_pts > dealer_pts:
            print(f"\n{player_pts} beats {dealer_pts}. You win!")
            wins += 1
            money += bet
        elif dealer_pts > player_pts:
            print(f"\n{dealer_pts} beats {player_pts}. You lose :(")
            losses += 1
            money -= bet
        else:
            print(f"\nYou both got {dealer_pts}. It's a tie!")
            pushes += 1

def playGame(bet):
    """
    Deal initial cards and check immediate blackjack conditions.
    Return True if we should continue playing the hand, False if
    the hand ended immediately (e.g. immediate blackjack).
    """
    global wins, losses, pushes, money

    # Deal dealer upcard
    dealer_hand = [random_card()]
    print("\nDealer shows: " + printHand(dealer_hand))

    # Deal player's hand
    player_hand = [random_card(), random_card()]
    print("You have: " + printHand(player_hand) + "\n")

    # Check if player has blackjack
    if blackjack(player_hand):
        print("You got blackjack!")
        wins += 1
        # typical blackjack pays 3:2. If we only add bet*1.5,
        # it means net profit is +1.5 * bet. 
        money += bet * 1.5
        return False, player_hand, dealer_hand

    return True, player_hand, dealer_hand

def playing(player_hand, dealer_upcard, bet):
    """
    Let the player act: 'hit', 'stand', 'double', or 'split'.
    Return the final action string or False if they bust.
    """
    global wins, losses, money

    correct_letter = properStrategy(player_hand, dealer_upcard)
    correct_cmd = strat2command(correct_letter)

    while True:
        action = input("What would you like to do? (hit/stand/double/split)  ").lower()

        if action == 'stand':
            # If the correct strategy was stand and we did stand => "You have stood"
            if correct_cmd != 'stand':
                print(f"\nWrong! Here you should have {pasttenseify(correct_cmd)}.")
            return 'stand'

        elif action == 'hit':
            if correct_cmd != 'hit':
                print(f"\nWrong! Here you should have {pasttenseify(correct_cmd)}.")
            hit(player_hand)
            time.sleep(1)
            print("\nYou have: " + printHand(player_hand) + "\n")
            if bust(player_hand):
                print("You busted!")
                losses += 1
                money -= bet
                return False  # signals the player busted

        elif action == 'double':
            if correct_cmd != 'double':
                print(f"\nWrong! Here you should have {pasttenseify(correct_cmd)}.")
            double(player_hand)
            print("\nYou have: " + printHand(player_hand) + "\n")
            if bust(player_hand):
                print("You busted!")
                losses += 1
                money -= (bet * 2)
                return False
            return 'double'  # done after one double

        elif action == 'split':
            if correct_cmd != 'split':
                print(f"\nWrong! Here you should have {pasttenseify(correct_cmd)}.")

            # Must check if actually a pair
            if not isPair(player_hand):
                print("\nYou cannot split a non-pair.")
                continue

            # Split into two separate 1-card hands
            split_hand_1 = [player_hand[0]]
            split_hand_2 = [player_hand[1]]
            print(f"\nSplit! First hand: {printHand(split_hand_1)}")
            final_1 = playing(split_hand_1, dealer_upcard, bet)
            
            print(f"\nSecond hand: {printHand(split_hand_2)}")
            final_2 = playing(split_hand_2, dealer_upcard, bet)
            
            # Return 'split' but we've basically forced the user to play each hand
            return 'split'

        else:
            print("Invalid action. Please type hit, stand, double, or split.")

def ask_for_bet():
    # Take a bet
    try:
        bet_str = input("How much would you like to bet?  ")
        bet = float(bet_str) if '.' in bet_str else int(bet_str)
    except ValueError:
        print("Invalid bet. Try Again")
        bet = ask_for_bet()
    return bet

def main():
    global wins, losses, pushes, money

    print("\n########################################################")
    print("Welcome to MAXJACK.")
    print("Press Enter to begin!")
    response = input()

    # Main loop
    while response == '':
        recordAndBalance()

        bet = ask_for_bet()            

        # Play a single game/hand
        continue_game, my_hand, dealer_hand = playGame(bet)
        if not continue_game:
            # That means immediate blackjack or something ended
            continue
        dealer_upcard = dealer_hand[0]  # the shown card

        # Player interacts
        final_action = playing(my_hand, dealer_upcard, bet)
        if final_action:
            # If user didn't bust
            # Dealer "effectively" gets a second card
            from actions import hit, bust, blackjack
            dealer_hand = hit(dealer_hand)  # Flip dealer's hole card
            print("\nDealer has: " + printHand(dealer_hand))

            # Check if dealer has blackjack
            if blackjack(dealer_hand):
                print("\nDealer has blackjack!")
                losses += 1
                money -= bet
                continue

            # Let dealer finish
            dealer_hand = dealer_strategy(dealer_hand)

            # If the player doubled, bet is effectively x2
            if final_action == 'double':
                bet *= 2

            # Evaluate winner
            # If the player *split*, we actually already handled each hand.
            # But as written, we only handle 1 "my_hand" here. 
            # Real multi-hand logic would handle each splitted hand separately.
            if final_action != 'split':
                evaluate_winner(my_hand, dealer_hand, bet)

def test():
    dealer_upcard = 'K'
    player_hand = ['4', '4', '9']
    print(properStrategy(player_hand, dealer_upcard))

if __name__ == "__main__":
    # test()
    main()
