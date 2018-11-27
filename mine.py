#!/usr/bin/env python3

col, row = map(int,input().split())
matrix =[]
for j in range(row):
    matrix.append(list(input()))
for i in range(row):
    for j in range(col):
        count = 0
        if matrix[i][j] == '*':
            print('*',end='')
        else:
            if ((i-1)>=0):
                if (matrix[i-1][j-1] == '*') and ((j-1)>=0):
                    count += 1
                if (matrix[i-1][j] == '*'):
                    count += 1
                if ((j+1)<col) and (matrix[i-1][j+1] == '*'):
                    count += 1
            if (matrix[i][j-1] == '*') and ((j-1)>=0):
                count += 1
            if ((j+1)<col) and (matrix[i][j+1] == '*'):
                count += 1
            if ((i+1)<row):
                if (matrix[i+1][j-1] == '*') and ((j-1)>=0):
                    count += 1
                if (matrix[i+1][j] == '*'):
                    count += 1
                if ((j+1)<col) and (matrix[i+1][j+1] == '*'):
                    count += 1
            print(count,end='')
    print()

