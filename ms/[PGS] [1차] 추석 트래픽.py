def solution(lines):
    # lines 원소가 1개이면 무조건 답은 1
    if len(lines) == 1:
        return 1

    # 밀리초로 변환 + 시작 시간 계산
    times = []
    for line in lines:
        s = line.split()
        time = s[1]   # 완료 시간
        t = float(s[2][:-1]) - 0.001   # 걸린 시간
        fList = [float(item) for item in time.split(':')]   # 완료 시간 시/분/초 분리
        finish = fList[0] * 3600 + fList[1] * 60 + fList[2]
        start = round(finish - t, 3)

        times.append([start, finish])

    # 초당 처리량 계산    
    temp = []
    for i in range(len(times)):
        end = round(times[i][1] + 0.999, 3)

        t = 0
        for j in range(i+1, len(times)):
            if times[j][0] <= end:
                t += 1
        
            temp.append(t+1)
    
    
    if len(temp) == 0:
        return 0
    else:
        return max(temp)
