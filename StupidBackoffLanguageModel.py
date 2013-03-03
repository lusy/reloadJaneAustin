import math, collections

class StupidBackoffLanguageModel:

    def __init__(self, corpus):
        """Initialize your data structures in the constructor."""
        self.unigramCounts = collections.defaultdict(lambda: 0)
        self.bigramCounts = collections.defaultdict(lambda: 0)
        self.fromUniToBiGrams = collections.defaultdict(lambda: 0)
        self.total = 0
        self.train(corpus)

    def train(self, corpus):
        """ Takes a corpus and trains your language model.
            Compute any counts or other corpus statistics in this function.
        """

        for datum in corpus:
            tokenuni = datum
            self.unigramCounts[tokenuni] = self.unigramCounts[tokenuni] + 1
            self.total += 1

        bitokens = zip(corpus[0:len(corpus)-1], corpus[1:len(corpus)])

        for bidatum in bitokens:
            tokenbi = (bidatum[0], bidatum[1])
            self.bigramCounts[tokenbi] = self.bigramCounts[tokenbi] + 1
            try:
                isThere = self.fromUniToBiGrams[bidatum[0]]
                self.fromUniToBiGrams[bidatum[0]].append(bidatum[1])
            except:
                self.fromUniToBiGrams[bidatum[0]] = [bidatum[1]]

    def score(self, sentence):
        """ Takes a list of strings as argument and returns the log-probability of the
            sentence using your language model. Use whatever data you computed in train() here.
        """
        score = 0.0
        vocabulary = len(self.unigramCounts)

        bisentence = zip(sentence[0:len(sentence)-1], sentence[1:len(sentence)])
        for token in bisentence:
            count = self.bigramCounts[token]
            if count > 0:
                score += math.log(count)
                score -= math.log(self.unigramCounts[token[0]])
            else:
                score += math.log(0.4)
                score += math.log(self.unigramCounts[token[1]]+1)
                score -= math.log(self.total+vocabulary) # smoothed
        return score
