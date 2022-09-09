# BOJ 잃어버린괄호 1541번 silver2
# 소요시간 : 18m
answer = 0
exp = list(input().split('-'))
if len(exp) == 1:
    # 모두 더하기 식
    tmp = exp[0].split('+')
    for v in tmp:
        answer += int(v)
else :
    for i in range(len(exp)):
        tmp = exp[i].split('+')
        if i == 0:
            for v in tmp:
                answer += int(v)
        else : 
            for v in tmp:
                answer -= int(v)
print(answer)