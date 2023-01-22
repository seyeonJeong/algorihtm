t = int(input())

for i in range(t):
    floor = int(input())
    room = int(input())

    zero_f = []


    if floor == 0:
        print(room)
    else:
        for j in range(1,room+1):
            zero_f.append(j)

        for a in range(floor):
            for b in range(1, room):
                zero_f[b] += zero_f[b-1]
        print(zero_f[-1])



