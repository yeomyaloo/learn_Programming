# 배열을 두 그룹으로 나누기

from typing import MutableSequence

def partition(a):
    n = len(a)
    pl = 0
    pr = n-1
    x = a[n//2] #가운데 원소 피벗

    while pl<=pr:
        while a[pl] < x:
            pl+=1
        while a[pl] < x:
            pr-=1
        #피벗기준 왼쪽은 피벗보다 큰거 만나면 멈춰서 if문으로 확인
        #피벗기준 오른쪽은 피벗보다 작은 거 만나면 멈춰서 if문으로 확인해준다.
            
        if pl <= pr:
            #피벗기준으로 나눈 pl pr을 살펴보는 도중 pr이 작고 pl이 큰 경우 두 수를 바꿔준다.
            a[pl],a[pr] = a[pr],a[pl]
            pl += 1
            pr -= 1


           
