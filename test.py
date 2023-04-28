import json
import random

def replacer(text):
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




print(replace_mispronunciations(text))