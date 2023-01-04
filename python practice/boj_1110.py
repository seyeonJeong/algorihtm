

# num을 int로 처리하기 싫어서 배열로 쓰는 방법으로 풀려니까 사칙연산 부분에서 int가 아니라 계속 오류가 났다
# 그냥 int는 int로 다루는게 나중에 오류도 잡기 편하고 그냥 그게 맞는것 같다.
# 다른 사람 풀이도 비슷하게 한걸보니 수의 자리 관련은 그냥 나머지 연산 이용하자

num = int(input())

diff_num = num
count = 0


while(1):

    num_first = int(diff_num/10)
    num_second = diff_num % 10

    diff_num = num_first + num_second
    diff_num = diff_num % 10
    diff_num = diff_num + (num_second * 10)
    count += 1
    if(diff_num == num):
        break

print(count)



