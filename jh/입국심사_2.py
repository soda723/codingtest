# 분이 먼저 주어지고, 주어진 시간 동안 각 심사관이 처리 가능한 사람 수를 구하는 것으로 생각
# 따라서 이분 탐색의 범위는 시간 범위, mid분 동안 처리 가능한 사람 수가 n보다 큰지, 작은지로 범위 이동하는 방식 사용
# times 배열이 정렬되어 있어야 mid분 동안 처리 가능한 최대 사람 수를 구할 수 있음 -> 주어진 입력에서는 정렬되어 있다고 가정

def solution(n, times):
    answer = 0
    start = min(times) # 가장 적게 걸릴 때
    end = max(times) * n # 가장 많이 걸릴 때
    
    while start <= end:
        mid = (start + end) // 2
        p = 0
        for t in times:
            p += mid // t # 정렬되어 있기 때문에 앞에서부터 순서대로 계산하면 최대 값이 됨
        if p >= n: # n명을 처리하는 데에 시간이 충분하다면
            answer = mid
            end = mid - 1 # 왼쪽 범위를 선택
        else:
            start = mid + 1 # 오른쪽 범위를 선택
    
    return answer