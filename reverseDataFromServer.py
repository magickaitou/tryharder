'''
    Reverse Program
        1. Dst_string => Index 
        2. Len of dst_string + add index 
        3. Eight characters of dst_string => five_array
        4. Five_array => string 
'''

# Variables:
dst_arr = ['33', '42', '51', '57', '50', '30', '4B', '38', '23', '4C', '4E', '56', '4C', '51', '58', '44', '44', '40', '36', '32', '59', '54', '50', '44', '46', '23', '4C', '42', '58', '5A', '4B', '42', '4B', '4B', '4D', '47', '57', '4D', '57', '38', '47', '42', '4A', '24', '4E', '44', '46', '42', '4B', '54', '4E']
xor_string = '*%<>()[]|'
string = "0#23WXYZ89BCDFGHJKLMNPQR$TV@567!1111111144444444"

length = len(dst_arr)

xor_string_arr = []
length_xor_str = len(xor_string)
for i in xor_string:
    xor_string_arr.append(i)
    
t = length % 8
if (t != 0):
    arr = ['30' for _ in range(8-t)]    
    dst_arr.extend(arr)
#print(dst_arr)

dst_arr_xl = []
for i in dst_arr:
    tmp = int(i,16)
    dst_arr_xl.append(chr(tmp))
#print(dst_arr_xl)

index = []
for i in dst_arr_xl:
    tmp = string.find(i)
    index.append(tmp)
#print(index)

'''
     index => bin
'''
bin_arr = []
for i in index:
    tmp = (bin(i))
    tmp = tmp[2:]
    if (len(tmp)!=8):
        tmp = (8-len(tmp))*'0' + tmp
    bin_arr.append(tmp)
#print(bin_arr)
#print(len(bin_arr))
number_eight_arr = len(bin_arr)//8

xor_file_bin = []

'''
    Eight to five character 
    Input: array has 8 characters
'''

def eight_to_five(arr_bin_eight):
    five_arr_bin = [-1 for _ in range(5)]
    five_arr_bin[0] = arr_bin_eight[1][5:] + arr_bin_eight[0][3:]
    five_arr_bin[1] = arr_bin_eight[3][7:]+arr_bin_eight[2][3:] + arr_bin_eight[1][3:5]
    five_arr_bin[2] = arr_bin_eight[4][4:]+arr_bin_eight[3][3:7]
    five_arr_bin[3] = arr_bin_eight[6][6:]+arr_bin_eight[5][3:] + arr_bin_eight[4][3]
    five_arr_bin[4] = arr_bin_eight[7][3:]+arr_bin_eight[6][3:6]
    return five_arr_bin

for i in range(number_eight_arr):
    arr_bin_eight = []
    for j in range(i*8, i*8 + 8):
        arr_bin_eight.append(bin_arr[j])
    five_arr_bin = eight_to_five(arr_bin_eight)
    xor_file_bin.extend(five_arr_bin)
# print(xor_file_bin)

xorfile = []

for i in xor_file_bin:
    tmp = int(i, 2)
    xorfile.append(tmp)
print("List ascii number of processed data from server after the first procession: ")
print(xorfile)

processedDataFromServer = ""
for i in xorfile:
    processedDataFromServer += chr(i)
print("\nprocessedDataFromServer after the first procession: " + processedDataFromServer)
    
def xor_file(data):
    xor_file_arr = []
    k = 0
    for i in data:
        j = k % length_xor_str
        tmp = i ^ ord(xor_string_arr[j])
        k = k+1
        xor_file_arr.append(tmp)
    return xor_file_arr

data_arr = xor_file(xorfile)
# print(data_arr)
# 2 3 5 7 8
if(t==7):
    # Remove 1 character
    data_arr = data_arr[:-1]
elif(t==5):
    # Remove 2 characters
    data_arr = data_arr[:-2]
elif(t==3):
    # Remove 3 characters
    data_arr = data_arr[:-3]
elif(t==2):
    # Remove 4 characters
    data_arr = data_arr[:-4]
print("\nList ascii number of data characters from server:  ")
print(data_arr)
    

