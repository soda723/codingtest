# 연결리스트 몰라서 다른 사람 풀이 참고함ㅠㅠ
def solution(n, k, cmd):
    linked_list = {i: [i - 1, i + 1] for i in range(n)}
    state = ['O'] * n
    delete = []
    answer = ''

    for c in cmd:
        c = c.split()

        if c[0] == 'D':
            for _ in range(int(c[1])):
                k = linked_list[k][1]

        elif c[0] == 'U':
            for _ in range(int(c[1])):
                k = linked_list[k][0]

        elif c[0] == 'C':
            prev, nxt = linked_list[k]
            state[k] = 'X'
            delete.append((prev, k, nxt))
            
            if nxt == n:   # 마지막 행 삭제했을 경우
                k = linked_list[k][0]
            else:
                k = linked_list[k][1]

            # 연결 리스트에서 삭제 작업 처리하기
            if prev == -1:   # 첫 행 삭제했을 경우
                linked_list[nxt][0] = prev
            elif nxt == n:   # 마지막 행 삭제했을 경우
                linked_list[prev][1] = nxt
            else:
                linked_list[prev][1] = nxt
                linked_list[nxt][0] = prev
        else:
            prev, now, nxt = delete.pop()
            state[now] = 'O'

            # 연결 리스트에서 실행 취소 작업 처리하기
            if prev == -1:
                linked_list[nxt][0] = now
            elif nxt == n:
                linked_list[prev][1] = now
            else:
                linked_list[prev][1] = now
                linked_list[nxt][0] = now
    

    for i in state:
        answer += i
    
    return answer


solution(8, 2, ["D 2","C","U 3","C","D 4","C","U 2","Z","Z"])

    
    
