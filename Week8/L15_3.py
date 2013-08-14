def stdDevOfLengths(L):
    """
    L: a list of strings

    returns: float, the standard deviation of the lengths of the strings,
      or NaN if L is empty.
    """
    
    lenght = 6
    listOfLenghts = [10, 4, 12, 15, 20, 5]
    median = 1.0*sum(listOfLenghts)/lenght
    tot = 0.0

    for e in listOfLenghts:
        tot += (e - median)**2
    
    return ((tot/lenght)**0.5)/median
 
    
            
        
