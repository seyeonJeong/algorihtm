t = int(input())

for i in range(t):
    floor = int(input())
    room = int(input())

    zero_f = [] # 0층은 미리 받아야한다.


    if floor == 0: # 0층이면 그냥 바로 출력함
        print(room)
    else:
        for j in range(1,room+1): # 1, room까지
            zero_f.append(j)

        for a in range(floor):
            for b in range(1, room):
                zero_f[b] += zero_f[b-1] # 0층이 아니라면 각 층은 본인 층 -1 층의 0~본인 호실까지의 인원수의 합이다. 그렇다면 이전 배열의 값은 0~본인 호실 -1 층 까지의 합이므로, 본인 층만 더하면 해결
        print(zero_f[-1])



