import os
import random
import string

for n in range(3):
    
    filename = "D:\\IR\\project final\\project" + str(n) + ".txt"
    afile = open(filename, "w+" )

    for i in range(int(10)):
        line =''.join([random.choice(string.ascii_letters[26:32])])
        afile.write(line)
        print(line)