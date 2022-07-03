#!/usr/bin/python3
for i in range(ord('a'), ord('z')+1):
    celin = chr(i)
    if celin not in "qe":
        print("{:s}".format(celin), end="")
