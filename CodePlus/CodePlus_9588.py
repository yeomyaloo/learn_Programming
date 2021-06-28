import sys
#골드바흐 추측
def goldbach(n,p):
  m = n//2+1
  for i in range(3,m,2):
    if p[i] == True and p[n-i] == True:#n, n-p가 모두 소수이면
      print(n,'=',i,'+',n-i)
      return
  print("Goldbach\'s conjecture is wrong.")

#에라토스테네스의 체
p = [True]*1000001
for i in range(3,1001,2):
  if p[i] == True:
    for j in range(i**2,1000001,i):
      p[j] = False

#입력
while True:
  n = int(sys.stdin.readline())
  if n == 0:
    break
  else:
    goldbach(n,p)
