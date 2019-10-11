from random import randint, seed
import sys
from collections import Counter
# from collections import deque

flag = -1
play_count = 5
times = ['second', 'third']
poker_hands = []
pokers = { 0: 'Ace', 1:'King', 2:'Queen', 3:'Jack', 4:'10', 5:'9' }
probabilities = {'Five of a kind':0, 'Four of a kind':0,  'Full house':0, 'Straight':0, 
                        'Three of a kind':0, 'Two pair':0, 'One pair':0}
# Bust

# sort pokers function
def returnPokersSort(v):
    value = {v: k for k, v in pokers.items()}
    return value[v]

# sublist from my assignment1_3
def is_sub_list(list_1,list_2):
    ori_length = len(list_2)
    temp = list_2.copy()
    if len(list_1) > len (temp):
        return False
    else:
        for i in range( len( list_1 ) ):
            if list_1[i] in temp:
                temp.remove(list_1[i])
        if len(list_1) == ori_length - len(temp):
            return True
        else:
            return False
    
# needed remove
# seed(0) 

def hands(play_count):
    global flag
    global poker_hands
    for _ in range(play_count):
        poker_hands.append( pokers[randint(0, 5)] )
    # sort poker_hands regarding its key
    poker_hands.sort( key = returnPokersSort)
    print( f'The roll is: {" ".join(poker_hands)}' ) 
    print('It is a',check_hands(poker_hands))
    flag +=1
    
## check probabilities using counter
# from collections import Counter
# a = dict(Counter(MyList))
# >>> print a           #or print(a) in python-3.x
# {'a': 3, 'c': 3, 'b': 1}
    
def check_hands(L):
    check = dict( Counter(L))
    if len(check) == 1:
        check_str = 'Five of a kind'
    elif len(check) == 2:
        for anycards in check:
            if check[anycards] == 4:
                check_str = 'Four of a kind'
                break
            elif check[anycards] == 3:
                check_str = 'Full house'
                break
    elif len(check) == 3:
        for anycards in check:
            if check[anycards] == 3:
                check_str = 'Three of a kind'
                break
            elif check[anycards] == 2:
                check_str = 'Two pair'
                break
    elif len(check) == 4:
        for anycards in check:
            if check[anycards] == 2:
                check_str = 'One pair'
                break
    elif L == [ 'Ace', 'King', 'Queen', 'Jack', '10'] or L == [ 'King', 'Queen', 'Jack', '10', '9']:
        check_str = 'Straight'
    else:
        check_str = 'Bust'
    if check_str != 'Bust':  
        probabilities[check_str] += 1
    return check_str

        
def initialHands():
    global poker_hands
    global flag
    print('Ok, done.')
    flag = -1
    poker_hands = []

def play():
    global poker_hands
    global times
    global flag
    # exit without output "OK, done"
    output_done = 0
    hands(5)
    # when round less than 3
    while flag < 2:
        which_kept = input(f'Which dice do you want to keep for the {times[flag]} roll? ').split()
        if len(which_kept) == 0:
            poker_hands = []
            hands(5)
            output_done = 1
            poker_hands = []
        else:
            while which_kept[0].lower()!= 'all':
                # All all input equals poker_hands
                if is_sub_list(poker_hands, which_kept):
                    # input = poker_hands, interrupt set flag = 10
                    flag = 10
                    poker_hands = []
                    break
                # input is the sublist of poker_hands
                elif is_sub_list( which_kept, poker_hands):
                    poker_hands = []
                    for cards in which_kept:
                        # kept cards
                        poker_hands.append(cards)
                    # how many cards does hands() generate
                    play_count = 5 - len(which_kept)
                    hands(play_count)
                    output_done = 1
                    break
                else:
                    print('That is not possible, try again!')
                    break
            # input All, all or same as poker_hands
            if which_kept[0].lower() == 'all' or flag == 10: 
                initialHands()
                break
    # # ends with "OK, done"
    # if flag != 10 and flag != -1 and output_done == 0:
    #     initialHands()

    # initial 
    flag = -1
    poker_hands = []

def simulate(n):
    for i in range(n):
        poker_hands = []
        for _ in range(5):
            poker_hands.append( pokers[randint(0, 5)] )
        # sort poker_hands regarding its key
        poker_hands.sort( key = returnPokersSort)
#         print(poker_hands)
        check_hands(poker_hands)
    for j in probabilities:
        ratio = probabilities[j]/n
        ratio = format(ratio, '0.2%')
        print( j.ljust(14)+':',ratio)
    for p in probabilities:
        probabilities[p] = 0
    