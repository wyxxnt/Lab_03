import random


def generate_key(length, characters):
    result = ""
    index = 0
    while index < length:
        spot = random_value(0, len(characters))
        if spot >= len(characters):
            spot = len(characters) - 1
        result += characters[spot]
        index += 1
    return result


def random_value(min_value, max_value=None):
    if max_value is None:
        max_value = min_value
        min_value = 0
    value = random.random()
    return int(value * (max_value - min_value) + min_value)


def demo_keys():
    letters = "abcdefghijklmnopqrstuvwxyz0123456789"
    print(generate_key(16, letters))
    print(generate_key(8, letters))
    print(generate_key(4, letters))


if __name__ == "__main__":
    demo_keys()
