# def sum(a,b)
#     return a+b #normal function

# sum=lambda a,b:a+b

# print(sum(1,2))
# 2 times
def func(n):
    return lambda x:x*n

doubler=func(2)

print(doubler(10))

# 3 times
def func(n):
    return lambda x:x*n

triple=func(3)

print(triple(10))

# 4 times
def func(n):
    return lambda x:x*n

four_times=func(4)

print(four_times(10))