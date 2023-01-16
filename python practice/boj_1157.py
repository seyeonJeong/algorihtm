
words = input().upper()
dic = {}

for i in words:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1

dic_sort = sorted(dic.items(), key = lambda item: item[1], reverse= True) # 딕셔너리를 정렬

if len(dic_sort) > 1: # 하나 있을때랑 구별해 줘야 런타임 에러가 안난다.
    if dic_sort[0][1] == dic_sort[1][1]: # (정렬되었기 때문에) 만약 처음과 두번째 value가 같다면 최대 알파벳이 겹치는 것
        print('?')
    else:
        print(dic_sort[0][0])
else: # 하나만 있을 경우 그냥 그 알파벳을 출력해준다.
    print(dic_sort[0][0])

# 딕셔너리를 처음 써 보았다.  문제에서 알파벳과 그 개수를 연관지어서 말하고 있음
