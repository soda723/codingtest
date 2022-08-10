# 정확성 64.3 / 효율성 35.7
# 메모이제이션이랑 재귀 써서 풀면 시간초과 나는 문제 -> 아마 C++은 되는듯
# 예전에 다른 사이트에서 동적계획법 공부하면서 풀어본 문제였음..

def solution(triangle):
    n = len(triangle)

    # 사진으로 설명 대체함 -> 사진 깃허브에 올려둠
    for i in range(1, n):
        for j in range(i+1):
            if j == 0:
                triangle[i][j] += triangle[i-1][j]
            elif j == i:
                triangle[i][j] += triangle[i-1][j-1]
            else:
                triangle[i][j] += max(triangle[i-1][j], triangle[i-1][j-1])

    return max(triangle[-1])
