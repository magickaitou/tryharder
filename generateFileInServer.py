import os

filename = "4445534b544f502d3243334951484f"

if os.path.exists(filename):
    os.remove(filename)

a = [105, 124, 110, 126, 108, 104, 9, 112, 16, 75, 73, 75, 95, 90, 76, 118, 21, 41, 100, 113, 13, 112, 111, 15, 26, 19, 61, 102, 125, 111, 16, 123]


with open(filename, "w") as file:
    for char_code in a:
        file.write(chr(char_code))
