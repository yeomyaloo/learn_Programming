# 6,9 묶음으로 cnt + 1씩 해주고 마지막에 2로 나눈 몫을 취한다
# 다른 수들은 그냥 1씩 증가 시켜준다

n = input()

roomNumber = [0] * 10

for i in n:
    if i == '6' or i == '9':
        if roomNumber[6] == roomNumber[9]:
            roomNumber[6] += 1
        else:
            roomNumber[9] += 1
    else:
        roomNumber[int(i)] += 1

print(max(roomNumber))
