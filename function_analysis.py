def count_args(func):
    import inspect
    sig = inspect.signature(func)
    return len(sig.parameters)

def check_functions(obj):
    result = []
    for key in obj:
        if callable(obj[key]):
            args_num = count_args(obj[key])
            result.append([key, args_num])
    return result

def func1(x):
    return x

def func2(x, y):
    return x + y

def func3(x, y, z):
    return x + y + z

my_obj = {
    "f1": func1,
    "f2": func2, 
    "f3": func3,
    "data": 123
}

info = check_functions(my_obj)
print(info)
