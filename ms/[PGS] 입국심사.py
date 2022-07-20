# 이분탐색 안쓰고 times 배수 계산해서 풀려고 하다가 1시간 날림
# 이분탐색은 모르는 개념이라 이 문제는 내 힘으로 풀었다고는 못하겠음ㅠ
# 이분탐색 다양한 예제 풀어보기!!!
def solution(n, times):
    # left 최소 시간, right 최대 시간
    # 예제 = 최소 시간은 1명 7분, 최대 시간은 6명 10분씩
    left, right = times[0], times[-1] * n

    # while True로 풀면 시간 초과
    while left < right:        
        mid = (left + right) // 2
        temp = 0

        # mid 시간 동안 검사할 수 있는 사람 수(temp) 계산
        for i in times:
            temp += mid // i
            if temp >= n:
                break

        # temp가 n보다 크거나 같으면 탐색 범위 left ~ mid
        # 그렇지 않으면 탐색 범위 mid+1 ~ right
        if temp >= n:
            right = mid
        else:
            left = mid + 1

    return left
    
