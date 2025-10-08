
def list_function_info(iface):
    details = []
    for name in iface:
        value = iface[name]
        if callable(value):
            try:
                arg_count = value.__code__.co_argcount
            except AttributeError:
                arg_count = 0
            details.append([name, arg_count])
    return details


def sample_functions():
    def m1(x):
        return [x]

    def m2(x, y):
        return [x, y]

    def m3(x, y, z):
        return [x, y, z]

    return {
        'm1': m1,
        'm2': m2,
        'm3': m3,
        'value': 5,
    }


if __name__ == '__main__':
    info = list_function_info(sample_functions())
    print(info)
