import os


def read_and_print(filename: str) -> None:
    with open(filename, "r") as file:
        for line in file:
            print(line)


def read_and_count(filename: str) -> None:
    with open(filename, "r") as file:
        count = 1
        for line in file:
            if line[0] != "T":
                print(count)
                break
            count += 1


def count_words(filename: str) -> None:
    with open(filename, "r") as file:
        words = 0
        for line in file:
            words += len(line.split())
        print(words)

def count_the(filename: str) -> None:
    with open(filename, "r") as file:
        the = 0
        for line in file:
            for word in line.split():
                if word == 'the':
                    the += 1
        print(the)



def display_words(filename: str) -> None:
    with open(filename, "r") as file:
        for line in file:
            for word in line.split():
                if len(word) < 4:
                    print(word)



def count_words(filename):
    with open(filename, "r") as file:
        this_these = 0
        for line in file:
            for word in line.split():
                if word == 'these' or word == 'this':
                    this_these += 1
        print(this_these)



def count_ewords(filename: str) -> None:
    with open(filename, "r") as file:
        e = 0
        for line in file:
            for word in line.split():
                if word[-1] == 'e':
                    e += 1
        print(e)

def count_upper(filename: str) -> None:
    with open(filename, 'r') as file:
        count = 0
        for line in file:
                for word in line.split():
                    for letter in word:
                        if letter.isupper():
                            count += 1
        print(count)

def hash_display(filename) -> None:
    with open(filename, 'r') as file:
        text = file.read()
        for letter in text:
            print(letter + '#', end='')

pwd = os.path.dirname(__file__)
absolute_path = os.path.join(pwd, "sample.txt")

read_and_print(absolute_path)
read_and_count(absolute_path)
count_words(absolute_path)
count_the(absolute_path)
display_words(absolute_path)
count_words(absolute_path)
count_ewords(absolute_path)
count_upper(absolute_path)
hash_display(absolute_path)
