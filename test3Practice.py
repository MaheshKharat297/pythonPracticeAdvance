def f1(func):
    def wrapper(*args, **kwargs):
        print("Stating func.......")
        print(func(*args, **kwargs))
        print("Ending func.......")


    return wrapper
@f1
def f(a, b=9):
    print(a, b)
@f1
def add(x, y):
    return x+y

add(3, 4)


###Genarators

def sqare_numbr(nums):
    for i in nums:
        yield i*i

my_nums = sqare_numbr([1,2,3,4,5])

for i in my_nums:
    print(i)


lst = [1,2,4,2,6,3]

m = sorted(lst)

lst.sort()
print(m)
print(lst)
