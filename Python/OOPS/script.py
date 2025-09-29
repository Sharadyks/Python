'''class Dog:
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
print(dog2.breed)'''


'''class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old")

person1 = Person("Alice",30)
person1.greet()'''


'''class User:
    def __init__(self, username, email,password):
        self.username = username
        self.email = email
        self.password = password

    def greet(self,user):
        print(f"Sending message to {user.username}: Hi {user.username}, it's {self.username}")

user1 = User("Sharad","ksfbd29@gmail.com","rdd******")
user2 = User("Rohan","ysfbd","dsdbv***")
user1.greet(user2)'''


