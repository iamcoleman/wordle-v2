import re
from random import shuffle


def create_wordlist():
    six_boys = []
    with open('en_US-custom.dic', encoding='utf-8') as f:
        for line in f:
            words = line.split('/')
            if re.match(r'^\w{6}$', words[0]):
                # print(words[0])
                six_boys.append(words[0].lower().replace('\n', ''))
    print(six_boys)
    shuffle(six_boys)
    print(six_boys)
    shuffle(six_boys)
    print(six_boys)
    print(len(six_boys))


if __name__ == '__main__':
    create_wordlist()
