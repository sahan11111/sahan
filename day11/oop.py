# class House:
#     windows=10
#     color="red"
#     door=5
    
#     def get_color(self):
#         return self.color
    
#     def set_color(self,color):
#         self.color=color
# ram_ko_ghar=House()
# # print(ram_ko_ghar.door)
# print(ram_ko_ghar.get_color())
# print(ram_ko_ghar.set_color("green"))

# class Pizza:
    
#     def dough(self):
#         print("dough")
#         return self
#     def sause(self):
#         print("sause")
#         return self
#     def cheese(self):
#         print("cheese")
#         return self
#     def sasage(self):
#         print("sausage")
#         return self 
# pizza=Pizza()       
# pizza.dough().sause().cheese().sasage()

# class Burger:
    
#     def Bun(self):
#         print("bun")
#         return self
#     def ketch_up_and_mewonies(self):
#         print("ketch_up_and_mewonies")
#         return self
#     def veg_salade(self):
#         print("veg_salade")
#         return self
#     def cheese(self):
#         print("cheese")
#         return self
#     def patty(self):
#         print("patty")
#         return self 
# burger=Burger()       
# burger.Bun().ketch_up_and_mewonies().veg_salade().cheese().patty()

class House():
    def __init__(self, windows, color, door):
        self.windows = windows
        self.color = color
        self.door = door

    def __str__(self):
        return f"House with {self.windows} windows, {self.color} color, and {self.door} doors"

house = House(1, "red", 4)
print(house)
