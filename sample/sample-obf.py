import base64

def encode_base64(s):
    return base64.b64encode(s.encode('utf-8')).decode('utf-8')

def decode_base64(s):
    return base64.b64decode(s).decode('utf-8')

# Encoded and obfuscated strings
encoded_strings = {
    'x1': 'Wm9va2VlcGVyJ3MgRGF0YWJhc2U=',
    'x2': 'KioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqCgoxOiAgUHJpbnQgQW5pbWFscyBMaXN0CjI6ICBBZGQgQW5pbWFsCjM6ICBEZWxldGUgQW5pbWFsCjQ6ICBFeGl0CgoqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqCg==',
    'x3': 'UGxlYXNlIG1ha2UgYSBzZWxlY3Rpb246IA==',
    'x4': 'RW50ZXIgbmV3IGFuaW1hbDog',
    'x5': 'QW5pbWFsIG51bWJlciB0byBkZWxldGU6IA==',
    'x6': 'VGlnZXI=',
    'x7': 'Umhpbm8=',
    'x8': 'RWxlcGhhbnQ=',
    'x9': 'T2N0b3B1cw==',
    'x10': 'UG9sYXIgQmVhcg=='
}

a = [
    decode_base64(encoded_strings['x6']),
    decode_base64(encoded_strings['x7']),
    decode_base64(encoded_strings['x8']),
    decode_base64(encoded_strings['x9']),
    decode_base64(encoded_strings['x10'])
]
a.sort()

def b():
    A = 1
    for B in a:
        C = str(A) + ' ' + B
        print(C)
        A += 1

while True:
    print("\n" + decode_base64(encoded_strings['x1']) + "\n" + decode_base64(encoded_strings['x2']))
    f = input(decode_base64(encoded_strings['x3']))
    if f == '1':
        b()
    elif f == '2':
        g = input(decode_base64(encoded_strings['x4']))
        a.append(g)
        a.sort()
    elif f == '3':
        b()
        h = int(input(decode_base64(encoded_strings['x5']))) - 1
        del a[h]
    elif f == '4':
        break
