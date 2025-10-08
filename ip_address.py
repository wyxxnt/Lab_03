from functools import reduce


def ip_to_number(address='127.0.0.1'):
    parts = address.split('.')
    numbers = []
    for item in parts:
        if item == '':
            numbers.append(0)
        else:
            numbers.append(int(item))
    while len(numbers) < 4:
        numbers.append(0)
    limited = numbers[:4]

    def shift(total, value):
        return (total << 8) + value

    return reduce(shift, limited, 0)


def show_ip_examples():
    samples = [
        '127.0.0.1',
        '10.0.0.1',
        '192.168.1.10',
        '165.225.133.150',
        '0.0.0.0',
        '8.8.8.8',
    ]
    for ip in samples:
        print(ip, '->', ip_to_number(ip))


if __name__ == '__main__':
    show_ip_examples()
