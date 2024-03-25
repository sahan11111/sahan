# a=10

# def hello():
#     a=11
#     print(a)
# print(a)
# hello()a=10

# def hello():
#     global a
#     a=11
#     print(a)
    
# hello()
# print(a)

x=9

def outer():
    x=10
    def inner():
        x=12
        print("inner sees x as",x)
        
    inner()
    print("outer sees x as",x)
    
outer()
print("global sees as",x)

