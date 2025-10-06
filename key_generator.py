import random

def make_key(size, chars):
    key = ""
    i = 0
    while i < size:
        num = random.randint(0, len(chars) - 1)
        key = key + chars[num]
        i = i + 1
    return key

letters = "abcdefghijklmnopqrstuvwxyz0123456789"
my_key = make_key(16, letters)
print(my_key)

short_key = make_key(8, letters)
print(short_key)
