#배열 원소의 최댓값을 구해서 출력하기(원솟값을 입력받음)

from max inport max_of

print("배열의 최댓값을 구합니다.")
print("주의: "End"를 입력하면 종료합니다.")

number = 0
x = [] #빈리스트

while true:
    s = input(f"x[{number}]값을 입력하세요.:")
    if s =='End':
        break
    x.append(int(s)) #입력받는 값을 배열의 맨 뒤에 추가시키는 함수 append
    number+=1

print(f"[{number}]개를 입력했습니다.")
print(f"최댓값은 {max_of(x)입니다.}")
