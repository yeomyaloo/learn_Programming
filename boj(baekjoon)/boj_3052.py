n = []

for _ in range(10):
    a = int(input())
    b = a % 42

    n.append(b)

s = set(n) #자료형의 중복을 제거 해주면 결과적으로 겹치는 것은 1개씩만 나오게 됨
print(len(s))
