# 점수 57.0

import numpy as np

def rotate(array):
    list_of_tuples = zip(*array[::-1])
    li = [list(elem) for elem in list_of_tuples]
    return np.array(li)

def solution(key, lock):
    if np.array_equal(lock, np.ones([len(lock), len(lock)])):
        return True
    
    check = np.array(lock)

    delete = np.array([1] * len(lock)) # 자물쇠의 가장자리의 필요없는 돌기 부분 제거하는 코드
    while True:
        if np.array_equal(check[0], delete):
            check = np.delete(check, 0, axis = 0)
            continue
        if np.array_equal(check[-1], delete):
            check = np.delete(check, -1, axis = 0)
            continue
        break
    
    delete = np.array([1] * len(check))
    while True:
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
        rotated = rotate(key)
        for r in range(len(key) - r_size + 1):
            for c in range(len(key[0]) - c_size + 1):
                k = rotated[r:r+r_size, c:c+c_size]
                if np.array_equal(k, check):
                    return True
    
    return False