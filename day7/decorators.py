
def star(func):
    def wrapper():
        print("*"*10)
        func()
        print("*"*10)
    return wrapper

# @star
# def hello():
#     print("hello")
# hello()

    


# def bye():
#     print("bye")
# star(bye)()

def hash(func):
    def wrapper():
        print("#"*10)
        func()
        print("#"*10)
    return wrapper

@hash
@star
def hello():
    print("hello")
hello()