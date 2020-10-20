class Mother:
    __name = '?'

    def __init__(self, name):
        self.__name = name

    def __str__(self):
        return self.get_str()

    def get_name(self):
        return self.__name

    def set_name(self):
        self.__name = name

    def get_str(self):
        return f'Mother: {self.get_name()}'

class Daughter(Mother):
    __mother = '?'

    def __init__(self, name, mother):
        super().__init__(name)
        self.__mother = mother

    def get_mother(self):
        return self.__mother

    def set_mother(self, mother):
        self.__mother = mother

    def get_str(self):
        return f'Daughter: {self.get_name()}; Mother: {self.get_mother()}'

if __name__ == '__main__':
    print(Mother('Jessica'))
    print(Daughter('Sofia', 'Jessica'))
