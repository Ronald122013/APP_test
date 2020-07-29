#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
七进制数相加

输入是两个七进制

输出也是七进制
'''

# 其他进制转化为十进制
def seven2int(n):
    s = 0
    l = list(str(n))
    l1 = [int(i) for i in l]
    for j in range(len(l1)) :
        s += l1[j]*7**(len(l1)-j-1)
    return s


# 十进制转化为其他进制
lis = []
def int2seven(n):
    n1 = n % 7
    n2 = n // 7
    lis.append(n1)
    if n1 != 0:
        int2seven(n2)
    else:
        a = [str(i) for i in lis[-2::-1]]
        global b
        b = int(''.join(a))
    return b




