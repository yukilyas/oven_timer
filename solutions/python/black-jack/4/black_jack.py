"""Functions to help play and score a game of blackjack.

How to play blackjack:    https://bicyclecards.com/how-to-play/blackjack/
"Standard" playing cards: https://en.wikipedia.org/wiki/Standard_52-card_deck
"""


def value_of_card(card):
    """Determine the scoring value of a card.

    :param card: str - given card.
    :return: int - value of a given card.  See below for values.

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 1
    3.  '2' - '10' = numerical value.
    """
    if card in ('K' ,'Q' , 'J'):
        return  10
    if card == 'A':
        return 1
    return int(card)
    


def higher_card(card_one, card_two):
    """Determine which card has a higher value in the hand.

    :param card_one, card_two: str - cards dealt in hand.  See below for values.
    :return: str or tuple - resulting Tuple contains both cards if they are of equal value.

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 1
    3.  '2' - '10' = numerical value.
    """
    V1 = value_of_card(card_one)
    V2 = value_of_card(card_two)

    if   V1 > V2:
        return card_one
    if V2 > V1:
        return card_two
    
    return  card_one, card_two
    


def value_of_ace(card_one, card_two):
    """Calculate the most advantageous value for the ace card.

    :param card_one, card_two: str - card dealt. See below for values.
    :return: int - either 1 or 11 value of the upcoming ace card.

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 11 (if already in hand)
    3.  '2' - '10' = numerical value.
    """
    V1 = value_of_card(card_one)
    V2 = value_of_card(card_two)
    
    if card_one == 'A':
        V1 = 11
    if card_two == 'A':
        V2 = 11

    ValueTotal = V1 + V2
    
    if ValueTotal + 11 > 21:
        return 1
   
    return 11
    
    


def is_blackjack(card_one, card_two):
    """Determine if the hand is a 'natural' or 'blackjack'.

    :param card_one, card_two: str - card dealt. See below for values.
    :return: bool - is the hand is a blackjack (two cards worth 21).

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 11 (if already in hand)
    3.  '2' - '10' = numerical value.
    """
    Ten_cards = ('J', 'Q', 'K', '10')
    A_card = ('A', '11')

    if card_one in Ten_cards and card_two in A_card:
        return True
    if card_two in Ten_cards and card_one in A_card:
        return True
    
    return False

def can_split_pairs(card_one, card_two):
    """Determine if a player can split their hand into two hands.

    :param card_one, card_two: str - cards dealt.
    :return: bool - can the hand be split into two pairs? (i.e. cards are of the same value).
    """
    V1 = value_of_card(card_one)
    V2 = value_of_card(card_two)
    if V1 == V2:
        return True
    
    return False
    


def can_double_down(card_one, card_two):
    """Determine if a blackjack player can place a double down bet.

    :param card_one, card_two: str - first and second cards in hand.
    :return: bool - can the hand can be doubled down? (i.e. totals 9, 10 or 11 points).
    """
    V1 = value_of_card(card_one)
    V2 = value_of_card(card_two)
    cards = (9, 10, 11)

    CardTotal = V1 + V2

    return CardTotal  in cards

    
