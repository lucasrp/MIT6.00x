import pylab


WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # wordList: list of strings
    wordList = []
    for line in inFile:
        wordList.append(line.strip().lower())
    print "  ", len(wordList), "words loaded."
    return wordList

def plotVowelProportionHistogram(wordList, numBins=15):
    """
    Plots a histogram of the proportion of vowels in each word in wordList
    using the specified number of bins in numBins
    """

    
    proportion = []

    for e in wordList:
        vowel = 0
        for letter in e:
            if letter in "aeiou":
                vowel += 1
        proportion.append(1.0*vowel/len(e))
        
    pylab.hist(proportion, numBins)
    xmin,xmax = pylab.xlim()
    ymin,ymax = pylab.ylim()
    pylab.xlabel("Vowel Distribution")
    pylab.ylabel("Number of occurrencies")
    pylab.title("Distributions")
    pylab.text(xmin, (ymax*18-ymin*2)/20, "Median is " + str(sum(proportion)*1.0/len(proportion)))
    pylab.show()
    




    

if __name__ == '__main__':
    wordList = loadWords()
    plotVowelProportionHistogram(wordList)
