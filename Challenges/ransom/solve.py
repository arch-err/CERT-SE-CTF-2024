#!/usr/bin/env python

with open("./RANSOM_NOTE", "r") as f:
    file = f.read()


flag = ""

for char in file:
    if char not in flag:
        flag += char
print(flag)
