def binary_search(m):
    start = 0
    end = n-1
    while start <= end:
        mid = (start + end) // 2
        if card[mid] == m:
            return 1
        elif card[mid] > m:
            end = mid - 1
        else:
            start = mid + 1

    return 0

n = int(input())
card = list(map(int,input().split()))
card.sort()

m = int(input())
a = list(map(int,input().split()))

for i in a:
    print(binary_search(i), end=" ")
