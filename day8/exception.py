# while True:
#     try:
#         a=int(input("enter a number"))
#         b=int(input("enter a number"))
#         if a==5:
#             raise Exception("Input cannot be 5")
#         print(a/b)
#     except ZeroDivisionError:
#         print("A number cannot divided zero")
    
#     except ValueError:
#         print("Input fields requirement only integer..")
        
#     except Exception as e:
#         print(f"something went wrong at{e}")
fruits=['apple','orange','banana','kiwi']
total_index=len(fruits)-1
while True:
    try:
        
        index=int(input(f"enter a index betwen o to {total_index}"))
        print(fruits[index])
        
    except IndexError:
        print(f"Entered value must me lesser or equal to  {total_index}")

    except ValueError:
        print('Input must be only integer..')
    
    except Exception as e:
        print("something went wrong",e) 