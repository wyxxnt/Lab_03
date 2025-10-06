import random

def my_random(a, b):
    x = random.random()
    result = x * (b - a) + a
    return int(result)

def my_random_max(max_num):
    x = random.random()
    result = x * max_num
    return int(result)

print(my_random(1, 10))
print(my_random_max(50))
print(my_random(10, 20))
print("тест:", my_random(5, 15))
