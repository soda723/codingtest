def time_format(time):
    hour = time // 60
    minute = time % 60
    hour = '0' + str(hour) if hour // 10 == 0 else str(hour)
    minute = '0' + str(minute) if minute // 10 == 0 else str(minute)
    return hour + ':' + minute

def solution(n, t, m, timetable):
    timetable.sort()
    for i in range(len(timetable)):
        time = list(map(int, timetable[i].split(':')))
        timetable[i] = time[0] * 60 + time[1]
            
    for i in range(n - 1):
        nowbus = 9 * 60 + i * t
        for _ in range(m):
            if len(timetable) == 0:
                break
            if timetable[0] <= nowbus:
                del timetable[0]
    
    latestbus = 9 * 60 + (n - 1) * t
    for _ in range(m - 1):
        if len(timetable) == 0:
            break
        if timetable[0] <= latestbus:
            del timetable[0]
    
    if len(timetable) != 0 and timetable[0] <= latestbus:
        answer = time_format(timetable[0] - 1)
    else:
        answer = time_format(latestbus)

    return answer