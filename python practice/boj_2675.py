
num = int(input())

for i in range(num):
    iter, word = input().split()

    text = ''
    for j in word:
        text += int(iter) * j
    print(text)



# 한번 틀렸었는데, 그때는 word를 배열 취급해서 하나하나 증가시켜서 print를 계속 박는 식으로 출력했는데 아닌가보다
# 빈 text를 하나 만들어서 word의 하나하나를 반복하는것이 더 파이썬에 알맞은 풀이인거같기도 하다.

