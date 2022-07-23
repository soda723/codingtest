#성공 x 이진탐색x
#1h 31m
def solution(n, times):
    answer = 0
    times.sort()
    if n == 1:
        return times[0]
    
    lists = [0]*len(times) # 대기시간
    lists[0] = times[0] # 첫번째 사람은 입장 해놓고
    i=2 # 두번째 사람부터 시작
    while(i!=n+1):
        #빈 곳 있을때
        if 0 in lists:
            empty_idx = lists.index(0) # 비어 있는 곳의 인덱스, 여러개 일 경우 가장 앞(=가장빠른 소요시간인곳)
            if empty_idx == 0: # 빈곳이 가장 빠른 곳이면 그냥 들어가도 됌
                lists[empty_idx] = times[empty_idx]
            else:#가장 빠른 곳이 아니면 더 빠른 곳에 들어가는 시간을 비교
                compare = lists[empty_idx-1]+times[empty_idx-1] #비교할 시간=더빠른곳의 대기시간+소요시간
                if times[empty_idx] > compare : # 앞이 더 빠르면
                    answer += lists[empty_idx-1] # 대기시간을 더해주고
                    # 대기시간 줄여주기
                    listss=[]
                    for rt in lists:
                        if rt-lists[empty_idx-1] > 0 : t= rt_lists[empty_idx-1]
                        else : t = 0
                        listss.append(t)
                    lists = listss
                    i-=1 # # 순서를 하나 줄여줌(다시 순서)
                else:#지금 빈곳에 바로 들어가는게 더 빠르면 들어가기
                   lists[empty_idx] = times[empty_idx]     
        #빈곳없을때 시간보내주기
        else:
            for _ in range(min(lists)): # 대기시간이 0인 곳이 나올때 까지 시간보내기
                lists = [minutes -1 for minutes in lists]
                answer +=1
            i -= 1 # 순서를 하나 줄여줌(다시 순서)

        i +=1 # 다음 순서
        
    answer += max(lists) # 마지막 순서 입장후 종료시간 더하기
    return answer