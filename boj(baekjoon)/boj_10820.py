import sys
input = sys.stdin.readline

a = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
b = "abcdefghijklmnopqrstuvwxyz"
num = "1234567890"



while True:
    s = input().rstrip('\n')
    A=B=SPACE=NUM = 0
    
    if not s:
        break
    for i in s:
        if i in a:
            A+=1
        elif i in b:
            B+=1
        elif i in num:
            NUM+=1
        else:
            SPACE +=1

    print(f"{B} {A} {NUM} {SPACE}")
        
