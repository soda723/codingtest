# 소요시간 50m 37s
def solution(n, cpts):
    '''
    0번 컴퓨터 부터 시작해서 방문한 곳 체크 = >  갈수 있는곳
    안 간곳에서 또 순회하기
    안 간곳이 없어질때까지
    시작점 개수 = answer
    '''
    answer = 0
    visit = [0]*n
    # 0번 컴퓨터부터 시작
    visit[0] = 1 
    nextcpt = 0
    while 1 : 
        q = [nextcpt]
        while q :
            now = q.pop()
            for c in range(n):
                if visit[c] == 0 and cpts[now][c] == 1:
                    visit[c] = 1
                    q.append(c) #다음 탐색할 인덱스 추가

        answer += 1
        try :
            #방문하지 않은 곳이 있으면 그곳을 시작점으로 다시 시작
            nextcpt = visit.index(0)
            visit[nextcpt] = 1
        except ValueError : break #없으면 종료
        
    return answer
