

num1 = int(input())
num2 = int(input())

# num1과 num2의 세번째 자리 수를 곱한다.
num2_third = num2 % 10
first_ans = num1 * num2_third

#num1과 num2의 두번째 자리 수를 곱한다.
num2_second = int((num2 % 100) / 10)
second_ans = num1 * num2_second

#num1과 num2의 첫번째 자리 수를 곱한다.
num2_first = int(num2 / 100)
third_ans = num1 * num2_first

print(first_ans)
print(second_ans)
print(third_ans)
print(num1 * num2)

# 다른 사람 풀이

# num1 = int(input()) int로 만든다.
# num2 = input() 그냥 받음 이렇게 해서 배열로 써도 되나봄

# first_ans = num1 * int(num2[2])
# second_ans = num1 * int(num2[1])
# third_ans = num1 * int(num2[0])

# print(first_ans, second_ans, third_ans , num1*num2, sep='\n')

# sep 이라는 기능이 있었다..
# 구분자 --> 문자열 사이사이 넣어줌 사이사이 줄바꿈을 해줘서 print를 여러개 안해도 된다.




