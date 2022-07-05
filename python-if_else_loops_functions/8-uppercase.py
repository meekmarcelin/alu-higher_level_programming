#!/usr/bin/python3
def uppercase(str1):
    for i in str1:
        i = ord(i)
        if 97 <= i <= 122:
            i = i - 32
            print("{:c}".format(i), end='')
    print("")
