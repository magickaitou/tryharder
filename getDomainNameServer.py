data = ['\x1a',
 'M',
 '_',
 'D',
 ']',
 '^',
 'P',
 '.',
 '4',
 '\x13',
 'Z',
 'M',
 'V',
 'U',
 'D',
 'K',
 '5',
 '0',
 'R',
 'I',
 'J',
 'Q',]
 
a = '[RYL\H(9'
b = '*%<>()[]|'

array = []
array2 = []
for char in a:
    array.append(char)
for char in b:
    array2.append(char)
for char in data:
    array.append(char)
# print(array)
# print(array2)
length = len(array)
# print(length)
result = ""
# pswzServerName[i] ^= byte_41D8C8[(int)i % 9];
for i in range (0, length):
    j = i%9
    tmp = ord(array[i]) ^ ord(array2[j])
    result = result + chr(tmp)
print("Domain name of server is: " + result)
# Domain name of server is: qwertasdfgzxcvyuiophjklbnm.com
