s = input()
result = [0]*26 #알파벳 개수만큼 리스트 선언

for i in s:
    result[ord(i)-97] = s.count(i)
for i in result:
    print(i, end =" ")
