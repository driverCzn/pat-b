#!/usr/bin/env python
# encoding: utf-8
import re
pattern = re.compile(r'[A]*PA+T[A]*')
number = int(input())
result_list = []
while number > 0:
    ui = input()
    st = re.search('T', ui)
    sp = re.search('P', ui)
    if re.search(pattern, ui)\
    and not re.findall(r'[^PAT]', ui)\
    and st\
    and sp\
    and (len(ui)-1 - st.start()) == sp.start() * (st.start() - sp.start() - 1):
        result_list.append('YES')
    else:
        result_list.append('NO')
    number -= 1
print('\n'.join(result_list))
