import sys


item = []

num = int(sys.stdin.readline()) # 이거 안쓰면 런타임 에러가 난다.
for i in range(num):

    word = sys.stdin.readline().split()
    oper = word[0] # 여기서 많이 애먹었는데 결국 검색해서 풀었다. word를 받는데 띄어쓰기를 기준으로 word[0]과 word[1]로 나뉜다.


    if oper == 'top': # 맨위에 있는것을 출력 없으면 -1
        if len(item) == 0:
            print(-1)
        else:
            print(item[-1])
    elif oper == 'size': # 사이즈를 출력한다.
        print(len(item))
    elif oper == 'pop': # 맨위에 있는것을 출력 후 삭제
        if len(item) == 0:
            print(-1)
        else:
            print(item.pop())
    elif oper == 'empty': # 비어있으면 1, 아니면 0 출력
        if len(item) == 0:
            print(1)
        else:
            print(0)
    elif oper == 'push': # 값을 넣는다.
        item.append(word[1])

