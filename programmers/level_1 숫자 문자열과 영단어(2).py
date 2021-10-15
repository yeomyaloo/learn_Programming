a = {"zero":"0", "one":"1", "two":"2", "three":"3", "four":"4", "five":"5", "six":"6", "seven":"7", "eight":"8", "nine":"9"}
def solution(s):
    answer = s
    for key,values in a.items():
        answer=answer.replace(key,values)
    
    return int(answer)
