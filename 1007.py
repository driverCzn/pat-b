#!/usr/bin/env python
# encoding: utf-8
# generate the prime list within sqrt(n) (the maximin prime in the list < sqrt(n) + 1)
# generate the full prime list using `sieve of Eratosthenes`
# count number of prime pairs
import math


def prime_list(n):
    p_l = [True] * (n + 1)
    p_l[0], p_l[1] = [False] * 2
    prime_index_set = list(filter(lambda x: all(map(lambda p: x % p != 0, range(2, x))), range(2, int(math.sqrt(n) + 1))))
    # print(list(prime_index_set))
    # if not 2 in prime_index_set:
        # prime_index_set += [2]
    for i in prime_index_set:
        temp = i
        while i + temp <= n:
            p_l[i + temp] = False
            temp += i
    count = 0
    # print(p_l)
    for i in range(len(p_l) - 2):
        if p_l[i] & p_l[i + 2]:
            count += 1
    print(count)
if __name__ == "__main__":
    prime_list(int(input()))
