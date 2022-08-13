# 소요시간:(계속)1h 51m 50s
# 틀린 + 런타임 에러 ㅠㅠ 이유를 못 찾겠음

def solution(n, k, cmd):

    answer = ['O']*n
    linked = {0:[-1,1], n-1:[n-2,-1]}
    for i in range(1,n-1):
        linked[i] = [i-1,i+1]
    idx = k
    tmp = []
    for c in cmd:
        print(linked)
        if c == "C":
            #현재행 삭제
            tmp.append(idx)
            answer[idx] = 'X'
            # 앞뒤 인덱스 바꿔주기
            if linked[idx][1] == -1 : # 마지막 행
                linked[idx-1][1] = -1
            elif linked[idx][0] == -1: # 첫 행
                linked[idx+1][0] = -1
            else:
                linked[idx-1][1] = linked[idx][1]
                linked[idx+1][0] = linked[idx][0]
            
            ii = linked[idx][1]
            if ii == -1: idx = linked[idx][0]
            else : idx = linked[idx][1]

        elif c == "Z":
            j = tmp.pop()
            answer[j] = 'O'
            if linked[j][1] == -1 :linked[j-1][1]=j
            elif linked[j][0] == -1: linked[j+1][0]=j
            else:
                linked[j-1][1]=j
                linked[j+1][0]=j

         
        elif c.split()[0] == "U":
            for _ in range(int(c.split()[1])):
                idx = linked[idx][0]
                    
        else: #c.split()[0] == "D"
            for _ in range(int(c.split()[1])):
                idx = linked[idx][1]

    return ''.join(answer)

ans = solution(8,2,["U 2","C","D 6","C","C","U 1","Z","Z","Z"])
if ans == "OOOOOOOO":
    print("TC1 정답")
else : 
    print("TC1 실패, ", ans)
