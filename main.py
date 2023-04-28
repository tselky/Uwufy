########################################################################################################################
# A silly script that takes any text and uwufies it.
# Don't take this too seriously, its silly fun!
# TODO: Make the uwu probability more impactful
########################################################################################################################

import random
import json
import random
import numpy.random


uwu_probability = 0.06


def uwufy_text(text, uwu_probability):
    """
    Takes in a text string, probability (a float between 0 and 1)
    Swaps some words around using a predefined (customizable) dictionary and uwufies the output.
    Depending on the probability, may misspell or make other changes such as exaggerating adjectives or adding typos.
    """
    start = ''
    with open('finalDict.json', 'r') as f:
        final_dict = json.load(f)
    # PRE-SPLIT
    text = text.lower().replace("'", "")
    uwutext = blankify(text)
    float = random.random()
    # POST-SPLIT
    words = uwutext.split()
    for i in range(len(words)):
        if float < uwu_probability:
            # randomly misspell the word
            words[i] = clutzify(words[i])
        elif words[i] in final_dict:
            # Replace the word with a random mispronunciation
            mispronunciations = random.choice(final_dict[words[i]])

            words[i] = mispronunciations
        words[i] = energize(words[i])
        words[i] = ditzify(words[i])
        words[i] = exaggerate(words[i])

    if float > 0.2:
        finisher = ["hehe", ":3", "uwu", "lolol", "!!!!!!", "ahahaha", ":^)", "owo"]
        words.append(numpy.random.choice(finisher))

    if float > 0.5:
        starter = ["omg so ", "ok so ", "dude ok so ", "yo wait so like ", "like ", "well "]
        start = (numpy.random.choice(starter))

    uwutext = start+' '.join(words)
    print("uwu Float: ", float)
    return uwutext


def translate(text):
    with open('finalDict.json', 'r') as f:
        final_dict = json.load(f)
    words = text.split()
    print(words)
    for i, word in enumerate(words):
        if word in final_dict:
            print(word)
            # Replace the word with a random mispronunciation
            mispronunciations = random.choice(final_dict[word])

            words[i] = mispronunciations
    return ' '.join(words)


def clutzify(word):
    """
    Takes in a word string and randomly misspells it. Has room for improvement
    """
    # randomly choose a number of letters to delete or add
    num_changes = random.randint(-1, 2)
    if num_changes < 0:
        # randomly delete letters
        indices = random.sample(range(len(word)), abs(num_changes))
        return ''.join([c for i, c in enumerate(word) if i not in indices])
    elif num_changes > 0:
        # randomly add letters
        indices = sorted(random.sample(range(len(word) + num_changes), num_changes))
        added_chars = [random.choice('abcdefghijklmnopqrstuvwxyz') for i in range(num_changes)]
        return ''.join([added_chars.pop(0) if i in indices else c for i, c in enumerate(word + ' ')])
    else:
        return word

# Swaps s -> z
# Swaps ie -> ei
def ditzify(word):
    if word.endswith('s'):
        word = word[:-1] + 'z'
    if 'ie' in word:
        word = word.replace('ie', 'ei')
    return word

# Sometimes stretches out vowels depending on probability setting
def energize(word):
    vowels = 'aeiou'

    if len(word) != 2 or word[0] in vowels or word[1] not in vowels:
        return word

    num_vowels = random.randint(0, 2)
    extra_vowels = word[1] * num_vowels
    new_word = word + extra_vowels

    return new_word

# Adds filler sometimes depending on probability setting
def blankify(text):
    fillers = ['like', 'um', 'uh',]
    new_text = []
    words = text.split()
    for i in range(len(words)):
        new_text.append(words[i])
        if random.randint(1, 15) == 1:
            filler = numpy.random.choice(fillers, p=[0.4, 0.3, 0.3])
            new_text.append(filler)
    return ' '.join(new_text)

# Adds more exaggeration before adjectives sometimes depending on probability
def exaggerate(word):
    fillers = ["uber ", "super ", "totally ", "like super ", "rly ", "like rly ", "amazingly ", "super duper "]
    with open("mostly-adjectives.txt", 'r') as file:
        for line in file:
            if line.strip() == word:
                word = random.choice(fillers)+word
                return word
                break
        return word




# EXAMPLE OUTPUT: omg so i saw a amazingly red car drive by! ahahaha
text = "I saw a red car drive by!"
x = 1

for i in range(x):
    print(uwufy_text(text, uwu_probability)+"\n")


