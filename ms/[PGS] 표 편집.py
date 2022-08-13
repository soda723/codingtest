# 런타임 에러가 나는 이유를 모르겠음
# 단순 리스트로는 못푸는 문제라는 말을 봐서 절망
def solution(n, k, cmd):
    state = [True for _ in range(n)]   # 표 상태(True가 O)
    recmd = []  # Z 처리해준 명령어 모음
    delete = []   # cmd에서 C 나오는 인덱스 위치
    answer = ''
    
    # Z 나오면 먼저 나온 C 제거
    for i in range(len(cmd)):
        if cmd[i] == "Z":
            recmd.pop(delete[-1])
            delete.pop()
        elif cmd[i] == "C":
            recmd.append(cmd[i])
            delete.append(i)
        else:
            recmd.append(cmd[i])
    
    # 명령어 처리
    idx = 0   # recmd의 인덱스
    while True:
        if idx == len(recmd):
            break

        if recmd[idx][0] == "D":
            k += int(recmd[idx][2])
            idx += 1

        elif recmd[idx][0] == "C":
            state[k] = False
            idx += 1

        elif recmd[idx][0] == "U":
            k -= int(recmd[idx][2])
            idx += 1

    for s in state:
        if s:
            answer += "O"
        else:
            answer += "X"
    
    
    print(answer)
    #return answer


solution(8, 2, ["D 2","C","U 3","C","D 4","C","U 2","Z","Z"])

    
    
