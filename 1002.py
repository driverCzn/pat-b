#!/usr/bin/env python
# encoding: utf-8
# return sum([ord(i) for i in user_input])
# print ' '.join([i for i in str(list))

user_input = input()
d = {'0': 'ling',
     '1': 'yi',
     '2': 'er',
     '3': 'san',
     '4': 'si',
     '5': 'wu',
     '6': 'liu',
     '7': 'qi',
     '8': 'ba',
     '9': 'jiu'}
total = sum([ord(i)-ord('0') for i in user_input])
print(' '.join([d[i] for i in str(total)]))
