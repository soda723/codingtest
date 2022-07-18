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

def operation_N2(bs1, bs2):
    after_set = set()
    for a in bs1:
        for b in bs2:
            after_set.add(a + b)
            after_set.add(a-b)
            after_set.add(a*b)
            after_set.add(b-a)
        try:
            after_set.add(a/b)
            after_set.add(b/a)
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

    forth = operation_N(N,third) #1+3
    forth = forth | operation_N2(second, second)#2+2
    forth.add(N*1000+N*100+N*10+N)
    if number in forth:
        return 4

    fifth = operation_N(N,forth) #1+4
    fifth = fifth | operation_N2(second, third)#2+3
    fifth.add(N*10000+N*1000+N*100+N*10+N)
    if number in fifth:
        return 5

    sixth = operation_N(N,fifth) #1+5
    sixth = sixth | operation_N2(second, forth)#2+4
    sixth = sixth | operation_N2(third, third)#3+3
    sixth.add(N*100000+N*10000+N*1000+N*100+N*10+N)
    if number in sixth:
        return 6

    seventh = operation_N(N,sixth) # 1+6
    seventh = seventh | operation_N2(second, fifth)#2+5
    seventh = seventh | operation_N2(third, forth)#3+4
    seventh.add(N*1000000+N*100000+N*10000+N*1000+N*100+N*10+N)
    if number in seventh:
        return 7
    
    eighth = operation_N(N,seventh) #1+7
    eighth = eighth | operation_N2(second, sixth)#2+6
    eighth = eighth | operation_N2(third, fifth)#3+5
    eighth = eighth | operation_N2(forth, forth)#4+4
    eighth.add(N*10000000+N*1000000+N*100000+N*10000+N*1000+N*100+N*10+N)
    if number in eighth:
        return 8

    return -1