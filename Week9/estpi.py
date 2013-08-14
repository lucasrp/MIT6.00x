def stdDev(X):
    mean = sum(X)/float(len(X))
    tot = 0
    for x in X:
        tot += (x-mean)**2
    return (tot/len(X))**0.5

def throwNeedles(numNeedles):
    inCircle = 0
    for needle in range(1, numNeedles + 1):
        x = random.random()
        y = random.random()
        if (x*x + y*x)**0.5 <= 1.0:
            inCircle += 1
    return 2*(inCircle/float(numNeedles))
