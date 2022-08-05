##아이디어 정리만 하다가 시간이 없어서 다 풀지는 못했어요ㅠㅠ 
## ~1h, 30m
def rotate90(key):
    return key
def rotate180(key):
    n_key=[]
    return key
def rotate270(key):
    return key:
def mvright(key):
    return key
def mvdown(key):
    return key

def solution(key, lock):
    answer = false # 확인 용
    
    #--**아이디어정리**--
    # 자물쇠를 열쇠 빈공간을 포함하도록 크게 만든다.
    new_length = len(lock) + (len(key)-1)
    # 한칸식 이동하면서 맞는 지 확인한다.(0,0)~(n,n)까지 촵촵촵
    # 회전 방향 4가지를 모두 확인한다.(정방향, 90회전, 180회전, 270회전)
    # 확인하면서 중간에 일차하는 값이 나오면 return true
    
    #없으면 false가 반환
    return answer