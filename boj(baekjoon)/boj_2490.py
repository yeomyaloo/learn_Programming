lst = []

for i in range(3):
    lst = list(map(int,input().split()))

    if lst.count(1) == 3:
        print("A")
    elif lst.count(1) == 2:
        print("B")
    elif lst.count(1) == 1:
        print("C")
    elif lst.count(1) == 0:
        print("D")
    elif lst.count(1) == 4:
        print("E")
    
    
