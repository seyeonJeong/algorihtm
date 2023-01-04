
#EOF를 쓰는 문제여서 가져왔다.
#EOF는 End Of File -> 파일의 끝이라는 뜻이다. 길이가 주어지지 않아도 프로그램이 파일의 끝을 알 수 있어야함
# 즉, 입력의 갯수가 주어지지 않아도 끝낼 수 있어야함 (아무것도 안치고 엔터를 치면 끝나는 것과 같이.. )
# 파이썬의 EOF는 아예 몰라서 블로그에서 가져왔다.

# 첫번째 방법은 예외처리를 이용하여, EOF를 구현한다. EOFError가 일어나면 더이상 수를 받지 않는다.
while True:
    try:
        a, b = map(int, input().split())
        print(a+b)

    except EOFError:
        break

# 다른 방법
# import sys
#
# lines = sys.stdin.readlines()
#
# for line in lines:
#     A, B = map(int, line.split())
#     print(A+B)

#출처 : https://y00n-lee.tistory.com/9