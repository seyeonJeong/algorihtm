

fix, flexible, price = map(int, input().split())

# output = 0
# input = fix
if flexible >= price:
    print(-1)
else:
    print(fix//(price-flexible) + 1)



# 일일히 다 구한것
# while True:
#     if flexible >= price:
#         print(-1)
#         break
#
#     output += price
#     input += flexible
#     cnt += 1
#     if output > input:
#         print(cnt)
#         break




