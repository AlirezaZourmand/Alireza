# -*- coding: utf-8 -*-
"""Q2

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1e8-BrRaG6keQo-r70x8bfOo8WLputlpi
"""

def f(n, s, targetword):
    words = s.split()
    targetwordpattern = targetword.lower()
    result = []
    for word in words:
        cw = word.lower()
        while len(targetwordpattern) > len(cw):
            cw += "_"
        while len(cw) > len(targetwordpattern):
            targetwordpattern += "_"
        d = 0
        for i in range(len(targetwordpattern)):
            if targetwordpattern[i]!=cw[i]:
                d +=1
        if d <= n:
            result.append(word)
    return result
import re
n = int(input())
s = input()[:-1]
s = re.sub(r"[،:؛.؟!٬٫]+","",s)
targetword = input()
output = f(n, s, targetword)
for j in output:
    print(j)