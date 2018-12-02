####
# Inline code comments under function "move" with "-TP" at the end are by Trevor Peitzman
####

import random

team_name = 'MeltingPot' # Only 10 chars displayed.
strategy_name = 'America The Beautiful'
strategy_description = 'a programmers rendition of the American Dream'
    
def move(my_history, their_history, my_score, their_score):
    ''' Arguments accepted: my_history, their_history are strings.
    my_score, their_score are ints.
    
    Make my move.
    Returns 'c' or 'b'. 
    '''

    # my_history: a string with one letter (c or b) per round that has been played with this opponent.
    # their_history: a string of the same length as history, possibly empty. 
    # The first round between these two players is my_history[0] and their_history[0].
    # The most recent round is my_history[-1] and their_history[-1].
    
    # Analyze my_history and their_history and/or my_score and their_score.
    # Decide whether to return 'c' or 'b'.

    # Create variable to represent the probability this is the last round to be played  -TP
    # knowing there is a random # of rounds played between 100 & 200    -TP
    probability_round_is_last = float((len(my_history))-100)/99.0

    # If opponent betrays in first 8 moves even though I didn't, retaliate for rest of match    -TP
    if 'b' in their_history[0:8]:
        return 'b'
    # As end of match approaches, change tactic slightly    -TP
    # Return 'b' when on the guaranteed last round      -TP
    elif probability_round_is_last == 1:
        return 'b'
    # Avoid issue with having no history; always return 'c' on first round  -TP
    elif len(their_history) == 0:
        return 'c'
    #First Round: no response is given, so their_history == 0 characters. Program colludes as initial response. --Brandon Rios
    elif their_history[-1] == 'b':
        return 'b'
    ##Subsequent Rounds: If opponent answered with 'betray' the previous round, respond with betray. --Brandon Rios
    else:
        return 'c'
    ###Subsequent Rounds (cont'd): If opponent responded with other (a.k.a. Collude) in previous round, respond with collude. --Brandon Rios

    
def test_move(my_history, their_history, my_score, their_score, result):
    '''calls move(my_history, their_history, my_score, their_score)
    from this module. Prints error if return value != result.
    Returns True or False, dpending on whether result was as expected.
    '''
    real_result = move(my_history, their_history, my_score, their_score)
    if real_result == result:
        return True
    else:
        print("move(" +
            ", ".join(["'"+my_history+"'", "'"+their_history+"'",
                       str(my_score), str(their_score)])+
            ") returned " + "'" + real_result + "'" +
            " and should have returned '" + result + "'")
        return False

if __name__ == '__main__':
     
    # Test 1: Betray on first move.
    if test_move(my_history='',
              their_history='', 
              my_score=0,
              their_score=0,
              result='c'):
         print 'Test passed'
     # Test 2: Continue betraying if they collude despite being betrayed.
    test_move(my_history='bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb',
              their_history='bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb',
              # Note the scores are for testing move().
              # The history and scores don't need to match unless
              # that is relevant to the test of move(). Here,
              # the simulation (if working correctly) would have awarded 
              # 300 to me and -750 to them. This test will pass if and only if
              # move('bbb', 'ccc', 0, 0) returns 'b'.
              my_score=0, 
              their_score=0,
              result='b')