'''
    This program is used to find content of C:\ProgramData\0001
'''
str_byte_403000 = "PNUDWNZANXCAVMVWSFHFMVOFRGPKRBHR"
str_byte_403029 = "TRYHARDERTRYHARDERTRYHARDERTRYHA"

buffer = ""

'''
        v4 = (unsigned __int8)*(&Buffer + i);
        v3 = (unsigned __int16)(v4 + (unsigned __int8)byte_403029[i] - 0x82) % 0x1Au + 0x41;
        v2 = (unsigned __int8)byte_403000[i] < v3;
        if ( byte_403000[i] != v3 || v4 < 0x41u || v4 > 0x5Au )
'''

for i in range(0,0x20):
    tmp = ord(str_byte_403000[i]) - 0x41 + 0x82 - ord(str_byte_403029[i])
    if (tmp<0x41): tmp = tmp + 0x1A
    buffer = buffer+ chr(tmp)
print(buffer)

# buffer: WWWWWWWWWELCOMETOOOOOOOOOCYRADAR # 
