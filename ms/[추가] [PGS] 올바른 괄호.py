def solution(s):
    stack = []

    for i in range(len(s)):
        print(stack)
        if s[i] == '(':
            stack.append('(')
        elif s[i] == ')':
            if len(stack) == 0:
                return False
            elif stack[-1] == '(':
                stack.pop()

    if len(stack) != 0:
        return False
        
    return True
