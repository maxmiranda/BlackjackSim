# strategy.py
from helpers import points
from actions import isPair
from cards_data import rules

def properStrategy(my_hand, dealer_upcard):
    """
    Returns the correct strategy letter (H, S, D, P) for your hand
    based on classic strategy in 'rules'.
    """
    # Build a lookup key like 'S17', '17', 'Pair8', etc.
    total = points(my_hand)
    your_hand_key = ""

    # Check if there's an Ace => soft total
    # (Naive approach: if there's at least one Ace, treat it as 'S')
    if 'A' in my_hand:
        your_hand_key += "S"

    # Check if it's a pair
    if isPair(my_hand):
        your_hand_key += "Pair"

    # Edge case: specifically two Aces => 'PairA'
    if my_hand == ['A', 'A']:
        your_hand_key = "PairA"
    else:
        # Now append total => e.g. "S18" or "16" or "Pair6"
        your_hand_key += str(total)

    # Convert the dealer upcard to index: 2..9 => 0..7, 10 => 8, Ace => 9
    if dealer_upcard in ['J', 'Q', 'K']:
        col_idx = 8  # same as 10
    elif dealer_upcard == 'A':
        col_idx = 9
    else:
        # e.g. '4' => int(4) - 2 = 2
        col_idx = int(dealer_upcard) - 2

    return rules[your_hand_key][col_idx]


def strat2command(strategy_letter):
    """
    Translate the single-letter strategy from the dictionary
    into a string command like 'hit', 'stand', 'double', or 'split'.
    """
    mapping = {
        'H': 'hit',
        'S': 'stand',
        'D': 'double',
        'P': 'split'
    }
    return mapping.get(strategy_letter, 'hit')  # default to 'hit'


def pasttenseify(verb):
    if verb == 'stand':
        return 'stood'
    elif verb == 'double':
        return 'doubled'
    elif verb == 'hit':
        return 'hit'
    elif verb == 'split':
        return 'split'
    return verb
