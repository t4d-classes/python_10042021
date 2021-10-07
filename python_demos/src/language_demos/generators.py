from collections.abc import Generator

# colors = [ 'red', 'green', 'blue' ]

# for color in colors:
#     print(color)


# r = range(10)

# print(r)
# print(type(r))

# for x in r:
#     print(x)

# def double(x: int) -> int:
#     """ double """
#     print("in double")
#     return x * 2

# # double_nums = []
# # for num in [1,2,3,4,5]:
# #     double_nums.append(double(num))

# # print(double_nums)


# # print(map(double, [1,2,3,4,5]))

# gen = map(double, [1,2,3,4,5])

# print(gen.__next__())


# for n in map(double, [1,2,3,4,5]):
# # for n in [ double(x) for x in [1,2,3,4,5] ]:
# # for n in list(map(double, [1,2,3,4,5])):
#     print(n)


# def get_nums() -> Generator[int, None, None]:
#     """ get nums """

#     print("get num 1")
#     yield 1

#     print("get num 2")
#     yield 2

#     print("get num 3")
#     yield 3

# def get_nums() -> list[int]:
#     """ get nums """

#     nums: list[int] = []

#     print("get num 1")
#     nums.append(1)

#     print("get num 2")
#     nums.append(2)

#     print("get num 3")
#     nums.append(3)

#     return nums


# gen = get_nums()

# print(gen.__next__())

# for n in get_nums():
#     print("in the loop")
#     print(n)


def my_infinite_gen() -> Generator[int, None, None]:
    """ my infinite gen """
    x = 0

    while True:
        yield x
        x = x + 1

gen = my_infinite_gen()

print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))


