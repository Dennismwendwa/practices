

class User:
    def __init__(self, name, age, address):
        self.name = name
        #self.set_name(name)
        self.age = age
        self.address = address
    
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name):
        if name == "fuck":
            print("Bad name. Name not set")
            self.__name = "No name"
        elif isinstance(name, int):
            print("name should be words")
            self.__name = "No name"
        else:
            self.__name = name


user1 = User("Dennis", 30, "80100-674")
user2 = User("fuck", 32, "46987")


print(user1.name)
print(user2.name)
