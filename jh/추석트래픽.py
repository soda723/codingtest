import decimal

def solution(lines):
    time = []
    for i in lines:
        data = i.split()
        e = 3600 * int(data[1][:2]) + 60 * int(data[1][3:5]) + float(data[1][6:])
        t = float(data[2][:-1])
        s = float(decimal.Decimal(str(e)) - decimal.Decimal(str(t)) + decimal.Decimal('0.001'))
        time.append([s, e])
    time.sort(key=lambda x: x[1])
    answer = 0
    for i in range(len(time)):
        count = 0
        for j in range(i, len(time)):
            if time[i][1] + 1 > time[j][0]:
                count += 1
        if count > answer:
            answer = count
    return answer