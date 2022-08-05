import numpy as np

def rotate(array): # 배열을 90도 회전시키는 함수
    list_of_tuples = zip(*array[::-1])
    li = [list(elem) for elem in list_of_tuples]
    return np.array(li)

def solution(key, lock):
    if np.array_equal(lock, np.ones([len(lock), len(lock)])): # 자물쇠가 이미 열려 있는 경우 처리
        return True
    
    check = np.array(lock)

    # 자물쇠 가장자리의 필요없는 돌기 부분 제거하는 코드
    delete = np.array([1] * len(lock))
    while True: # 필요없는 행 제거
        if np.array_equal(check[0], delete):
            check = np.delete(check, 0, axis = 0)
            continue
        if np.array_equal(check[-1], delete):
            check = np.delete(check, -1, axis = 0)
            continue
        break
    
    delete = np.array([1] * len(check))
    while True: # 필요없는 열 제거
        if np.array_equal(check[:, 0], delete):
            check = np.delete(check, 0, axis=1)
            continue
        if np.array_equal(check[:, -1], delete):
            check = np.delete(check, -1, axis=1)
            continue
        break
        
    check = np.where(check % 2 == 0, 1, 0) # eqaul 비교를 위해 자물쇠 배열 반전
    r_size = len(check)
    c_size = len(check[0])
    
    for _ in range(4):
        key = rotate(key) # 기존 코드에는 key 배열을 회전한 것으로 key를 갱신하지 않아 그냥 제자리에서 90도 회전만 4번 한 거였음 -> 90, 180, 270도 회전을 위해 회전한 key 배열로 값을 갱신
        for r in range(len(key) - r_size + 1):
            for c in range(len(key[0]) - c_size + 1):
                k = key[r:r+r_size, c:c+c_size] # key 배열에서 자물쇠의 홈 부분 만큼 잘라내서 비교
                if np.array_equal(k, check):
                    return True
    
    return False