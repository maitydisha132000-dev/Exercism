"""Functions for tracking poker hands and assorted card tasks.

Python list documentation: https://docs.python.org/3/tutorial/datastructures.html
"""


def get_rounds(number):
    """Create a list containing the current and next two round numbers.

    Parameters:
        number (int): The current round number.

    Returns:
        list: The current round number and the two that follow.
    """

    result=[]
    for i in range(3):
        result.append(number+i)
    return result
        


def concatenate_rounds(rounds_1, rounds_2):
    """Concatenate two lists of round numbers.

    Parameters:
        rounds_1 (list): The first rounds played.
        rounds_2 (list): The second group of rounds played.

    Returns:
        list:  All rounds played.
    """

    return rounds_1+rounds_2

def list_contains_round(rounds, number):
    """Check if the list of rounds contains the specified number.

    Parameters:
        rounds (list): The rounds played.
        number (int): The round number.

    Returns:
        bool: Was the round played?
    """

    if number in rounds:
        return True
    else:
        return False


def card_average(hand):
    """Calculate and returns the average card value from the list.

    Parameters:
        hand (list): The cards in the hand.

    Returns:
        float: The average value of the cards in the hand.
    """
    result=0
    for i in hand:
        result+=i
        avg=result/len(hand)
    return avg


def approx_average_is_average(hand):
    """Return if the (average of first and last card values) OR ('middle' card) == calculated average.

    Parameters:
        hand (list): The cards in the hand.

    Returns:
        bool: Does one of the approximate averages equal the `true average`?
    """

    s1=(hand[0]+hand[-1])/2
    s2=0
    mid=len(hand)//2
    if len(hand)%2==0:
        avg=(hand[mid]+hand[mid-1])/2
    else:
        avg=hand[mid]
    for i in hand:
        s2+=i
        o_a=s2/len(hand)
    if s1==o_a or avg==o_a:
        return True
    else:
        return False
        


def average_even_is_average_odd(hand):
    """Return if the (average of even indexed card values) == (average of odd indexed card values).

    Parameters:
        hand (list): The cards in the hand.

    Returns:
        bool: Are the even and odd averages equal?
    """
    even_i=0
    even_l=0
    odd_i=0
    odd_l=0
    for i in range(len(hand)):
        if i%2==0:
            even_i+=hand[i]
            even_l+=1
        else:
            odd_i+=hand[i]
            odd_l+=1
    even_avg=even_i/even_l
    odd_avg=odd_i/odd_l
    if even_avg==odd_avg:
        return True
    else:
        return False
            


def maybe_double_last(hand):
    """Multiply a Jack card value in the last index position by 2.

    Parameters:
        hand (list): The cards in the hand.

    Returns:
        list: The hand with Jacks (if present) value doubled.
    """

    if hand[-1]==11:
        result=hand[-1]*2
        hand[-1]=result
    return hand
