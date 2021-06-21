if __name__ == '__main__':
    print("10진수를 n진수로 변환합니다.")

    while True: #마지막 행의 계속성을 위해서 while True문을 사용
        while True:
            no = int(input("변환할 값으로 음이 아닌 정수를 입력하세요.: "))
            if no > 0:
                break #변환할 값을 음수로 입력할 때 계속해서 무한루프를 돌고 이때 정수를 입력받으면 break문으로 파괴
        while True:
            cd = int(input("어떤 진수로 변환할까요?: "))
            if 2 <= cd <= 36:
                break

        print(f"{cd}진수로는 {2-7_완성(no, cd)}입니다.")

        retry = input("한 번 더 변환할까요?(Y .... 예 / N .... 아니요): ")
        if retry in {'N','n'}: #n N을 입력하면 프로그램 종료.
            break
        
