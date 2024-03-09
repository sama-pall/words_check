"""
    Program should get words from file (csv, txt) |database
    make list (other container ?) of them
    every line should contain:
    eng_word part_of_speach transcription ru_word ex1_eng .... ex1_ru
    program randomly should choose direction of translation eng-ru or ru-eng
    after that it should print word, examples and make inquiry for translation
    if compared translation is right move-on, if wrong add it to need_to_learn list -> file, base

    should run till all words are checked
    1st iteration cli , 2nd GUI tkinter
"""
import random
import sys
from datetime import datetime


def open_file(in_file) -> list:
    wlist = []
    with open(in_file, 'r', encoding='utf-8') as fh:
        for line in fh.readlines():
            if not line.startswith('#'):
                wlist.append(line.strip().lower().split('\t'))
            else:
                continue

    return wlist


def get_direction_of_translation():
    return bool(random.randint(0, 1))


def eng_ru_dir(word, need_to_learn: list):
    print(word[0])
    print(word[1])
    print(word[4].replace(word[0], '***'))
    answer = input('Enter your translation: ').strip().encode("utf-8")
    if word[3] == answer:
        print('Your are right. Well done')
    else:
        print(f'Unfortunately you was wrong. Right answer is {word[3]}')
        need_to_learn.append(word)


def ru_eng_dir(word, need_to_learn: list):
    print(word[3])
    print(word[1])
    print(word[4].replace(word[0], '***'))
    answer = input('Enter your translation: ').strip().encode("utf-8")
    if word[0] == answer:
        print('Your are right. Well done')
    else:
        print(f'Unfortunately you was wrong. Right answer is {word[0]}')
        need_to_learn.append(word)


def write_file_to_learn(name: str, wlist: list):
    with open(name, 'a') as file:
        file.write(datetime.now().strftime("%Y-%m-%d %H-%M-%S") + '\n')
        for word in wlist:
            file.write(','.join(word) + '\n')

def main():
    print('Let\'s check you knowledge')
    word_list = open_file(sys.argv[1])
    print(*[len(word) for word in word_list])
    need_to_learn = []
    while len(word_list):
        word = word_list.pop(random.randint(0, len(word_list) - 1))

        if get_direction_of_translation():
            ru_eng_dir(word, need_to_learn)
            print()
        else:
            eng_ru_dir(word, need_to_learn)
            print()
    print('Congratulation!!! You checked all words')
    print(need_to_learn)
    name = 'words_to_revice.txt'
    write_file_to_learn(name, need_to_learn)


if __name__ == '__main__':
    main()
