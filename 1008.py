#!/usr/bin/env python
# encoding: utf-8

length, number = (int(i) for i in input().split())
# print(type(length), type(number))
# print(length, number)
l = list(input().split())
# print(l)
for i in range(number):
    poped_number = l.pop()
    l.insert(0, poped_number)
print(' '.join(l))
