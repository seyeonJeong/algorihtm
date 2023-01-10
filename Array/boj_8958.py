num = int(input())

score = [0 for j in range(num)]

# o이면 1증가 연속이면 또 계속 증가 x이면 다시 초기화
def count_score(case):
    sum = 0
    tmp = 0
    for k in range(len(case)):
        if case[k] == 'O':
            tmp += 1
            sum += tmp
        else:
            tmp = 0
    return sum

# 배열과 함수를 통한 구현
for i in range(num):
    result = input()
    score[i] = count_score(result)

for n in range(num):
    print(score[n])

