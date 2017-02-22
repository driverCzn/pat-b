#!/usr/bin/env python
# encoding: utf-8
n = int(input())
l = []
d = {True: 'true', False: 'false'}
for i in range(n):
    # a, b, c = input().split()
    # print(a, b, c)
    a, b, c = map(lambda x: int(x), input().split())
    # print('a = {}, b = {}, c = {}'.format(a, b, c))
    # print('type a = {}, type b = {}, type c = {}'.format(type(a), type(b), type(c)))
    l.append(a + b > c)
    # print(a + b > c)
    # print(l)

# print('len(l) = ', len(l))
for i in range(len(l)):
    print('Case #{}: {}'.format(i + 1, d[l[i]]))
