#문자열로 이어붙이고 int형으로 강제 형변환해서 진행?

import sys
input = sys.stdin.readline

n = int(input())
a = {'A':'9','B':'4','C':'8','D':'6','E':'5','F':'3','G':'7'}
s = []

for _ in range(n):
    s.append(input())

