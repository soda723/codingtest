def time_format(time): # 분 단위로 주어진 시간을 "HH:MM" 형식의 문자열로 반환하는 함수
    hour = time // 60
    minute = time % 60
    hour = '0' + str(hour) if hour // 10 == 0 else str(hour)
    minute = '0' + str(minute) if minute // 10 == 0 else str(minute)
    return hour + ':' + minute

def solution(n, t, m, timetable):
    timetable.sort()
    for i in range(len(timetable)): # "HH:MM"의 데이터를 분 단위의 int 값으로 변환
        time = list(map(int, timetable[i].split(':')))
        timetable[i] = time[0] * 60 + time[1]
            
    for i in range(n - 1): # 마지막 버스만 남겨두고 탑승할 수 있는 인원 제외
        nowbus = 9 * 60 + i * t
        for _ in range(m):
            if len(timetable) == 0:
                break
            if timetable[0] <= nowbus:
                del timetable[0]
    
    latestbus = 9 * 60 + (n - 1) * t # 마지막 버스의 도착 시간
    for _ in range(m - 1): # 마지막 버스에서 한 자리만 남겨두고 탑승할 수 있는 인원 제외
        if len(timetable) == 0:
            break
        if timetable[0] <= latestbus:
            del timetable[0]
    
    if len(timetable) != 0 and timetable[0] <= latestbus: # 대기 중인 크루가 있는데 그 크루가 마지막 버스 도착 시간보다 일찍 대기하는 경우
        answer = time_format(timetable[0] - 1) # 대기 중인 크루보다 1분 일찍 대기해야 함
    else:
        answer = time_format(latestbus) # 위의 경우가 아니면 마지막 버스 도착 시간에 맞춰 대기하면 됨

    return answer