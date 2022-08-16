import math

def solution(progresses, speeds):
    finish = []
    queue = []
    answer = []
    
    for i in range(len(progresses)):
        finish.append(math.ceil((100 - progresses[i]) / speeds[i]))

    for i in range(len(finish)):
        if (len(queue) == 0) or (queue[0] >= finish[i]):
            pass
        else:
            answer.append(len(queue))
            queue.clear()

        queue.append(finish[i])

        if i == (len(finish) - 1):
            answer.append(len(queue))

    return answer
