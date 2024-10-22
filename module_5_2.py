class House:
    def __init__(self,name ,number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors
    def go_to(self,new_floor):
        if new_floor > self.number_of_floors or new_floor <1:
            print('"Такого этажа не существует"')
        else:

            for i in range(new_floor):
                print (i+1)

    def __len__(self):
        s=self.number_of_floors
        return s
    def __str__(self):
        s='Название: '+ str(self.name) + ", кол-во этажей: "+str(self.number_of_floors)
        return s  # 'Название: ',self.name, ", кол-во этажей: ", self.number_of_floors

h1= House('ЖК Эльбрус', 30)
h2= House('СНТ Междуречье 15-7',2)

# __str__
print(h1.__str__())
print(h2.__str__())

# __len__
print(h1.__len__())
print(h2.__len__())