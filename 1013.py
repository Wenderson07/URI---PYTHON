# -*- coding:utf-8 -*-
a = input()
b = input()
c = input()
maior_ab = (a + b + abs(a-b))/2
maior_c = (maior_ab + c + abs(maior_ab - c )) /2

print "%d eh o maior" %maior_c
