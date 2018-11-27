#!/usr/bin/env python3

price = input()
prices = map(int,price.split(';'))
for i in prices:
    print(i)