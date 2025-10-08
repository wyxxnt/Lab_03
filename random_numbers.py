import random
import math

def random_func(min_val=None, max_val=None):
    if max_val is None and min_val is not None:
        max_val = min_val
        min_val = 0
    elif min_val is None and max_val is None:
        return random.random()
    
    result = random.random() * (max_val - min_val) + min_val
    return math.floor(result)

print(random_func(5, 15))
print(random_func(20))
print(random_func(1, 100))
