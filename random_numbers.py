import random
import math


def random_value(min_value, max_value=None):
    if max_value is None:
        max_value = min_value
        min_value = 0
    if max_value < min_value:
        temp = min_value
        min_value = max_value
        max_value = temp
    raw = random.random()
    scaled = raw * (max_value - min_value) + min_value
    return math.floor(scaled)


def show_random_examples():
    print("случайное 5-15:", random_value(5, 15))
    print("случайное до 20:", random_value(20))
    print("случайное 0-1:", random_value(0, 2))


if __name__ == "__main__":
    show_random_examples()
