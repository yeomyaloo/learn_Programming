n = int(input())
w = []
result = []
for _ in range(n):
    w.append(int(input()))
w.sort(reverse = True)

for i in range(n):
    result.append(w[i]*(i+1))
print(max(result))
