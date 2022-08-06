# 출력 형식에 맞게 문자열로 리턴해주는 함수
def output(h, m):
    if h < 10:
        if m < 10:
            return "0" + str(h) + ":0" + str(m)
        else:
            return "0" + str(h) + ":" + str(m)
    else:
        if m < 10:
            return str(h) + ":0" + str(m)
        else:
            return str(h) + ":" + str(m)
    

def solution(n, t, m, timetable):
    arrive = [540]   # 셔틀 도착시간 리스트(셔틀은 9:00분부터 도착)
    time = []   # timetable 분 단위 변환 리스트

    # 셔틀 도착시간 계산
    for i in range(1, n):
        arrive.append(arrive[i-1] + t)

    # timetable 분 단위 변환
    for i in range(len(timetable)):
        temp = list(map(int, timetable[i].split(':')))
        time.append(temp[0] * 60 + temp[1])
    time.sort()
    

    # 마지막 셔틀 직전까지 셔틀에 탈 수 있는 크루들 time에서 제거
    for i in range(len(arrive) - 1):
        for _ in range(m):
            if time[0] <= arrive[i]:
                time.pop(0)
            else:
                break

    # 마지막 셔틀 도착시간보다 늦게 도착한 크루들 time에서 제거
    while len(time) != 0:
        if arrive[-1] < time[-1]:
            time.pop()
        else:
            break

    # 대기열에 남아있는 크루들 수(len(time))이 m보다 작을 때
    # 콘의 도착시간은 마지막 셔틀의 도착시간과 같음
    if len(time) < m:
        h = arrive[-1] // 60
        m = arrive[-1] % 60
        return output(h, m)
    # 그렇지 않다면 콘의 도착시간은 m번째 서있는 크루보다 1분 빠른 시간
    else:
        h = (time[m-1] - 1) // 60
        m = (time[m-1] - 1) % 60
        return output(h, m)
