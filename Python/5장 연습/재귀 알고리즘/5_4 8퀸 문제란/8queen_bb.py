# 각 열에 퀸을 1개씩 배치하는 조합을 재귀적으로 나열하기

pos = [0] * 8      # 각 열에 퀸의 위치
flaf = [False] * 8 #각 행에 퀸을 배치했는지 체크


def put():
    #각 열에 배치한 퀸의 위치 출력
    for i in range(8):
        print(f'{pos[i]:2}', end=" ")
        
def set(i):
    #i열에 퀸을 배치
    for j in range(8):
        if no flag[j]:
            pos[i] = j
            if i == 7:
                put()
        else:
            flag[j] =True
            set(i+1) #다음 열에 퀸 배치
            flag[j] = False
            
set(0) #0열에 퀸을 배치
