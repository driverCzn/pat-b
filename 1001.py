#!/usr/bin/env python
# encoding: utf-8
#n is even return n/2
#n is not even return (3n+1)/2

user_input = int(input())
count = 0
while True:
    if user_input == 1:
        break
    elif user_input % 2 == 0:
        user_input /= 2
        count += 1
    else:
        user_input = (3 * user_input + 1) / 2
        count += 1

print(count)
