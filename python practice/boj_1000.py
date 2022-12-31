

#input 함수 정리
# 사용자의 입력을 받음
# 문자열로 취급한다.
# 사용자의 입력을 반환
# 입력은 엔터 전까지 모두 받음

# 한번에 값 두개 입력받기
# 변수1, 변수2 = input().split(기준문자)
a,b = map(int,input().split()) # 공백을 기준으로 분리 input(입력받을때 하고싶은말?)

# map에 int와 input().split()을 넣으면 split의 결과를 모두 int로 변환

print(a+b)

print(a-b)

print(a*b)

print(a/b)