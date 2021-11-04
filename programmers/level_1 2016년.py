def solution(a, b):
    Wdays = ["THU","FRI","SAT","SUN","MON","TUE","WED"]
    mon = [31, 29, 31, 30, 31, 30 , 31, 31, 30, 31, 30, 31]
    day = 0
    for i in range(a-1):
        day += mon[i]
   
    weekday = (day+b)%7
    return Wdays[weekday]
