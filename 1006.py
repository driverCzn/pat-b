#!/usr/bin/env python
# encoding: utf-8
data = input()[::-1]
data_len = len(data)
result = []
result += ''.join([str(i + 1) for i in range(int(data[0]))])
if data_len >= 2:
    result.insert(0, 'S' * int(data[1]))
    if data_len == 3:
        result.insert(0, 'B' * int(data[2]))
print(''.join(result))
