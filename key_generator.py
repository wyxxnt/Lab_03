import random

def generateKey(length, characters):
    key = ""
    i = 0
    while i < length:
        num = random.randint(0, len(characters) - 1)
        key = key + characters[num]
        i = i + 1
    return key

characters = "abcdefghijklmnopqrstuvwxyz0123456789"
key = generateKey(16, characters)
print(key)
