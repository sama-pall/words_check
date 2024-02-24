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

def open_file(in_file) -> list:
    wlist = []
    with open(in_file, 'r') as fh:
        for line in fh.readlines():
            if not line.startswith('#'):
                wlist.append(line.strip().lower().split('\t'))
            else:
                continue

    return wlist


def get_direction_of_translation():
    return bool(random.randint(0,1))


def eng_ru_dir(word, need_to_learn: list) -> list:
    print(word[0])
    print(word[1])
    print(word[4].replace(word[0], '***'))
    if word[3] == input('Enter your translation: '):
        print('Your are right. Well done')
    else:
        print(f'Unfortunately you was wrong. Right answer is {word[4]}')
        need_to_learn.append(word)
    return need_to_learn


def ru_eng_dir(word, need_to_learn: list):
    print(word[3])
    print(word[1])
    print(word[2])
    print(word[4].replace(word[0], '***'))
    if word[0] == input('Enter your translation: '):
        print('Your are right. Well done')
    else:
        print(f'Unfortunately you was wrong. Right answer is {word[0]}')
        need_to_learn.append(word)
    return need_to_learn


def write_file_to_learn(wlist: list):
    with open(wlist, 'w') as file:
        for word in wlist:
            file.write(word)


def main():
    print('Let\'s check you knowledge')
    word_list = open_file(sys.argv[1])

    while len(word_list):
        word = word_list.pop(random.randint(0,len(word_list)))
        need_to_learn = []
        if get_direction_of_translation():
            need_to_learn = ru_eng_dir(word, need_to_learn)
        else:
            need_to_learn = eng_ru_dir(word, need_to_learn)

    print('Congratulation!!! You checked all words')
    write_file_to_learn(need_to_learn)


if __name__ == '__main__':
    main()
