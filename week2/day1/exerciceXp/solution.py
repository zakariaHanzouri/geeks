# class Pets():
#     def __init__(self, animals):
#         self.animals = animals

#     def walk(self):
#         for animal in self.animals:
#             print(animal.walk())


# class Cat():
#     is_lazy = True

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def walk(self):
#         return f'{self.name} is just walking around'


# class Bengal(Cat):
#     def sing(self, sounds):
#         return f'{sounds}'


# class Chartreux(Cat):
#     def sing(self, sounds):
#         return f'{sounds}'


# class Siamese(Cat):
#     pass


# bengal = Bengal("Bengal",3);
# chartreux = Chartreux("Chartreux",3);
# siamese = Siamese("Siamese",3);


# all_cats=[bengal,chartreux,siamese]

# saras_pets=Pets(all_cats)

# saras_pets.walk();



# _________________________________________________________________________________________________

# Exercice 2:

# Create a class called Dog with the following attributes:

# nam
# ag
# weight

# class Dog:
#     def __init__(self,name,age, weight):
#         self.name = name;
#         self.age = age;
#         self.weight = weight;


#     # Implement the following methods in the Dog class:

#     # bark: returns a string which states: “<dog_name> is barking”.

#     def bark(self):
#         return f"{self.name} is barking";


#     # run_speed: returns the dog’s running speed: (weight / age * 10).

#     def run_speed(self):
#         return (self.weight / (self.age *10));

#     # fight: takes a parameter which value is another Dog instance, called other_dog. This method returns a string stating which dog won the fight. The winner should be the dog with the higher run_speed x weight.

#     def fight(self,other_dog):

#         if (self.run_speed() * self.weight) > (other_dog.run_speed() * other_dog.weight):
#             return f"The winner is {self.name} ";
#         else:
#             return f"The winner is {other_dog.name} ";



# # Create 3 dogs and run them through your class.


# rex = Dog("Rex",3,10);
# lussi = Dog("Lussi",5,20);
# luna = Dog("Luna",15,25);


# all_dogs=[rex,lussi,luna];
# for dog in all_dogs:
#     print(dog.bark());
#     print(dog.run_speed());
#     print("----------------------------------");

# print(rex.fight(luna));

# _________________________________________________________________________________________________

#Exercice 3:

class Family:

    def __init__(self,members,last_name):
        self.members= members;
        self.last_name = last_name;

    # born: adds a child to the members list. Use **kwargs. Don’t forget to print a message congratulating the family.

    def born(self,**kwargs):

        self.members.append(kwargs);

        print("Congartulations "+self.last_name);
    # is_18: takes the name of a family member as a parameter and returns True if they are over 18 and False if not.


    def is_18(self,name):
        for member in self.members:
            if member.get("name") == name:
                return member.get("age") >= 18


    # family_presentation: a method that prints the family’s last name and all the members’ details

    def family_presentation(self):

        print(f"{self.last_name} Family:\n");

        for member in self.members:
            print(member.get("name"));
            print(member.get("age"));
            print(member.get("gender"));
            print(member.get("is_child"));
            print(member.get("power"));
            print("-----------------------------------------\n");

           


# Create an instance of the Family class, with the last name of your choice, and the below members. Then call all the methods you created in Point 2.

members=[
    {'name':'Michael','age':35,'gender':'Male','is_child':False},
    {'name':'Sarah','age':32,'gender':'Female','is_child':False}
];

Hanzouri_family= Family(members,"Hanzouri");

Hanzouri_family.family_presentation();
Hanzouri_family.born(name="nadir",age=1);
print(Hanzouri_family.is_18("nadir"));


#Exercie 4:

class TheIncredibles(Family):
    

    def use_power(self, **kwargs):
        if super().is_18(kwargs.get("age")):
            print(member.get("power"));
        else:
            print("You are under the 18 to use the power");


    def incredible_presentation(self):
        print("Here is our powerful family")

        super().family_presentation()



powerful_family=[
    {'name':'Michael','age':35,'gender':'Male','is_child':False,'power': 'fly','incredible_name':'MikeFly'},
    {'name':'Sarah','age':32,'gender':'Female','is_child':False,'power': 'read minds','incredible_name':'SuperWoman'}
];


theIncredibles= TheIncredibles(powerful_family,"Incredibles");

theIncredibles.incredible_presentation();

theIncredibles.born(name="Jack ",age=1,power="Unknown Power");

theIncredibles.use_power(name="Jack",age=1);
theIncredibles.incredible_presentation();