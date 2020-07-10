# def square2(num): return num * num


# def square3(num): return num*num


# print(square2(7))
nums = [1, 2, 3, 4, 5]
# doubles = map(lambda x: x*2, nums)
# for num in doubles:
#     print(num)


doubles = list(filter(lambda x: x % 2 == 0, nums))
for num in doubles:
    print(num)
