#!/usr/bin/env python
# encoding: utf-8
# the same as 1001, but I stuck in this for hours...

def get_number(n):
    if n % 2 == 0:
        return n / 2
    else:
        return (3 * n + 1) / 2

n = int(input())
number_list = [int(i) for i in input().split()]
data = number_list[:]


for i in data:
    while not i == 1:
        i = get_number(i)
        if i in number_list:
            number_list.remove(i)
number_list.sort(reverse=True)
print(' '.join([str(i) for i in number_list]))
