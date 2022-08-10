# 소요시간 : 2h 10m ~~ing
# 시간문제는 최소 단위로 변환하기
# TC 18 런타임 에러
def to_answerformat(time):
    hour = time // 60
    minute = time - hour*60
    if hour <10 : hour =  "0" + str(hour)
    else : hour = str(hour)
    if minute <10 : minute =  "0" + str(minute)
    else : minute = str(minute)
    return hour + ":" + minute
    
def solution(n, t, m, timetable):
    # 시간을 분(= 최소시간단위)으로 바꾼다.
    newtable = []
    for value in timetable:
        hour, minute = value.split(':')
        newtable.append( int(hour) * 60 + int(minute) )

    #answer를 막차시간으로 초기화
    answer = 540 + t *(n-1)
    
    # 오는 사람이 최대 인원보다 작으면 막차탑승
    if len(timetable)  < m :
        return to_answerformat(answer)

    # 사람을 순서대로 정렬하기
    newtable.sort()

    # 막차보다 늦게 오는사람은 신경쓸사람 아님 -> 삭제
    while newtable : 
        if newtable[-1] > answer : newtable.pop()
        else: break


    # 막차에 남는 사람만 남기자.
    bus = 540
    while bus < answer :
        for _ in range(m):
            if bus >= newtable[0]:
                newtable.pop(0)
            else:break 
        bus += t # 다음 차시간


    # 남은 사람이 정원보다 많으면 정원의 마지막 사람보다 1분 일찍온다.
    if len(newtable) >= m : answer = newtable[m-1] - 1
       
    return to_answerformat(answer)

# ans = solution(1, 1, 1, ["23:59"])
# if ans == "09:00":
#     print("정답")
# else : print("틀림 : ",ans)