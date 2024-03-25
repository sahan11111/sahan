# class GrandFather:
#     house="luxery house"

# class Father(GrandFather):
#     car="lambogini"
# class Mother:
#     necklace="gold"
# class Son(Father,Mother):
#     gaming_consol="PS5"

# son=Son()
# # print(son.house)# class Father(GrandFather):
# print(son.necklace)
# print(son.car)


class GrandFather:
    house="luxery house"
    def __init__(self):
        print(f"i own a {self.house}")
        

class Father(GrandFather):
    car="lambogini"
    def __init__(self):
        print(f"i own a {self.car}")
        print("i own new house")
        super().__init__()
class Mother:
    necklace="gold"
    def __init__(self):
        print(f"i own a {self.necklace}")
class Son(Father,Mother):
    gaming_consol="PS5"
    def __init__(self):
        print(f"i own a {self.gaming_consol}")

father=Father()

