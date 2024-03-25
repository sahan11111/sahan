class Person:
    
    def __init__(self,name,age,password):
        self.name=name
        self._age=age#protected
        self.__password=password
    @property
    def password(self,password):
        return self.__password
    @password.setter
    def password(self,password):
        self.__password=password
    
ram=Person()
    
    
    