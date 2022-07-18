# 미완성
from datetime import datetime, timedelta

def solution(lines):
    #lines : 로그 문자열 리스트
    #max_throughput : 초당 최대 처리량 : 임의 시간부터 1s 간 처리하는 요청의 최대수 (완료여부x)
    max_throughput = 0
    
    # 동일 날짜 제거
    n_lines = [line.strip('2016-09-15').split()[0] for line in lines ]
    n_lines = [datetime.strptime(date_string,'%H:%M:%S.%f') for date_string in n_lines]
    duration = [line.strip('2016-09-15').split()[1].strip('s') for line in lines ]
    # test_date = datetime(1900,1,1,20,59,56,3)
    # test_date2 = datetime(1900,1,1,20,59,58,3)
    # print((test_date2 - test_date).seconds)
    for log in n_lines:
        start = log - timedelta(seconds=1)
        end = log
        print("^",start)
        print("^",end)
        cnt = 0
        for log2 in n_lines:
            oper1 = (log2 - start).seconds
            oper2 = (log2 - end).seconds

            # 음수 계산
            print("#", start + timedelta(seconds = oper1))
            print("#", log2)
            if start + timedelta(seconds = oper1) == log2 : 
                print("pass1", oper1)
                pass
            else :
                oper1 *= -1

            print("😒", end + timedelta(seconds = oper2))
            print("😒", log2)
            if end + timedelta(seconds = oper2) == log2 : 
                print("pass", oper2)
                pass
            else:
                oper2 *= -1

            #연산
            if oper1 * oper2 < 0:
                cnt +=1
            
            
        if max_throughput < cnt : 
            max_throughput = cnt

    
    return max_throughput

lines = ["2016-09-15 20:59:57.421 0.351s", "2016-09-15 20:59:58.233 1.181s", "2016-09-15 20:59:58.299 0.8s", "2016-09-15 20:59:58.688 1.041s", "2016-09-15 20:59:59.591 1.412s", "2016-09-15 21:00:00.464 1.466s", "2016-09-15 21:00:00.741 1.581s", "2016-09-15 21:00:00.748 2.31s", "2016-09-15 21:00:00.966 0.381s", "2016-09-15 21:00:02.066 2.62s"]
answer = 7

my = solution(lines)
print("내 답 : ", my, "기댓값 : ", answer)
if my == answer : 
    print("---성공---")
else :
    print("---실패---")