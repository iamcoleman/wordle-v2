import re
from random import shuffle


def create_wordlist():
    six_boys = []
    with open('en_US-custom-35.dic', encoding='utf-8') as f:
        for line in f:
            words = line.split('/')
            if re.match(r'^\w{6}$', words[0]):
                # print(words[0])
                six_boys.append(words[0].lower().replace('\n', ''))
    # print(six_boys)
    # shuffle(six_boys)
    # print(six_boys)
    # shuffle(six_boys)
    print(six_boys)
    print(len(six_boys))


def create_medium_wordlist():
    six_men = []
    with open('en_US-custom-50.dic', encoding='utf-8') as f:
        for line in f:
            words = line.split('/')
            if re.match(r'^\w{6}$', words[0]):
                # skip all the uppercase words (pronouns and such)
                if words[0][0].isupper():
                    continue
                # skip (some of) the naughty words
                if len(words) > 1 and '!' in words[1]:
                    continue
                six_men.append(words[0].lower().replace('\n', ''))
    print(six_men)
    print(len(six_men))
    shuffle(six_men)
    print(six_men)
    shuffle(six_men)
    print(six_men)
    shuffle(six_men)
    print(six_men)


def create_long_wordlist():
    six_fellas = []
    with open('en_US-custom-60.dic', encoding='utf-8') as f:
        for line in f:
            words = line.split('/')
            if re.match(r'^\w{6}$', words[0]):
                # skip all the uppercase words (pronouns and such)
                if words[0][0].isupper():
                    continue
                # skip (some of) the naughty words
                if len(words) > 1 and '!' in words[1]:
                    continue
                six_fellas.append(words[0].lower().replace('\n', ''))
    print(six_fellas)
    print(len(six_fellas))


def create_acceptable_guesses():
    six_gods = []
    with open('en_US-custom-70.dic', encoding='utf-8') as f:
        for line in f:
            words = line.split('/')
            if re.match(r'^\w{6}$', words[0]):
                # skip all the uppercase words (pronouns and such)
                # if words[0][0].isupper():
                #     continue
                # skip (some of) the naughty words
                if len(words) > 1 and '!' in words[1]:
                    continue
                six_gods.append(words[0].lower().replace('\n', ''))
    print(six_gods)
    print(len(six_gods))


if __name__ == '__main__':
    # create_wordlist()
    # create_medium_wordlist()
    # create_long_wordlist()
    create_acceptable_guesses()
