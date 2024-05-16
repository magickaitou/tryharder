# Đây là lấy tên file cần GET
#print(len(a))
b = 'DESKTOP-2C3IQHO'
#print(len(b))
result =  ''
for char in b:
    tmp = str(hex(ord(char)))
    tmp = tmp[2:4]
    result = result + str(tmp)
    #print(tmp)
print("File Name is: " + result)
# File Name is: 4445534b544f502d3243334951484f
