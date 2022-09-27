# 백준 크리스마스 선물 14235번 silver3
# 소요시간 : 17m15s

n = int(input())
# 0 : 아이만남 > 출력 / 선물 충전 2 3 2 : 2개 충전, 가치 : 3,2 
bag = []
minibag = []
for _ in range(n): 
    now = list(map(int, input().split()))
    if len(now) == 1 : # 아이 만남
        if len(bag) == 0 : print(-1)
        else : 
            m = max(bag)
            print(m)
            bag.remove(m)
    else: # 선물 리필
        minibag = now[1:]
        bag.extend(minibag)
