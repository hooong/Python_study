#!/usr/bin/env python3

count = int(input())
for i in range(1,count+1):
    for j in range(count-i,0,-1):
        print(' ',end='')
    for k in range(1,i*2):
        print('*',end='')
    print()