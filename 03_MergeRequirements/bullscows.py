import argparse
import random
import sys
from os.path import isfile
from urllib import request as req


def bullscows(guess, secret):
    bulls, cows = 0, 0
    for index, elem in enumerate(guess):
        if elem == secret[index]:
            bulls += 1
        elif elem in secret:
            cows += 1
    return bulls, cows


def gameplay(ask, inform, words):
    wrd = random.choice(words)
    attempt = 1
    user_word = ''
    while user_word != wrd:
        user_word = ask(f'Введите слово: ', words)
        inform('Быки: {}, Коровы: {}', *bullscows(user_word, wrd))
        attempt += 1
    return attempt


def ask(prompt, valid=None):
    word = input(prompt)
    if valid is not None:
        while word not in valid:
            print('Введённого слова нет в словаре')
            word = input(prompt)
    return word


def inform(format_string, bulls, cows):
    print(format_string.format(bulls, cows))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('dict', type=str)
    parser.add_argument('length', nargs='?', default=5, type=int)
    args = parser.parse_args()

    if isfile(args.dict):
        with open(args.dict, 'rb') as f:
            allWords = f.read().decode().split()
    else:
        with req.urlopen(args.dict) as f:
            allWords = f.read().decode().split()

    dictionary = [word for word in allWords if len(word) == args.length]

    if not dictionary:
        print('Запустите игру с меньшей длиной слова')
        exit(0)

    print(f'Вы угадали слово за {gameplay(ask, inform, dictionary)} попыток')