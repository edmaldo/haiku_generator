import sys
from string import punctuation
import json
from nltk.corpus import cmudict

with open('missing_words.json') as f:
    missing_words = json.load(f)

cmudict = cmudict.dict()


def count_syllables(words):
    """Use corpora to count syllables in English word or phrase."""
    words = words.replace("-", " ")
    words = words.lower().split()
    num_sylls = 0
    for word in words:
        word = word.strip(punctuation)
        if word.endswith("'s"):
            word = word[:-2]
        if word in missing_words:
            num_sylls += missing_words[word]
        else:
            for phonemes in cmudict[word][0]:
                for phoneme in phonemes:
                    if phoneme[-1].isdigit():
                        num_sylls += 1
    return num_sylls


def main():
    while True:
        print("The Syllable Counter\n")
        word = input("Type word or phrase to count its syllables: ")
        if word == '':
            sys.exit()
        try:
            num_syllable = count_syllables(word)
            print(f"Number of syllables in:: {word} = {num_syllable}")
            print()
        except KeyError:
            print("Word not found. Try again.\n", file=sys.stderr)


if __name__ == '__main__':
    main()

