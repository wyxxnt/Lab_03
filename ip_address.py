def ip_to_num(ip):
    parts = ip.split(".")
    a = int(parts[0])
    b = int(parts[1]) 
    c = int(parts[2])
    d = int(parts[3])
    
    result = a * 256 * 256 * 256 + b * 256 * 256 + c * 256 + d
    return result

print(ip_to_num("127.0.0.1"))
print(ip_to_num("10.0.0.1"))
print(ip_to_num("192.168.1.10"))
print(ip_to_num("0.0.0.0"))
print(ip_to_num("8.8.8.8"))
