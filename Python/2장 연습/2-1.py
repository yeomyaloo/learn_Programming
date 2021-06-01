

for _in range(1,4):
    a =list(input())



def max_of(a):

    maximum = a[0]
    for i in range(1,len(a)):
        if a[i]>maximum:
            maximum = a[i]


print(f"최댓값은 {a}입니다.")
