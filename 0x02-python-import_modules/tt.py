#!/usr/bin/python3

from add_0 import *

al = globals()
print(al)
for k, v in al.items():
    if callable(add_0.k):
	    print(k)


