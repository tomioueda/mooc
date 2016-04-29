"""
Planner for Yahtzee
Simplifications:  only allow discard and roll, only score against upper level

www.codeskulptor.org
"""

# Used to increase the timeout, if necessary
import codeskulptor
codeskulptor.set_timeout(20)

def gen_all_sequences(outcomes, length):
    """
    Iterative function that enumerates the set of all sequences of
    outcomes of given length.
    """
    answer_set = set([()])
    for dummy_idx in range(length):
        temp_set = set()
        for partial_sequence in answer_set:
            for item in outcomes:
                new_sequence = list(partial_sequence)
                new_sequence.append(item)
                temp_set.add(tuple(new_sequence))
        answer_set = temp_set
    return answer_set


def score(hand):
    """
    Compute the maximal score for a Yahtzee hand according to the
    upper section of the Yahtzee score card.

    hand: full yahtzee hand

    Returns an integer score 
    """
    max_score = 0
    dict_score = dict((handitem,0) for handitem in hand)
    for eachitem1 in hand:
        dict_score[eachitem1] += eachitem1
        if dict_score[eachitem1] > max_score :
            max_score = dict_score[eachitem1]           
    return max_score;
            


def expected_value(held_dice, num_die_sides, num_free_dice):
    """
    Compute the expected value of the held_dice given that there
    are num_free_dice to be rolled, each with num_die_sides.

    held_dice: dice that you will hold
    num_die_sides: number of sides on each die
    num_free_dice: number of dice to be rolled

    Returns a floating point expected value
    """
    tuples1 = tuple([x+1 for x in range(num_die_sides)])
    set1=gen_all_sequences(tuples1, num_free_dice)
    sum1 = 0;
    for each in set1:
        hand_cur = tuple(held_dice + each);
        sum1 += score(hand_cur)
    return float(sum1)/len(set1) 


def gen_all_holds(hand):
    """
    Generate all possible choices of dice from hand to hold.

    hand: full yahtzee hand

    Returns a set of tuples, where each tuple is dice to hold
    """
    set_cur = set([()])
    for hand_ele in hand:
        for each in set_cur.copy():
            new_each = list(each)
            new_each.append(hand_ele)
            set_cur.add(tuple(new_each))
    return set_cur   


def strategy(hand, num_die_sides):
    """
    Compute the hold that maximizes the expected value when the
    discarded dice are rolled.

    hand: full yahtzee hand
    num_die_sides: number of sides on each die

    Returns a tuple where the first element is the expected score and
    the second element is a tuple of the dice to hold
    """
    all_holds = gen_all_holds(hand)
    max_score = 0.0
    max_hold = ()
    for each in all_holds:
        num_free_dice = len(hand) - len(each)
        each_score = expected_value(each, num_die_sides, num_free_dice)
        if each_score > max_score:
            max_score = each_score
            max_hold = each
    return (max_score, max_hold)


def run_example():
    """
    Compute the dice to hold and expected score for an example hand
    """
    num_die_sides = 6
    hand = (1, 1, 1, 5, 6)
    hand_score, hold = strategy(hand, num_die_sides)
    print "Best strategy for hand", hand, "is to hold", hold, "with expected score", hand_score
    

if __name__ == '__main__':
    run_example()
    
    # Test game with the console or the GUI.  Uncomment whichever
    # you prefer.  Both should be commented out when you submit
    # for testing to save time.
    import poc_holds_testsuite
    poc_holds_testsuite.run_suite(gen_all_holds)