cache = [[[-1 for c in range(102)] for r in range(102)] for d in range(102)]   # 3차원 리스트

def w(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return 1

    A = a + 50
    B = b + 50
    C = c + 50

    ret = cache[A][B][C]
    if ret != -1:
        return ret

    if a > 20 or b > 20 or c > 20:
        cache[A][B][C] = w(20, 20, 20)
        return cache[A][B][C]

    if a < b and b < c:
        cache[A][B][C] = w(a, b, c - 1) + w(a, b - 1, c - 1) - w(a, b - 1, c)
        return cache[A][B][C]

    else:
        cache[A][B][C] = w(a - 1, b, c) + w(a - 1, b - 1, c) + w(a - 1, b, c - 1) - w(a - 1, b - 1, c - 1)
        return cache[A][B][C]

while True:
    a, b, c = map(int, input().split())

    if a == -1 and b == -1 and c == -1:
        break

    result = w(a, b, c)
    print("w(" + str(a) + ", " + str(b) + ", " + str(c) + ") = " + str(result))