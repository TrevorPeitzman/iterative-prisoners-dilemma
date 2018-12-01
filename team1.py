team_name = 'Bscts&Grvy'
strategy_name = 'Timmy the Trustworthy'
strategy_description = 'Begins with collusion. Mimics the answer of the opponent in the previous round.'
    
def move(my_history, their_history, my_score, their_score): #Identifies all possible used variables in game.
    if len(their_history) == 0:
        return 'c'
    #First Round: no response is given, so their_history == 0 characters. Program colludes as initial response. --Brandon Rios
    elif their_history[-1] == 'b':
        return 'b'
    ##Subsequent Rounds: If opponent answered with 'betray' the previous round, respond with betray. --Brandon Rios
    else:
        return 'c'
    ###Subsequent Rounds (cont'd): If opponent responded with other (a.k.a. Collude) in previous round, respond with collude. --Brandon Rios
    ####
    #   Variables 'my_history', 'my_score', and 'their_score' are not considered b/c Timmy the Trustworthy does not take them into
    #   account when making his decision. The strategy is a simple one: mimic the answer of his opponent's from the previous round.
    #   Using the psychology of human competition against them, for his own benefit.                        --Brandon Rios
    ####
    
def test_move(my_history, their_history, my_score, their_score, result):
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
     
    if test_move(my_history='',
              their_history='', 
              my_score=0,
              their_score=0,
              result='b'):
         print 'Test passed'
     
    test_move(my_history='bbb',
              their_history='ccc', 
              my_score=0, 
              their_score=0,
              result='b')             