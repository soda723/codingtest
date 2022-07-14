def solution(N, number):
    answer = 0
    result = []

    # N = number 경우 추가 해주기! (테스트케이스 9) 
    if N == number:
        return 1
    result.append(set([N]))

    for i in range(2, 9):
        temp = set()
        temp.add(int(str(N) * i))
        
        first = i - 1
        second = 1
        # 뺄셈, 나눗셈 교환법칙 성립하지 않음 (테스트케이스 8)
        while True:
            for j in result[first-1]:
                for k in result[second-1]:
                    temp.add(j + k)
                    temp.add(k - j)
                    temp.add(j - k)
                    temp.add(j * k)
                    temp.add(k // j)
                    temp.add(j // k)
            
            if number in temp:
                answer = i
                break
                
            if (first == second) or (second + 1 == first):
                break

            first -= 1
            second += 1
        
        if answer != 0:
            break
        else:
            temp.discard(0)   # 0으로 나누면 컴파일 에
            result.append(temp)
    
    if answer != 0:
        return answer
    else:
        return -1
    
