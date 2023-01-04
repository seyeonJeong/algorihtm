

result = int(input())
num = int(input())
receipt = [[0 for i in range(2)] for j in range(num)]

for i in range(num):
    receipt[i][0], receipt[i][1] = map(int, input().split())

def calc_recipt(receipt):
    sum = 0
    for i in range(num):
        sum = sum + (receipt[i][0] * receipt[i][1])

    if(sum == result):
        print('Yes')
    else:
        print('No')

calc_recipt(receipt)

# 다른 사람 풀이인데 굳이 2차원 배열을 만들 필요는 없었다. 함수를 일부러 여러개 썼는데 어떤게 맞는지는 모르겠다.
# 굳이 값을 저장하지 않아도 되므로 2차원 배열을 만드는건 비효율적으로 보인다.
# # 첫째 줄에는 영수증에 적힌 총 금액 X가 주어진다.
# total = int(input())
#
# # 둘째 줄에는 영수증에 적힌 구매한 물건의 종류의 수 N이 주어진다.
# type = int(input())
#
# sum = 0  # 총 금액
#
# # 이후 N개의 줄에는 각 물건의 가격 a와 개수 b가 공백을 사이에 두고 주어진다.
# for i in range(type):
#     a, b = map(int, input().split())
#     sum += a * b
#
# # 총 금액과 영수증 금액 같은지 확인
# if total == sum:
#     print("Yes")
# else:
#     print("No")
# 출처 : https://coding-nurse.tistory.com/423
