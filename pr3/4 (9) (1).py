# -*- coding: utf-8 -*-
"""4

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1bTHrmvMCJg6DlqutZnc8mfq5cxldrcv9
"""

a = input()
b = int(input())
c = a.split()
d = dict()
e = dict()
for index,item in enumerate(c):
    d[int(item)]=index
for i in d.keys():
    f = b - i
    if f in d and f!=i:
        summ = d[i]+d[f]
        if (f,i) not in e.keys():
            e[(i,f)]=summ
g = sorted(e.values())
if not e:
    print("Not Found!")
else:
    for x in g:
        print(x)