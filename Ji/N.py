#TC 1,5,6,7,8 실패

def operation_N(N,before_set):
    after_set = set()
    for Nn in before_set:
        after_set.add(N + Nn)
        after_set.add(N-Nn)
        after_set.add(N*Nn)
        after_set.add(Nn-N)
        try:
            after_set.add(N/Nn)
            after_set.add(Nn/N)
        except ZeroDivisionError:
            pass

    return after_set


def solution(N, number):
    if N == number :
        return 1

    second = set([N*10 + N, N+N , N-N, N*N,  N/N,])
    if number in second : 
        return 2

    third = operation_N(N,second)
    third.add(N*100+N*10+N)
    if number in third:
        return 3

    forth = operation_N(N,third)
    forth.add(N*1000+N*100+N*10+N)
    if number in forth:
        return 4

    fifth = operation_N(N,second)
    fifth.add(N*10000+N*1000+N*100+N*10+N)
    if number in fifth:
        return 5

    sixth = operation_N(N,second)
    sixth.add(N*100000+N*10000+N*1000+N*100+N*10+N)
    if number in sixth:
        return 6

    seventh = operation_N(N,second)
    seventh.add(N*1000000+N*100000+N*10000+N*1000+N*100+N*10+N)
    if number in seventh:
        return 7

    return -1