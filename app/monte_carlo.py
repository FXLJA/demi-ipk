import random


def generate(probability, n=1):
    result = []
    for _i in range(n):
        result += [test_success(probability)]
    return result


def test_success(probability):
    return random.random() < probability