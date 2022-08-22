def lcm(a, b):
    for i in range(max(a, b), a*b+1):
        if i % a == 0 and i % b == 0:
            return i

def solution(arr): 
    while len(arr) != 1:
        x = arr.pop()
        y = arr.pop()
        arr.append(lcm(x, y))
    return arr[0]