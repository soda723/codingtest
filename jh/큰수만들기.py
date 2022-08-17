def solution(number, k):
    li = [int(i) for i in number]
    ans = []
    f_idx, b_idx = 0, len(li)-1
    for i in range(len(li)-k): # 앞에서부터 가장 큰 수를 하나씩 빼내는 방식
        b_idx = (k + i + 1) # 큰 수를 찾는 범위를 아직 정해지지 못한 자릿수만큼 제외해 줘야 함
        mxnum = 0
        for j in range(f_idx, b_idx):
            if mxnum < li[j]:
                f_idx = j + 1
                mxnum = li[j]
            if mxnum == 9: # max num이 9면 더 볼 필요가 없음
                break
        ans.append(mxnum)
    ans = list(map(str, ans))
    return ''.join(ans)