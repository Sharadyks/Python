class Dog:
    def __init__(self,name,breed,owner):
        self.name= name
        self.breed = breed
        self.owner = owner

    def bark(self):
        print("Whoof Whoof")


class Owner:
    def __init__(self,name,address,contact_number):
        self.name = name
        self.address = address
        self.contact_number = contact_number

owner1 = Owner("Sharad","Faridabad","807666****")
owner2 = Owner("Rohan","Delhi","935625****")

dog1 = Dog("Tommy","hello",owner1)
dog1.bark()
print(dog1.name)
print(dog1.breed)
print(dog1.owner.name)

dog2 = Dog("Freya","Hi",owner2)
dog2.bark()
print(dog2.name)
print(dog2.breed)
