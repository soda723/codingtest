def solution(n, k, cmd):
    state = [True for _ in range(n)]
    recmd = []
    delete = []
    answer = ''
    
    for i in range(len(cmd)):
        if cmd[i] == "Z":
            recmd.pop(delete[-1])
            delete.pop()
        elif cmd[i] == "C":
            recmd.append(cmd[i])
            delete.append(i)
        else:
            recmd.append(cmd[i])

    idx = 0
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

    
    
