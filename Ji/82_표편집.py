#소요시간:1h1m45s
#정확도테스트o 효율성6~10시간초과 -> 연결리스트를 사용해야함

def solution(n, k, cmd):

    answer = ['O']*n
    idx = k
    tmp = []
    for c in cmd:
        if c == "C":
            #현재행 삭제
            tmp.append(idx)
            answer[idx] = 'X'
            
            found = 0
            for i in range(idx, n):
                if answer[i]=='O':
                    found = 1
                    break
            if found==0 : #위쪽 선택
                cnt = 1
                while cnt :
                    idx -=1
                    if answer[idx] == 'X':
                        continue
                    else :
                        cnt -=1
            else: #아래쪽 선택
                cnt = 1
                while cnt :
                    idx +=1
                    if answer[idx] == 'X':
                        continue
                    else :
                        cnt -=1

        elif c == "Z":
            answer[tmp.pop()] = 'O'
         
        elif c.split()[0] == "U":
            cnt = int(c.split()[1])
            while cnt :
                idx -=1
                if answer[idx] == 'X':
                    continue
                else :
                    cnt -=1
                    
        else: #c.split()[0] == "D"
            cnt = int(c.split()[1])
            while cnt :
                idx +=1
                if answer[idx] == 'X':
                    continue
                else :
                    cnt -=1
    return ''.join(answer)

ans = solution(8,2,["D 2","C","U 3","C","D 4","C","U 2","Z","Z"])
if ans == "OOOOXOOO":
    print("TC1 정답")
else : 
    print("TC1 실패, ", ans)

ans = solution(8,2,["D 2","C","U 3","C","D 4","C","U 2","Z","Z","U 1","C"])
if ans == "OOXOXOOO":
    print("TC2 정답")
else : 
    print("TC2 실패, ", ans)