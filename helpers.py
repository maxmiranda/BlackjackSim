# helpers.py
from cards_data import cards, card_vals
import numpy as np

def index(card, running_total):
    """
    Returns the index in card_vals that should be used for the given card,
    depending on the current running_total (mainly to handle Ace as 1 or 11).
    """
    if card == 'A':
        # If counting Ace as 11 busts, use 1 instead
        if running_total + 11 > 21:
            return 0  # card_vals[0] = 1
        else:
            return 13 # card_vals[13] = 11
    else:
        for i, c in enumerate(cards):
            if card == c:
                return i
    raise ValueError(f"Invalid card: {card}")


def organize(hand):
    """
    If there's an Ace in the hand, move it to the end
    so that points() logic can easily handle 1 or 11.
    """
    # Just put all Aces at the end:
    sorted_hand = sorted(hand, key=lambda x: (x == 'A', x))
    return sorted_hand


def points(hand):
    """
    Returns the total point value of a hand (list of card strings).
    """
    total = 0
    # Move Aces to the end so we can handle them last
    ordered_hand = organize(hand[:])  # copy so we don't mutate original
    for card in ordered_hand:
        total += card_vals[index(card, total)]
    return total


def random_card():
    return np.random.choice(cards)


def printHand(hand):
    return " ".join(str(c) for c in hand)

def is_soft(hand):
    # Returns True if the hand contains at least one Ace counted as 11.
    # i.e., if total < (points without that Ace as 11).
    # Or more simply: after reorganizing, check if adding 10 would not bust.
    
    # One approach:
    return 'A' in hand and points(hand) < (points(hand) + 10) <= 21
