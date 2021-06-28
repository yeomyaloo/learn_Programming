#이진 검색 알고리즘

from typing import Any, Sequence

def bin_search(a:Sequence, key: Any) -> int:
    pl = 0 #검색 범위 맨 앞의 원소 인덱스
    pr = len(a) -1 #검색 범위 맨 뒤의 원소 인덱스

    while True:
        
        pc = (pl+pr) //2 #중앙의 원소 인덱스를 구하는 것 그리고 나누기를 하면 소숫점 나와서 안 된다고 함
        if a[pc] == key:
            return pc #검색 성공

        #키값이 중앙값보다 큰 경우 중앙값을 다시 세팅
        elif a[pc] < key:
            pl = pc + 1
            #현재의 중앙값 바로 뒤를 검색 범위 맨 앞의 원소 인덱스로 설정해준다.

        else: #키값이 중앙값보다 작은 경우 중앙값 다시 세팅
            pr = pc -1
             #키값이 중앙값보다 작은 경우 pl 검색 범위 맨 앞의 원소 인덱스는 그대로니 pr 검색 범위 맨 뒤의 원소 인덱스를 현재 중앙값의 바로 앞으로 설정

        if pl > pr:
            break
    return -1 #검색 실패

if __name__ == '__main__': #스크립트 파일로 실행 프로그램의 시작점이 맞는지 판단하는 작업. 또한 스크립트 파일이 메인 프로그램으로 사용될 때와 모듈로 사용될 때를 구분하기 위한 용도
    num = int(input('원소 수를 입력하세요.: '))
    x = [None] * num

    print("배열의 데이터를 오름차순으로 입력하세요.")

    x[0] = int(input('x[0]:'))
    for i in range(1,num): #x[0]을 입력받아 놓은 상태이기 때문에 x[1]부터 num개 입력받기 시작
        while True:
            x[i] = int(input(f"x[{i}]: "))
            if x[i]>= x[i-1]:#입력 값이 직전 입력값보다 클 경우 프로그램 종류
                break

    ky = int(input('검색할 값을 입력하세요.: '))

    idx = bin_search(x,ky)

    if idx == -1:
        print("검색값을 갖는 원소가 존재하지 않습니다.")

    else:
        print(f"검색 값은 x[{idx}]에 있습니다.")
            
            
            
        

            
        
    
