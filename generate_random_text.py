import sys
import string
import random

"""
Plan:
    * develop language model
    * train language model on the input data
    * generate output data

"""


def randomText (inputText, length):
    bagOfWords = inputText.split()
    maxIndex = len(bagOfWords) - 1

    randText = []
    for x in range(length):
        randomIndex = random.randint(0,maxIndex)
        randText.append(bagOfWords[randomIndex])

    return " ".join(randText)

def main():
    input_alice = "There was nothing so _very_ remarkable in that; nor did Alice think it so _very_ much out of the way to hear the Rabbit say to itself, 'Oh dear! Oh dear! I shall be too late!'(when she thought it over afterwards, it occurred to her that she ought to have wondered at this, but at the time it all seemed quite natural); but when the Rabbit actually _took a watch out of its waistcoat-pocket_, and looked at it, and then hurried on, Alice started to her feet, for it flashed across her mind that she had never before seen a rabbit with either a waistcoat-pocket, or a watch to take out of it, and burning with curiosity, she ran across the field after it, and was just in time to see it pop down a large rabbit-hole under the hedge."

    input_jane_eyre = "Each picture told a story; mysterious often to my undeveloped understanding and imperfect feelings, yet ever profoundly interesting: as interesting as the tales Bessie sometimes narrated on winter evenings, when she chanced to be in good humour; and when, having brought her ironing-table to the nursery hearth, she allowed us to sit about it, and while she got up Mrs. Reed's lace frills, and crimped her nightcap borders, fed our eager attention with passages of love and adventure taken from old fairy tales and other ballads; or (as at a later period I discovered) from the pages of Pamela, and Henry, Earl of Moreland."

    print 'Random Alice Text:\n '
    print randomText(input_alice,30)
    print '\n'
    print randomText(input_alice,30)
    print '\n'
    print 'Random Jane Eyre Text:\n'
    print randomText(input_jane_eyre, 30)
    print '\n'
    print randomText(input_jane_eyre, 330)

if __name__ == "__main__":
    main()