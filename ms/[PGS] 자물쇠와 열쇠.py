# 2차원 배열 회전 코드 참고함
# 리스트 깊은복사가 안됨 걍 총체적 난국.. 나만 어려운거 아니지..
def solution(key, lock):
    kbump = 0
    lhole = 0
    lockl = []
    UD = []
    LR = []
    
    for i in key:
        kbump += i.count(1)
    for i in lock:
        lhole += i.count(0)

    if lhole > kbump:
        return False

    # 자물쇠의 홈 부분 좌표 구하기
    for i in range(len(lock)):
        for j in range(len(lock)):
            if lock[i][j] == 0:
                lockl.append([i, j])
                UD.append([0, 1])
                LR.append([1, 0])
                

    for i in range(4):
        keyl = []
        keylU = []
        key = [[row[i] for row in key[::-1]] for i in range(len(key[0]))]

        # 키의 돌기 부분 좌표 구하기
        for i in range(len(key)):
            for j in range(len(key)):
                if key[i][j] == 1:
                    keyl.append([i, j])
                    keylU.append([i, j])


        # 키 상하좌우로 이동
        for i in range(len(lock)-1):
            for j in range(len(keyl)):
                keylU[j][1] = keyl[j][1] - (i + 1)
            

            



solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]], [[1, 1, 1], [1, 1, 0], [1, 0, 1]])
