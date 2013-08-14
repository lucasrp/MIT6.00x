import random
def genEven():
    '''
    Generates a random number x, where 0 <= x < 100
    '''
    list = []
    for number in range(0,100):
        if number%2 != 0:
            list.append(number)
    
    return random.choice(list)
