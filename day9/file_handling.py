# try:
#     f=open("hello.txt")
#     print(f.readline())
#     f.close()
# except Exception as e:
#     print(e)

# try:
#     f=open("hello.txt")
#     print(f.readlines())
#     f.close()
# except Exception as e:
#     print(e)

# append
# try:
#     f=open("hello.txt","a")
#     f.write("\ni was learning python")
#     f.close()
# except Exception as e:
#     print(e)

# write
# try:
#     f=open("hello.txt","w")
#     f.write("\ni was learning python")
    
#     f.close()
# except Exception as e:
#     print(e)

# delete file
# import os
from time import sleep
try:
    f=open("hello.txt","w")
    f.write("\ni was learning python")
    
    f.close()
    sleep(3)
    # os.remove("hello.txt")
except Exception as e:
    print(e)
    
# user input kun file banau ne ho banau h=nu paryo
# file bhitra content kasari user sanga input mag ne
# read
# input new add garnu..
# last file delete garne pani user input



# homework
# cli application using data type
# todolist
# titel ra discription maaagne
# tyo globle databse