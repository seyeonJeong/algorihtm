
# 검색해서 풀긴 했으나 많은 인사이트를 얻을 수 있었던 문제
# 3의 배수 5의 배수에 헷갈릴 수 있으나, 배수란 것은 결국엔 덧셈을 여러번 한것
# 5의 배수가 아니라면 3으로 하나하나 빼면서 설탕 가방 갯수를 늘려간다

n = int(input())

bag = 0

while n >= 0:
    if n % 5 ==0:
        bag +=  (n//5)
        print(bag)
        break
    n -= 3
    bag += 1

else:
    print(-1)



