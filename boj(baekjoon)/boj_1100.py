Map = []
result = 0 
for _ in range(8):
    Map.append(list(input()))

for i in range(8):
    for j in range(8):
        if i%2 == 0 and j%2 == 0 and Map[i][j] == "F":
            result += 1
        elif i%2 == 1 and j%2 == 1 and Map[i][j] =="F":
            result += 1
print(result)
