#!/usr/bin/env python
# encoding: utf-8
#input table
# sort the table
#print the first and the last
import re
pat = re.compile(r'([\w]+)[\s]([\w]+)[\s]([\w]+)')
n = int(input())
table = []
while n:
    table.append(re.search(pat, input()).groups())
    n -= 1
table = sorted(table, key=lambda t: int(t[2]), reverse=True)
print(table[0][0], table[0][1])
print(table[-1][0], table[-1][1])
