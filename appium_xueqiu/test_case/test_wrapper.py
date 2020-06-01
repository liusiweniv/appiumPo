


#*args, **kwargs接受任意参数
from functools import wraps


def F(a):
    def extend(func):
        @wraps(func)
        def hello(*args, **kwargs):
            print("hello")
            print(a)
            print(args)
            print(kwargs)
            func(*args, **kwargs)
            print("good by")

        return hello
    return extend


# @extend("aaaaaa")
# def tmp(a: int, b: str ,c,d=1)-> int:
#     print("tmp")
#     return 1

@F("aaaaaa")
def tmp()-> int:
    print("tmp")
    return 1
        
def test_wrapper():
    # tmp(1,2,3,d=10)
    #用__annotations__需要在装饰器函数上加上@wraps(func)

    # print(tmp.__annotations__)
    print(tmp())
