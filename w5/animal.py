class Animal:
    __animal = '?'
    __age = '?'

    def __init__(self, name, age):
        self.__name = name
        self.__age  = age

    def get_name(self):
        return self.__name

    def get_age(self):
         return self.__age

    def __str__(self):
        return self.get_str()

class Zebra(Animal):
    __color = '?'

    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.__color = color

    def get_color(self):
        return self.__color

    def get_str(self):
        return f"Name: {self.get_name()}; Age: {self.get_age()}; Color: {self.get_color()}"

class Dolphin(Animal):
    __color = '?'

    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.__color = color

    def get_color(self):
        return self.__color

    def get_str(self):
        return f"Name: {self.get_name()}; Age: {self.get_age()}; Color: {self.get_color()}"

if __name__ == '__main__':
    print("Zebra's characteristics: ", Zebra('Plotva', 5, 'Black and White'))
    print("Dolphin's characteristics: ", Dolphin('Nemo', 7, 'Grey'))
