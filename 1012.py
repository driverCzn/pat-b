#!/usr/bin/env python
# encoding: utf-8
input_list = [i for i in map(lambda x: int(x), input().split())]
input_list = input_list[1: 1 + input_list[0]]
A1, A2, A3, A4, A5 = (0,) * 5
flag_A2 = False
exist_A2 = False
count_A4 = 0
for i in input_list:
    remainder = i % 5
    if remainder == 1:  # n1 + (-n2) + n3 + (-n4) + ...
        # A2 += -i if flag_A2 else i
        if flag_A2:
            A2 += -i
            flag_A2 = False
        else:
            A2 += i
            flag_A2 = True
        exist_A2 = True  # ensure A2 is printed if sum(i % 5 == 1) is 'ZERO'
    elif remainder == 2:  # count
        A3 += 1
    elif remainder == 3:  # sum
        A4 += i
        count_A4 += 1
    elif remainder == 4:  # bigest
        if i > A5:
            A5 = i
    else:  # sum of even numbers
        if i % 2 == 0:
            A1 += i

if count_A4:
    A4 = round(A4 / count_A4, 1)

a = []
for i in A1, A2, A3, A4, A5:
    if i:
        a.append(i)
    else:
        a.append('N')

if exist_A2:
    a[1] = A2
print(' '.join([str(i) for i in a]))
