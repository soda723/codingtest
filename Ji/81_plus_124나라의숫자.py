#Lv2 추가문제
# 소요시간 : 23m
# 진법 계산기 어떻게 했는지 참고하고 풀었음
def solution(n):
    tmp = ''
    while n : 
        if n%3 == 0 :
            tmp = '4' + tmp
            n = n // 3 -1
        else:
            tmp = str(n%3) + tmp
            n = n // 3

    return tmp.replace('3','4') 