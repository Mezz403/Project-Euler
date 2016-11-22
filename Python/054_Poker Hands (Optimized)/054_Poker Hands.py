import collections


def convert_facecards(value):
    """
    Convert Ten (T), Jack (J), Queen (Q), King (K), and Ace (A) to corresponding numerical value
    :param value: list of characters
    :return: The numerical equivalent of a face card
    """
    for i, num in enumerate(value):
        if num == 'T':
            value[i] = '10'
        elif num == 'J':
            value[i] = '11'
        elif num == 'Q':
            value[i] = '12'
        elif num == 'K':
            value[i] = '13'
        elif num == 'A':
            value[i] = '14'

    return value


def compare(x, y):
    """
    Compare two lists for equality
    :param x: The first of two lists to compare
    :param y: The second of two lists to compare
    :return: True if list x equals list y, else False
    """
    return sorted(x) == sorted(y)


def is_royalflush(value, suit):
    """
    Determine if player hand is a royal flush: T, J, Q, K, A of same suit
    :param value: list of cards' numerical value
    :param suit: list of cards' suits
    :return: True if hand is a royal flush, otherwise False
    """
    royalflush = ['10', '11', '12', '13', '14']  # ['T', 'J', 'Q', 'K', 'A']

    # Determine if suit elements are identical and if value elements equal royalflush elements. If True, the hand can be
    # concluded as a royal flush.
    if suit.count(suit[0]) == len(suit) and compare(value, royalflush):
        return True
    else:
        return False


def is_straightflush(value, suit):
    """
    Determine if hand is a straight flush: all cards are consecutive values of same suit
    :param value: list of cards' numerical value
    :param suit: list of cards' suits
    :return: True if hand is a straight flush, otherwise False
    """

    # Determine if the suit elements are identical. If not, the hand cannot be concluded as a straight flush.
    if suit.count(suit[0]) == len(suit):
        value = sorted(map(int, value))
        straight = [value[0]]

        # Based on the first element in value, generate the ideal straight sequence.
        for i in range(0, 4):
            straight.append(straight[i] + 1)

        # Determine if the value list equals the straight value list. If True, the hand can be concluded as a straight
        # flush.
        if compare(value, straight):
            return True
        else:
            return False

    else:
        return False


def is_fourofakind(value):
    """
    Determine if hand is a Four of a Kind: four cards have the same value
    :param value: list of cards' numerical value
    :return: True if hand is a Four of a Kind as well list of remaining
             cards not in winning sequence and the value of the winning hand, otherwise False
    """

    # Establish a count of all the elements in the value list
    count = collections.Counter()
    count.update(value)

    # Determine if the quantity of the most common value in the count equates to 4. If True, the hand can be concluded
    # as a Four of a Kind
    for letter, count in count.most_common(1):
        if count >= 4:
            # The remainder of the cards in the hand not used in the sequence are set apart to be possibly used in a
            # tie breaker
            remainder = list(filter(lambda a: a != letter, value))
            return True, remainder, letter
        else:
            return False


def is_fullhouse(value):
    """
    Determine if the hand is a Full House: Three of a kind and a Pair
    :param value: list of cards numerical value
    :return: True if hand is a Full House, otherwise False
    """

    # A Full House composes of one pair and one three of a kind. If the hand can be determined as both a One Pair and
    # a Three of a Kind, the hand can be concluded as a Full House.
    if is_onepair(value) and is_threeofakind(value):
        return True
    else:
        return False


def is_flush(suit):
    """
    Determine if the hand is a Flush: All cards of the same suit
    :param suit: list of cards' suits
    :return: True if hand is a Flush, otherwise False
    """

    # Determine if the suit of the cards in the hand are identical. If True, the hand can be concluded as a Flush.
    if suit.count(suit[0]) == len(suit):
        return True
    else:
        return False


def is_straight(value):
    """
    Determine if the hand is a Straight: A continuous sequence of five cards
    :param value: list of cards' numerical value
    :return: True if hand is a Straight, otherwise False
    """

    # Get the smallest element in value and initialize a new list with the smallest element in value.
    value = sorted(map(int, value))
    straight = [value[0]]

    # Based on the first element in value, generate the ideal straight sequence.
    for i in range(0, 4):
        straight.append(straight[i] + 1)

    # Determine if the value list is identical to the straight list. If True, the hand can be concluded as a straight.
    if compare(value, straight):
        return True
    else:
        return False


def is_threeofakind(value):
    """
    Determine if the hand is a Three of a Kind: Three cards have the same value
    :param value: list of cards' numerical value
    :return: True if the hand is a Three of a Kind as well list of remaining
             cards not in winning sequence and the value of the winning hand, otherwise False
    """

    # Establish a count of all the elements in the value list
    count = collections.Counter()
    count.update(value)

    # Determine if the quantity of the most common value in the count equates to 3. If True, the hand can be concluded
    # as a Three of a Kind
    for letter, count in count.most_common(1):
        if count == 3:
            # The remainder of the cards in the hand not used in the sequence are set apart to be possibly used in a
            # tie breaker
            remainder = list(filter(lambda a: a != letter, value))
            return True, remainder, letter
        else:
            return False


def is_twopair(value):
    """
    Determine if the hand is a Two Pair: Two different pairs of cards
    :param value: list of cards' numerical value
    :return: True if the hand is a Two Pair, otherwise False
    """

    # Establish a count of all the elements in the value list
    count = collections.Counter()
    count.update(value)

    pair = 0

    # Using the two most common elements in the count, determine if both of their frequencies is equivalent to 2.
    for letter, count in count.most_common(2):
        if count == 2:
            pair += 1

    # Determine if there are two pairs in the hand. If True, the hand can be concluded as a Two Pair.
    if pair == 2:
        return True
    else:
        return False


def is_onepair(value):
    """
    Determine if the hand contains One Pair of cards
    :param value: list of cards' numerical value
    :return: True if the hand is a One Pair as well list of remaining
             cards not in winning sequence and the card value of the winning hand, otherwise False
    """

    # Establish a count of all the elements in the value list
    count = collections.Counter()
    count.update(value)

    # Determine if the most common element in the hand has a quantity of two. If True, the hand can be concluded as a
    # One Pair.
    for letter, count in count.most_common(1):
        if count == 2:
            # The remainder of the cards in the hand not used in the sequence are set apart to be possibly used in a
            # tie breaker
            remainder = list(filter(lambda a: a != letter, value))
            return True, remainder, letter

    return False


def is_highcard(value1, value2):
    """
    Determine if the first hand contains the highest card between the two hands
    :param value1: first list of cards' numerical value to be compared
    :param value2: second list of cards' numerical value to be compared
    :return: True if value1 has the highest card, otherwise false
    """

    # Determine if value1 is greater than value2 for when value1 and value2 are string types
    if type(value1) == 'string':
        if int(value1) > int(value2):
            return True
        else:
            return False
    else:
        # value1 and value2 are lists and are mapped as int and sorted from highest to lowest
        res1 = sorted(list(map(int, value1)), reverse=True)
        res2 = sorted(list(map(int, value2)), reverse=True)

        # Determine if value1 has the highest card. If True, value1 can be concluded to have the highest card
        for i in range(0, len(value1) - 1):
            if res1[i] < res2[i]:
                return False
            elif res1[i] > res2[i]:
                return True


def result(value, suit):
    """
    Determine sequence of hand and subsequent value of win
    :param value: list of cards' numerical value
    :param suit: list of cards' suits
    :return: (int) rank, (list) remainder, (char) card
    """
    card = ''
    remainder = []

    # Determine the sequence that the hand contains, and the rank of the hand. The more valuable the hand, the higher
    # the rank.

    # Determine if hand is a Royal Flush.
    if is_royalflush(value, suit):
        rank = 10
    # Determine if hand is a Straight Flush.
    elif is_straightflush(value, suit):
        rank = 9
    # Determine if hand is a Four of a Kind.
    elif is_fourofakind(value):
        card = is_fourofakind(value)[2]
        remainder = is_fourofakind(value)[1]
        rank = 8
    # Determine if hand is a Full House.
    elif is_fullhouse(value):
        rank = 7
    # Determine if hand is a Flush.
    elif is_flush(value):
        rank = 6
    # Determine if hand is a Straight.
    elif is_straight(value):
        rank = 5
    # Determine if hand is a Three of a Kind.
    elif is_threeofakind(value):
        card = is_threeofakind(value)[2]
        remainder = is_threeofakind(value)[1]
        rank = 4
    # Determine if hand is a Two Pair.
    elif is_twopair(value):
        rank = 3
    # Determine if hand is a One Pair.
    elif is_onepair(value):
        card = is_onepair(value)[2]
        remainder = is_onepair(value)[1]
        rank = 2
    # The hand has no sequence by this point.
    else:
        rank = 1

    return rank, remainder, card


def project_euler54():
    """
    Determine the amount of hands Player 1 wins
    :return: (int) wins
    """

    # Text file containing played hands between two players.
    handsfile = \
        "C:\\Users\\Alexis\\Documents\\GitHub\\Project-Euler\\Python\\054_Poker Hands (Optimized)\\p054_poker.txt"

    wins = 0

    # Open the file and run through each played game
    with open(handsfile) as hands:
        for hand in hands:
            player1 = []
            player2 = []
            value1 = []
            suit1 = []
            value2 = []
            suit2 = []

            # Remove the end of line character and split the line into a list delimited by a space
            hand = hand.replace('\n', '')
            hand = hand.split(' ')

            # Split out the two players' hands. The first player is the first 5 elements and the second player is the
            # last 5 elements.
            for i in range(0, 5):
                player1.append(hand[i])
            for i in range(5, 10):
                player2.append(hand[i])

            # Separate the value of the card from the suit of the card for further assessment.
            for card in player1:
                value1.append(str(card[:-1]))
                suit1.append(card[-1:])
            for card in player2:
                value2.append(str(card[:-1]))
                suit2.append(card[-1:])

            # Convert any face cards (T, J, Q, K, A) to their numerical equivalent (10, 11, 12, 13, 14)
            value1 = convert_facecards(value1)
            value2 = convert_facecards(value2)

            # Determine the best sequence the two hands preset.
            player1_result = result(value1, suit1)
            player2_result = result(value2, suit2)

            # Determine if Player 1 won the hand. Below are the scenarios where Player 1 can win:
            if player1_result[0] == 1 and player2_result[0] == 1:
                # If both hands have rank 1, Player 1 has the highest card
                if is_highcard(value1, value2):
                    wins += 1
                continue
            # Player 1's rank is higher
            elif player1_result[0] > player2_result[0]:
                wins += 1
                continue
            elif player1_result[0] == player2_result[0]:
                # If both hands have the same rank not equal to 1, Player 1 has the highest card between the two
                # sequences
                if int(player1_result[2]) > int(player2_result[2]):
                    wins += 1
                    continue
                # If both hands have the same rank and the same winning hand, Player 1 has the highest card outside the
                # winning sequence
                elif player1_result[2] == player2_result[2]:
                    if is_highcard(player1_result[1], player2_result[1]):
                        wins += 1

    return wins

# Get the results of the problem
print(project_euler54())
