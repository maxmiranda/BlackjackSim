# cards_data.py

cards = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

# The 14-element card_vals array is intentional so that index(card, total)
# can return 0 (count Ace as 1) or 13 (count Ace as 11). The other non-Ace
# cards map directly (2 -> index 1 => value 2, J -> index 10 => value 10, etc.)
card_vals = [
    1,  # index 0 (used for Ace as 1)
    2,  # index 1
    3,  # index 2
    4,  # index 3
    5,  # index 4
    6,  # index 5
    7,  # index 6
    8,  # index 7
    9,  # index 8
    10, # index 9  (10)
    10, # index 10 (J)
    10, # index 11 (Q)
    10, # index 12 (K)
    11  # index 13 (Ace as 11)
]

rules = {
    #
    # HARD TOTALS (keys "8" through "20")
    #
    "2" :  ["H","H","H","H","H","H","H","H","H","H"],         # Always Hit
    "3" :  ["H","H","H","H","H","H","H","H","H","H"],         # Always Hit
    "4" :  ["H","H","H","H","H","H","H","H","H","H"],         # Always Hit
    "5" :  ["H","H","H","H","H","H","H","H","H","H"],         # Always Hit
    "6" :  ["H","H","H","H","H","H","H","H","H","H"],         # Always Hit
    "7" :  ["H","H","H","H","H","H","H","H","H","H"],         # Always Hit
    "8" :  ["H","H","H","H","H","H","H","H","H","H"],         # Always Hit
    "9" :  ["H","D","D","D","D","H","H","H","H","H"],         # Double vs 3..6
    "10":  ["D","D","D","D","D","D","D","D","H","H"],         # Double vs 2..9
    "11":  ["D","D","D","D","D","D","D","D","D","D"],         # Always Double
    "12":  ["H","H","S","S","S","H","H","H","H","H"],         # Stand vs 4..6, else Hit
    "13":  ["S","S","S","S","S","H","H","H","H","H"],         # Stand vs 2..6, else Hit
    "14":  ["S","S","S","S","S","H","H","H","H","H"],
    "15":  ["S","S","S","S","S","H","H","H","H","H"],
    "16":  ["S","S","S","S","S","H","H","H","H","H"],
    "17":  ["S","S","S","S","S","S","S","S","S","S"],         # Always Stand
    "18":  ["S","S","S","S","S","S","S","S","S","S"],         # ...
    "19":  ["S","S","S","S","S","S","S","S","S","S"],
    "20":  ["S","S","S","S","S","S","S","S","S","S"],

    #
    # SOFT TOTALS (keys "S13" through "S20", i.e. Ace+2 => "S13", up to Ace+9 => "S20")
    #
    "S13": ["H","H","H","D","D","H","H","H","H","H"],         # A,2
    "S14": ["H","H","D","D","D","H","H","H","H","H"],         # A,3
    "S15": ["H","H","D","D","D","H","H","H","H","H"],         # A,4
    "S16": ["H","H","D","D","D","H","H","H","H","H"],         # A,5
    "S17": ["D","D","D","D","D","H","H","H","H","H"],         # A,6
    # A,7 => Double vs 2..6, Stand vs 7..8, Hit vs 9..A
    "S18": ["D","D","D","D","D","S","S","H","H","H"],
    # A,8 => Double vs 6, else Stand
    "S19": ["S","S","S","S","D","S","S","S","S","S"],
    # A,9 => Always Stand
    "S20": ["S","S","S","S","S","S","S","S","S","S"],

    #
    # PAIRS (keys like "Pair4" for 2,2 up to "PairA" for A,A)
    #
    # 2,2 => split vs 2..7
    "Pair4":  ["P","P","P","P","P","P","H","H","H","H"],
    # 3,3 => split vs 2..7
    "Pair6":  ["P","P","P","P","P","P","H","H","H","H"],
    # 4,4 => split vs 5..6 if DAS (assume yes)
    "Pair8":  ["H","H","H","P","P","H","H","H","H","H"],
    # 5,5 => never truly “split,” treat as hard 10 => double vs 2..9
    "Pair10": ["D","D","D","D","D","D","D","D","H","H"],
    # 6,6 => split vs 2..6
    "Pair12": ["P","P","P","P","P","H","H","H","H","H"],
    # 7,7 => split vs 2..7, else hit
    "Pair14": ["P","P","P","P","P","P","H","H","H","H"],
    # 8,8 => always split
    "Pair16": ["P","P","P","P","P","P","P","P","P","P"],
    # 9,9 => split vs 2..6 & 8..9; stand vs 7,10,A
    "Pair18": ["P","P","P","P","P","S","P","P","S","S"],
    # 10,10 (or any T,T/J,J/Q,Q/K,K => total 20) => never split
    "Pair20": ["S","S","S","S","S","S","S","S","S","S"],
    # A,A => always split
    "PairA":  ["P","P","P","P","P","P","P","P","P","P"]
}
