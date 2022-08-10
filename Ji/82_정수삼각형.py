# 소요시간 47m

def solution(tri):
    tri = tri[::-1] # 목적지를 하나로 만들어야 생각하기 편해서 뒤집음
    # 비용값(거리값)을 계산할 리스트 초기화
    c = [ [0 for _ in range(len(tri[0]))] for _ in range(len(tri)) ] 
    # 시작 초기값을 넣어준다.
    for idx in range( len(tri[0]) ):
        c[0][idx] = tri[0][idx]
    
    for i in range(1, len(tri)): 
        for j in range(0, len(tri[i])): 
            # 현재 위치까지 오는 비용은 위에서 가능한 위치 중 큰 값
            c[i][j] = tri[i][j] + max(c[i-1][j], c[i-1][j+1])

    return c[len(tri) -1][0]

# answer = solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]])
# if answer == 30 : print("정답")
# else : print("오답 : ", answer)