import sys

n = int(sys.stdin.readline())

list = []
stack = []
nlist = []
for i in range(n):
    list.append(int(sys.stdin.readline()))

j = 1 # 넣는 수
p = 0 # 가리키는 포인터
k = 0 # 포인터 2

while True:
    stack.append(j)
    p += 1
    print('+')
    if list[k] == j:
        print('-')
        stack.pop()
        nlist.append(stack[a])
        k += 1
        p -= 1


    for a in range(len(stack)):
        if stack[a] == list[k]:
            if a == len(stack) -1:
                list[k] == stack[a]
                print('-')
                stack.pop()
                nlist.append(stack[a])
                k += 1
                p -= 1
            else:
                for b in range(len(stack)-1, a):
                    stack.pop()
                    print('-')
                    k += 1
                    p -= 1


    j += 1
    if nlist == list:
        break


# 23.01.25 ~ ing



