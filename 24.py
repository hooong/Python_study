#!/usr/bin/env python3

a = input()
words = list(a.split())
count = 0
for i in words:
    i = i.strip(',.')
    if i == 'the':
        count += 1
print(count)
