import random


def choose_random(choices):
    return random.choice(choices)


def generate_random():
    num = 2
    if random.randint(1, 3) == 1:
        num = 4
    return num
