import sys

n = int(input())
queue = []
front = 0
rear = 0
for i in range(n):
    word = sys.stdin.readline().split()
    oper = word[0]

    if oper == 'push':
        queue.append(word[1])
        rear += 1
    elif oper == 'pop':
        if rear == front:
            print(-1)
        else:
            print(queue[front])
            front += 1

    elif oper == 'size':
        print(rear - front)
    elif oper == 'empty':
        if rear == front :
            print(1)
        else:
            print(0)
    elif oper == 'front':
        if rear == front:
            print(-1)
        else:
            print(queue[front])
    elif oper == 'back':
        if rear == front:
            print(-1)
        else:
            print(queue[rear-1])

# 시간초과 에반데 진짜로