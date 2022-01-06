# 힙정렬 알고리즘

def heap_sort(a):

    def down_heap(a,l,r):
        temp = a[l]

        parent = l
        while parent < (r + 1) // 2:
            cl = parent * 2 + 1
            cr = cl + 1
            child = cr if cr < r and a[cr] > a[cl] else cl
            if temp >= a[child]:
                break
            a[parent] = a[child]
            parent = child
        a[parent] = temp

    n = len(a)

    # a[i] ~ a[n-1]을 힙으로 만들기
    for i in range((n-1)//2,-1,-1):
        down_heap(a,i,n-1)

    # 최댓값인 a[0]과 마지막 원소를 교환
    for i in range(n-1,0,-1):
        a[0],a[i] = a[i], a[0]
        down_heap(a,0,i-1)
        

print("힙 정렬을 수행합니다.")
num = int(input("원소 수를 입력하세요:"))
x = [None] * num
for i in range(num):
    x[i] =int(input(f"x[{i}]: "))
heap_sort(x)

print("오름차순으로 정렬했습니다.")
for i in range(num):
    print(f"x[{i}] = {x[i]}")
