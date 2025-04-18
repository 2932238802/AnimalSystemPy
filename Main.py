from Animal import Animal
from Common import AnimalKind
from Hotel import Hotel
from PythonShell import PythonShellForAnimal

def main():
    hotel_ = Hotel()

    hotel_.AddRectRoom(2,3,4,101)
    hotel_.AddRectRoom(1,4,4,102)
    hotel_.AddRectRoom(4,2,1,103)
    hotel_.AddRectRoom(2,3,1,104)
    hotel_.AddRectRoom(1,2,1,105)
    hotel_.AddRectRoom(2,1,2,106)
    hotel_.AddRectRoom(2,3,3,107)
    hotel_.AddRectRoom(2,4,1,108)
    hotel_.AddRectRoom(1,1,2,109)
    hotel_.AddRectRoom(2,3,3,110)
    hotel_.AddRectRoom(2,1,1,111)
    hotel_.AddCircleRoom(2,112)
    hotel_.AddCircleRoom(3,113)
    hotel_.AddCircleRoom(4,114)
    hotel_.AddCircleRoom(5,115)
    hotel_.AddCircleRoom(6,116)
    hotel_.AddCircleRoom(7,117)
    print('-'*30)

    animal_a = Animal("熊大",AnimalKind.Mammal,3,3,4)
    animal_b = Animal("熊二",AnimalKind.Mammal,4,4,2)
    animal_c = Animal("大鸟",AnimalKind.Bird,5,3,2)
    animal_g = Animal("大鸟妈妈",AnimalKind.Bird,2,3,5)
    animal_h = Animal("大鸟爸爸",AnimalKind.Bird,2,3,4)
    animal_d = Animal("印度二嫂",AnimalKind.Reptile,4,3,4)
    animal_e = Animal("莎莎",AnimalKind.Fish,4,3,2)
    animal_f = Animal("娃娃鱼",AnimalKind.Fish,2,2,4)
    print('-'*30)


    hotel_.CheckIn(animal_a)
    hotel_.CheckIn(animal_b)
    hotel_.CheckIn(animal_c)
    hotel_.CheckIn(animal_d)
    hotel_.CheckIn(animal_e)
    hotel_.CheckIn(animal_f)
    hotel_.CheckIn(animal_g)
    hotel_.CheckIn(animal_h)
    print('-'*30)


    hotel_.CheckOut(animal_e)
    hotel_.CheckOut(animal_a)
    hotel_.CheckOut(animal_f)
    hotel_.CheckOut(animal_c)
    hotel_.CheckOut(animal_b)
    hotel_.CheckOut(animal_g)
    hotel_.CheckOut(animal_h)
    print('-'*30)
    print("以上展现的是这些功能的完美实现")
    print("下面是我实现的扩展循环")

    shell_ = PythonShellForAnimal(hotel_)
    shell_.ShowHelp()
    shell_.Run()




if __name__ == '__main__':
    main()