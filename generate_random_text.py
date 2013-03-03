import sys
import string
import random
from StupidBackoffLanguageModel import StupidBackoffLanguageModel

"""
Plan:
    * develop language model
    * train language model on the input data
    * generate output data

"""


def randomText (inputText, length):
    lm = StupidBackoffLanguageModel(inputText)

    #print "unigramCounts: ", lm.unigramCounts

    vocab = lm.unigramCounts.keys()
    #print "bigramCounts: ", lm.bigramCounts

    #print "test......................."
    #for x in lm.bigramCounts.keys():
    #    if x[0] == 'and':
    #        print x[1]
    #print "................."
    #print "fromUniToBi: ", lm.fromUniToBiGrams

    maxIndex = len(vocab) - 1

    # current version
    randText = []
    for i in range(length):
        tempNextWords = dict()
        # if random text empty, pick a first word at random
        if len(randText) == 0:
            randomIndex = random.randint(0,maxIndex)
            randText.append(vocab[randomIndex])
        # otherwise we've got at leat one word in the random text and we select the last one
        else:
            lastWord = randText[len(randText) - 1]
            # if lastWord is only once in input text
            if lm.unigramCounts[lastWord] == 1:
                coin = random.randint(0,1)
                # with 50% prob pick 2. part of bigram
                if coin == 0:
                    try:
                        isItTheLastCorpusWord = lm.fromUniToBiGrams[lastWord]
                        randText.append((lm.fromUniToBiGrams[lastWord])[0])
                    except:
                        randomIndex = random.randint(0,maxIndex)
                        randText.append(vocab[randomIndex])

                # with 50% prob pick random word from vocab
                else:
                    randomIndex = random.randint(0,maxIndex)
                    randText.append(vocab[randomIndex])
            # if lastWord is more than once in corpus, pick one of the possible bigrams
            else:
                possibleBis = lm.fromUniToBiGrams[lastWord]
                dice = random.randint(0,len(possibleBis)-1)
                randText.append(possibleBis[dice])

    return " ".join(randText)


"""
        # old version
        # picking between 5 and 15 different next words, computing the lm score and chosing the best one
        # creates a copy of randText and not a second reference to it!!!!!
        tmpRandomText = randText[:]
        for j in range(random.randint(15,30)):
            randomIndex = random.randint(0,maxIndex)
            tmpNW = vocab[randomIndex]
            tmpRandomText.append(tmpNW)
            score = lm.score(tmpRandomText)
            tempNextWords[score] = tmpNW

        bestWord = tempNextWords[max(tempNextWords)]
        if i == 0:
            print bestWord
            print "randText before: ", randText

        randText.append(bestWord)
        if i== 0:
            print "randText after: ", randText
"""
    #return " ".join(randText)

"""
    # oldest version
    bagOfWords = inputText.split()
    maxIndex = len(bagOfWords) - 1

    randText = []
    for x in range(length):
        randomIndex = random.randint(0,maxIndex)
        randText.append(bagOfWords[randomIndex])

    return " ".join(randText)
"""

def main():
    input_alice = "ALICE was beginning to get very tired of sitting by her sister on the bank, and of having nothing to do: once or twice she had peeped into the book her sister was reading, but it had no pictures or conversations in it, 'and what is the use of a book,' thought Alice, 'without pictures or conversations?' So she was considering in her own mind (as well as she could, for the hot day made her feel very sleepy and stupid) whether the pleasure of making a daisy-chain would be worth the trouble of getting up and picking the daisies, when suddenly a White Rabbit with pink eyes ran close by her. There was nothing so _very_ remarkable in that; nor did Alice think it so _very_ much out of the way to hear the Rabbit say to itself, 'Oh dear! Oh dear! I shall be too late!' (when she thought it over afterwards, it occurred to her that she ought to have wondered at this, but at the time it all seemed quite natural); but when the Rabbit actually _took a watch out of its waistcoat-pocket_, and looked at it, and then hurried on, Alice started to her feet, for it flashed across her mind that she had never before seen a rabbit with either a waistcoat-pocket, or a watch to take out of it, and burning with curiosity, she ran across the field after it, and was just in time to see it pop down a large rabbit-hole under the hedge. In another moment down went Alice after it, never once considering how in the world she was to get out again. The rabbit-hole went straight on like a tunnel for some way, and then dipped suddenly down, so suddenly that Alice had not a moment to think about stopping herself before she found herself falling down what seemed to be a very deep well."

    input_jane_eyre = "Each picture told a story; mysterious often to my undeveloped understanding and imperfect feelings, yet ever profoundly interesting: as interesting as the tales Bessie sometimes narrated on winter evenings, when she chanced to be in good humour; and when, having brought her ironing-table to the nursery hearth, she allowed us to sit about it, and while she got up Mrs. Reed's lace frills, and crimped her nightcap borders, fed our eager attention with passages of love and adventure taken from old fairy tales and other ballads; or (as at a later period I discovered) from the pages of Pamela, and Henry, Earl of Moreland."

    languageModelAlice = StupidBackoffLanguageModel(input_alice)
    vocabAlice = languageModelAlice.unigramCounts.keys()

    input_alice_file = open("test_corpus_download/alice_chapter1", "r")
    input_alice_2 = input_alice_file.read()
    input_alice_2.replace('\n', ' ')

    input_ja_file = open("test_corpus_download/sense_and_sensibility_chapter1", "r")
    input_ja = input_ja_file.read()
    input_ja.replace('\n', ' ')


    print 'Random Alice Text:\n '
    #print randomText(input_alice.split(" "),300)
    #print '\n'
    print randomText(input_alice_2.split(" "),300)
    print '\n'
    
    print 'Random Jane Austin:\n'
    print randomText(input_ja.split(" "),300)
    #print 'Random Jane Eyre Text:\n'
    #print randomText(input_jane_eyre.split(" "), 30)
    #print '\n'
    #print randomText(input_jane_eyre.split(" "), 330)

if __name__ == "__main__":
    main()
