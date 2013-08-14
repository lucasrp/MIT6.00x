def noReplacementSimulation(numTrials):
    '''
    Runs numTrials trials of a Monte Carlo simulation
    of drawing 3 balls out of a bucket containing
    3 red and 3 green balls. Balls are not replaced once
    drawn. Returns the a decimal - the fraction of times 3 
    balls of the same color were drawn.
    '''
    
    sucesses = 0
    for trial in range(numTrials+1):
        Bucket = ["B","B","B","R","R","R"]
        Sample = random.sample(Bucket, 3)
        
        flag = False
        for n in range(len(Sample) - 1):
            
            if Sample[n] is not Sample[n+1]:
                flag = True
        
        if flag == False:
            sucesses += 1

    print sucesses, numTrials
    print sucesses * 1.0/numTrials
    return sucesses * ((numTrials)**(-1))
