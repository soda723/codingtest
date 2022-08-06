# 소요시간 : 23m
# [1,2] 7 => -1
'''
## 베스트 댓글 참고해서 나중에 다시 풀어보기
코드들을 보니 다들 import heapq를 하셨는데 저는 heap을 몰라서..ㅎㅎ
 queue만 써서 풀었는데도 시간이 heap을 쓴 풀이의 절반 정도 걸리네요.
  저는 섞어서 나온 새로운 값, mix들을 별도의 queue에 넣었는데 이게 가장 큰 요인같네요.
   나중에 나온 mix값이 먼저 나온 것보다 클 수밖에 없어서 섞는 순서대로 queue에 넣어주면 크기 순서를 신경 쓸 필요가 없어요.
    그냥 popleft로 꺼내면 무조건 mix값의 최소입니다ㅎ
'''
import heapq
def solution(scoville, K):
    cnt = 0
    heapq.heapify(scoville)
    
    while 1 :
        m1 = heapq.heappop(scoville)
        if m1 >= K: break
        elif m1 == 0 : return -1
        try:
            m2 = heapq.heappop(scoville)
        except IndexError:
            return -1
        
        new = m1 + m2*2
        heapq.heappush(scoville, new)
        cnt += 1
    
    return cnt


'''
#시간초과 heap x

def solution(scoville, K):
    scoville.sort()
    if scoville[0] == 0: return -1
    cnt = 0
    stop = 1
    scoville.sort()
    while stop :
        if scoville[0] >= K:
            break
        else:
            new = scoville[0]+ scoville[1]*2
            cnt += 1
            scoville.pop(0)
            scoville.pop(0)
            scoville.append(new)
            scoville.sort()
            
    return cnt
'''