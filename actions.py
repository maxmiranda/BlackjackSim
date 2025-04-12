# actions.py
import time
from helpers import random_card, points, printHand, is_soft

def hit(hand):
    """
    Adds a random card to the hand (in-place) and returns it.
    """
    hand.append(random_card())
    return hand

def stand(hand):
    """
    Technically does nothing to the hand, but we include it for clarity.
    """
    return hand

def double(hand):
    """
    Equivalent to hitting once but doubling your bet,
    so you usually only get one extra card.
    """
    return hit(hand)

def bust(hand):
    return points(hand) > 21

def blackjack(hand):
    return (points(hand) == 21 and len(hand) == 2)

def isPair(hand):
    """
    Returns True if exactly 2 cards of the same rank (by points).
    (E.g. J, Q, K, 10 are all 10-valued, so that's considered a pair.)
    """
    if len(hand) == 2:
        val_first = points([hand[0]])
        val_second = points([hand[1]])
        if val_first == val_second:
            return True
    return False

def dealer_strategy(dealer_hand):
    """
    Dealer hits on soft 17.
    """
    while points(dealer_hand) < 17 or (points(dealer_hand) == 17 and is_soft(dealer_hand)):
        hit(dealer_hand)
        time.sleep(1)
        print("\nDealer hits: " + printHand(dealer_hand))
    return dealer_hand
