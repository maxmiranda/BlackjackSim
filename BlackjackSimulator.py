import numpy as np
import time

cards = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
card_vals = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]
rules = {# 2	3	4	5	6	7	8	9	10	A
'2':	['H',	'H',	'H',	'H',	'H',	'H',	'H',	'H',	'H',	'H'],
'3':	['H',	'H',	'H',	'H',	'H',	'H',	'H',	'H',	'H',	'H'],
'4':	['H',	'H',	'H',	'H',	'H',	'H',	'H',	'H',	'H',	'H'],
'5':	['H',	'H',	'H',	'H',	'H',	'H',	'H',	'H',	'H',	'H'],
'6':	['H',	'H',	'H',	'H',	'H',	'H',	'H',	'H',	'H',	'H'],
'7':	['H',	'H',	'H',	'H',	'H',	'H',	'H',	'H',	'H',	'H'],
'8':	['H',	'H',	'H',	'H',	'H',	'H',	'H',	'H',	'H',	'H'],
'9':	['H',	'D',	'D',	'D',	'D',	'H',	'H',	'H',	'H',	'H'],
'10':	['D',	'D',	'D',	'D',	'D',	'D',	'D',	'D',	'H',	'H'],
'11':	['D',	'D',	'D',	'D',	'D',	'D',	'D',	'D',	'D',	'H'],
'12':	['H',	'H',	'S',	'S',	'S',	'H',	'H',	'H',	'H',	'H'],
'13':	['S',	'S',	'S',	'S',	'S',	'H',	'H',	'H',	'H',	'H'],
'14':	['S',	'S',	'S',	'S',	'S',	'H',	'H',	'H',	'H',	'H'],
'15':	['S',	'S',	'S',	'S',	'S',	'H',	'H',	'H',	'H',	'H'],
'16':	['S',	'S',	'S',	'S',	'S',	'H',	'H',	'H',	'H',	'H'],
'17':	['S',	'S',	'S',	'S',	'S',	'S',	'S',	'S',	'S',	'S'],
'18':	['H',	'H',	'H',	'H',	'H',	'H',	'H',	'H',	'H',	'H'],
'19':	['H',	'H',	'H',	'H',	'H',	'H',	'H',	'H',	'H',	'H'],
'20':	['H',	'H',	'H',	'H',	'H',	'H',	'H',	'H',	'H',	'H'],
'S13': ['H',	'H',	'H',	'D',	'D',	'H',	'H',	'H',	'H',	'H'],
'S14':	['H',	'H',	'H',	'D',	'D',	'H',	'H',	'H',	'H',	'H'],
'S15':	['H',	'H',	'D',	'D',	'D',	'H',	'H',	'H',	'H',	'H'],
'S16':	['H',	'H',	'D',	'D',	'D',	'H',	'H',	'H',	'H',	'H'],
'S17': ['H',	'D',	'D',	'D',	'D',	'H',	'H',	'H',	'H',	'H'],
'S18':	['S',	'D',   'D',	'D',	'D',	'H',	'H',	'H', 'H'],
'S19':	['S',	'S',	'S',	'S',	'S',	'S',	'S',	'S',	'S',	'S'],
'S20':	['S',	'S',	'S',	'S',	'S',	'S',	'S',	'S',	'S',	'S'],
'Pair4':	['P',	'P',	'P',	'P',	'P',	'P',	'H',	'H',	'H',	'H'],
'Pair6':	['P',	'P',	'P',	'P',	'P',	'P',	'H',	'H',	'H',	'H'],
'Pair8':	['H',	'H',	'H',	'P',	'P',	'H',	'H',	'H',	'H',	'H'],
'Pair10':	['D',	'D',	'D',	'D',	'D',	'D',	'D',	'D',	'H',	'H'],
'Pair12':	['P',	'P',	'P',	'P',	'P',	'H',	'H',	'H',	'H',	'H'],
'Pair14':	['P',	'P',	'P',	'P',	'P',	'P',	'H',	'H',	'H',	'H'],
'Pair16':	['P',	'P',	'P',	'P',	'P',	'P',	'P',	'P',	'P',	'P'],
'Pair18':	['P',	'P',	'P',	'P',	'P',	'S',	'P',	'P',	'S',	'S'],
'Pair20':	['S',	'S',	'S',	'S',	'S',	'S',	'S',	'S',	'S',	'S'],
'PairA':	['P',	'P',	'P',	'P',	'P',	'P',	'P',	'P',	'P',	'P']}
def index(card, total):
    for i in range(len(cards)):
        if card == 'A':
            if total + 11 > 21:
                return 0
            elif total + 11 <= 21:
                return 13
        if card == cards[i]:
            return i
    return "This is not a valid card"

def organize(hand):
    for i in range(len(hand)):
        if hand[i] == 'A':
            del(hand[i])
            hand.append('A')
    return hand

def points(hand): #Note this means hand must be configured as an array of strings listed in cards
    total = 0
    hand = organize(hand)
    """if hand[len(hand)-1] == hand[len(hand)-2] == 'A' and len(hand) > 2:
        total+= 2
        for card in hand:
            total += card_vals[index(card,total)]"""

    for card in hand:
        total += card_vals[index(card, total)]
    return total

def random_card():
    rand_int = np.random.randint(13)
    return cards[rand_int]

def hit(hand): #simply adds a random card to a hand
    hand.append(random_card())
    return hand

def stand(hand):
    return hand

def double(hand):
    hand = hit(hand)
    return hand

def bust(hand):
    if points(hand) > 21:
        return True
    return False

def blackjack(hand):
    if points(hand) == 21 and len(hand) == 2:
        return True
    return False

def isPair(hand):
    if len(hand) == 2 and points([hand[0]]) == points([hand[1]]): #Note this is only true if the house lets you split any face cards (but also note one should never be splitting face cards in the first place)
        return True
    return False

def dealer_strategy(hand, upcard):
    while points(hand) < 17:
        hand = hit(hand)
        time.sleep(4)
        print("\n" + "Dealer hits: " + printHand(hand))
    return hand

def recordAndBalance(wins, losses, pushes, money):
    time.sleep(2)
    print("\n")
    print("Record: " + str(wins) + "-" + str(losses) + "-" + str(pushes))
    print("Balance: " + str(money))
    print("\n")

def firstCard(hand):
    return [hand[0]]

def secondCard(hand):
    return [hand[1]]

def printHand(hand):
    string = ''
    for card in hand:
        string += (str(card) + "   ")
    return string
def properStrategy(my_hand, upcard):
    #returns proper straegy based on an array of rules
    yourhand = ''
    if 'A' in my_hand:
        yourhand += 'S'
    if isPair(my_hand):
        yourhand += "Pair"

    yourhand += str(points(my_hand))

    if my_hand == ['A','A']: # super edge case that it's just hard to find a niche for, their sum doesn't work and they're a pair
        yourhand = 'PairA'
    if upcard[0] in ['J','Q','K']:
        return rules[yourhand][8]
    if upcard[0] == 'A':
        return rules[yourhand][9]
    upcardindex = int(upcard[0])-2
    return rules[yourhand][upcardindex]

def strat2command(strategy):
    if strategy == 'H':
        return 'hit'
    if strategy == 'P':
        return 'split'
    if strategy == 'S':
        return 'stand'
    if strategy == 'D':
        return 'double'

def pasttenseify(verb):
    if verb == 'stand':
        return 'stood'
    if verb == 'double':
        return 'doubled'

def playGame(bet):
    global wins
    global losses
    global pushes
    global money
    global upcard
    global my_hand
    my_hand = []
    time.sleep(1)
    upcard = [random_card()]
    print("\n" + "Dealer shows: " + printHand(upcard) + "\n")

    time.sleep(1)

    my_hand = [random_card(), random_card()]
    print("You have: " + printHand(my_hand) + "\n")

    time.sleep(1)


    if blackjack(my_hand):
        time.sleep(1)
        print("You got blackjack!")
        wins += 1
        money += bet * 1.5
        return False
    return True

def playing(my_hand,bet):
    global wins
    global losses
    global money
    RIGHT_STRATEGY = properStrategy(my_hand,upcard)
    action = raw_input("What would you like to do?   ")
    while str.lower(action) != "stand":
        if strat2command(RIGHT_STRATEGY) != str.lower(action):
            print("\n Wrong! Here you should have " + pasttenseify(strat2command(RIGHT_STRATEGY)))
        if str.lower(action) == "hit":
            my_hand = hit(my_hand)
            time.sleep(1)
            print("\n" + "You have: " + printHand(my_hand) + "\n")
        elif str.lower(action) == "double":
            my_hand = hit(my_hand)
            time.sleep(2)
            print("\n" + "You have: " + printHand(my_hand) + "\n")
            if bust(my_hand):
                time.sleep(1)
                print("You busted!")
                losses +=1
                money -= bet *2
                return False
            break
        elif str.lower(action) == "split":
            if isPair(my_hand):
                my_hand = [firstCard(my_hand),secondCard(my_hand)]
                print("\n" + "You have: " + printHand(my_hand[0]) + "\n")
                playing(my_split_hand,bet)
                print("\n" + "You have: " + printHand(my_hand[1]) + "\n")
                playing(my_split_hand2,bet)
                break
            else:
                print("\n" + "You can't split it if it's not a pair" + "\n")

        
        if bust(my_hand):
            time.sleep(1)
            print("You busted!")
            losses +=1
            money -= bet
            #playGame(response, wins, losses, pushes, money) #This is the reason that when you bust once on simulator, you have to play a whole game before you get back to the thing
            return False
        action = raw_input("What would you like to do?   ")
    return action

def evaluate_winner(my_hand, dealer_hand):
    global wins
    global losses
    global pushes
    global money

    dealer_points = points(dealer_hand)

    point_total = points(my_hand)
    if bust(dealer_hand):
        time.sleep(1)
        print("\n" + "The dealer busted!")
        wins +=1
        money += bet
    else:
        time.sleep(3.5)
        if point_total > dealer_points:
            time.sleep(1)
            print("\n" + str(point_total) + " beats " + str(dealer_points) + ". You win!")
            wins +=1
            money += bet
        elif dealer_points > point_total:
            print("\n" + str(dealer_points) + " beats " + str(point_total) + ". You lose :(")
            losses +=1
            money -= bet
        else:
            print("\n" + "You both got " + str(dealer_points) + ". It's a tie!")
            pushes +=1

wins = 0
losses = 0
pushes = 0
money = 100
upcard = ''
my_hand = []

response = raw_input("\n" +"########################################################" + "\n"+ "\n" + "Welcome to Max's Command Line Blackjack Simulator. If you would like to get started, press enter!")

while not response:
    recordAndBalance(wins,losses,pushes,money)

    bet = input("How much would you like to bet?   ")
    if not bet:
        bet = input("\nHow much would you like to bet?   ")
    if '.' in bet:
        bet = float(bet)
    else:
        bet = int(bet)
    if playGame(bet):
        my_split_hand = firstCard(my_hand)
        my_split_hand2 = secondCard(my_hand)

        finalreturn = playing(my_hand,bet)
        if finalreturn:
            dealer_hand = hit(upcard) #dealer (by flipping over hole card is effectively hitting)
            print("\n" + "Dealer had: " + printHand(dealer_hand))
            if blackjack(dealer_hand):
                time.sleep(1)
                print("\n The dealer had blackjack!")
                losses += 1
                money -= bet
                continue
            dealer_hand = dealer_strategy(dealer_hand, upcard) #even though upcard is completely unnecessary, need to include it because of the declaratory and strict nature of parameters,
            if str.lower(finalreturn) == "split":
                if not bust(my_split_hand):
                    evaluate_winner(my_split_hand, dealer_hand)
                if not bust(my_split_hand2):
                    evaluate_winner(my_split_hand2, dealer_hand)
            else:
                if str.lower(finalreturn) == "double":
                    bet *=2
                evaluate_winner(my_hand, dealer_hand)
