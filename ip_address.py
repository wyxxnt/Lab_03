def ip_to_number(ip='127.0.0.1'):
    parts = ip.split('.')
    numbers = []
    for part in parts:
        numbers.append(int(part))
    
    result = 0
    for i in range(len(numbers)):
        byte_val = numbers[i]
        shift_count = (3 - i) * 8
        shifted = byte_val << shift_count
        result = result + shifted
    
    return result

def ip_to_number_reduce(ip='127.0.0.1'):
    parts = ip.split('.')
    numbers = [int(part) for part in parts]
    
    total = 0
    for i, byte_val in enumerate(numbers):
        shift_count = (3 - i) * 8
        total += byte_val << shift_count
    
    return total

print('127.0.0.1 ->', ip_to_number('127.0.0.1'))
print('10.0.0.1 ->', ip_to_number('10.0.0.1'))
print('192.168.1.10 ->', ip_to_number('192.168.1.10'))
print('0.0.0.0 ->', ip_to_number('0.0.0.0'))
print('8.8.8.8 ->', ip_to_number('8.8.8.8'))

print()
print('З reduce:')
print('127.0.0.1 ->', ip_to_number_reduce('127.0.0.1'))
print('10.0.0.1 ->', ip_to_number_reduce('10.0.0.1'))
