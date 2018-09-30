import itertools
import os
import urllib.request

# PREWORK
#urllib.request.urlretrieve('http://bit.ly/2iQ3dlZ', DICTIONARY)

scrabble_scores = [(1, "E A O I N R T L S U"), (2, "D G"), (3, "B C M P"),
                   (4, "F H V W Y"), (5, "K"), (8, "J X"), (10, "Q Z")]
LETTER_SCORES = {letter: score for score, letters in scrabble_scores
                              for letter in letters.split()}


with open("dictionary.txt") as f:
    dictionary = set([word.strip().lower() for word in f.read().split()])


def get_possible_dict_words(draw):
    words = []
    for permutation in _get_permutations_draw(draw):
        if ''.join(permutation) in dictionary:
                words.append(''.join(permutation))
    max_word_value(words)


def letter_value(letter):
    return LETTER_SCORES[letter]


def max_word_value(words):
    max=["", 0]
    for word in words:
        score = calc_word_value(word)
        if score > max[1]:
            max = [word, score]
    return max[0]


def calc_word_value(word):
    word_score = 0
    for character in word:
        if character.isalpha():
            word_score += letter_value(character.upper())
    return word_score


def _get_permutations_draw(draw):
    permutations = []
    for count in range(1, len(draw) + 1):
        for permutation in itertools.permutations(''.join(draw).upper(), count):
            permutations.append(permutation)
    return permutations


if __name__ == '__main__':
	print(get_possible_dict_words(['T', 'I', 'I', 'G', 'T', 'T', 'L']))
