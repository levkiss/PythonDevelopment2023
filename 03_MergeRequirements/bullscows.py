import argparse
import random
import sys
from cowsay import cowsay, list_cows
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
    word = input(cowsay.cowsay(prompt, cowfile=getcow_random()) + '\n\n')
    if valid is not None:
        while word not in valid:
            print(cowsay.cowsay('Введённого слова нет в словаре', cowfile=getcow_random()) + '\n\n')
            word = input(cowsay.cowsay(prompt, cowfile=getcow_random()) + '\n\n')
    return word


def getcow_random() -> str:
    return random.choice(list_cows())


def inform(format_string, bulls, cows):
    message = cowsay(format_string.format(bulls, cows), cow=getcow_random()) + '\n'
    print(message)


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