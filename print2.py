#!/usr/bin/env python3

a,b,c,d = map(int,input().split())
if (a<0 or a>100) and (b<0 or a>100) and (c<0 or c>100) and (d<0 or d>100):
    print('잘못된 점수')
else:
    f = (a+b+c+d)//4
    if f>=80:
        print('합격')
    else:
        print("불합격")
