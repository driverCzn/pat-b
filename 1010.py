#!/usr/bin/env python
# encoding: utf-8
import re


def process(x, y):
    return x * y, y - 1


r = re.compile(r'([-\w]+)\s([-\w]+)')
l = re.findall(r, input())
l = [(int(x), int(y)) for x, y in l]
li = []
flag = 1  # must use a flag to indicate no non-zero pair
for x, y in l:
    if x and y:
        # li += list([lambda a, b:(a * b, b - 1), x, y])
        li += process(x, y)
        flag = 0
# li = [process(x, y) for x, y in l if y]
if flag:
    print('0 0')
# elif l[-1] == (0, 0):
    # print(' '.join([str(i) for i in li]), end='')
    # print(' 0 0')
else:
    print(' '.join([str(i) for i in li]))
