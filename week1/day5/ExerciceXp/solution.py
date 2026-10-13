# Execice 1

# class Cat:

#     def __init__(self, cat_name, cat_age):
#         self.cat_name = cat_name;
#         self.cat_age = cat_age


# 1.Instantiate three Cat objects using the code provided above.

# cat1 = Cat("Diamond",10);
# cat2 = Cat("Tom",20);
# cat3 = Cat("lussi",90);

# 2.Outside of the class, create a function that finds the oldest cat and returns the cat.

# allCats=[cat3,cat1, cat2];

# def oldestCat(allCats):
    
#     oldes_cat= allCats[0];

#     for i in range(1,len(allCats)):
#         if allCats[i].cat_age > oldes_cat.cat_age:
#             oldes_cat =  allCats[i];
    
#     return oldes_cat;

# 3. Print the following string: “The oldest cat is <cat_name>, and is <cat_age> years old.”. Use the function previously created.

# oldestCat= oldestCat(allCats);

# print(f"The oldest cat is {oldestCat.cat_name} and is {oldestCat.cat_age} years old.")

# ______________________________________________________________________

# Execice 2

# Instructions

# Create a class called Dog.

class Dog:
    # In this class, create an __init__ method that takes two parameters : name and height. This function instantiates two attributes, which values are the parameters.
    def __init__(self, name, height):
        self.name =  name;
        self.height = height;

    # Create a method called bark that prints the following string “<dog_name> goes woof!”.
    def bark(self):
        print(f"{self.name} goes woof!")

    # Create a method called jump that prints the following string “<dog_name> jumps <x> cm high!”. x is the height*2.
    def jump(self):
        print(f"{self.name} jumps {self.height*self.height} cm high!");


# Outside of the class, create an object called davids_dog. His dog’s name is “Rex” and his height is 50cm.

davids_dog= Dog("Rex",50);

# Print the details of his dog (ie. name and height) and call the methods bark and jump.

details=f"dog's name is {davids_dog.name} and its height is {davids_dog.height}";

print(details);
davids_dog.jump();
davids_dog.bark();

# Create an object called sarahs_dog. Her dog’s name is “Teacup” and his height is 20cm.

sarahs_dog=Dog("Teacup",20);


# Print the details of her dog (ie. name and height) and call the methods bark and jump.


details=f"dog's name is {sarahs_dog.name} and its height is {sarahs_dog.height}";

print(details);
sarahs_dog.jump();
sarahs_dog.bark();

# Create an if statement outside of the class to check which dog is bigger. Print the name of the bigger dog.

if davids_dog.height > sarahs_dog.height:
    print(f"{davids_dog.name} is the bigger");
else:
    print(f"{sarahs_dog.name} is the bigger");


# ________________________________________________________________________________________________________

# 🌟 Exercise 3 : Who’s the song producer?

# Instructions

# 1. Define a class called Song, it will show the lyrics of a song.

# class Song:
    # Its __init__() method should have two arguments: self and lyrics (a list).
    # def __init__(self,lyrics):
    #     self.lyrics= lyrics;
    
    # 2. Inside your class create a method called sing_me_a_song that prints each element of lyrics on its own line.
    # def sing_me_a_song(self):
    #     for sentence in self.lyrics:
    #         print(sentence);


# 3. Create an object, for example:

# mySong= Song(["This is the first line of the song","but this is the seeeeeeecond ooooooooone","yeeeeeeeeeeeeeeeeh"]);

# stairway= Song(["There’s a lady who's sure","all that glitters is gold", "and she’s buying a stairway to heaven"])

# 4. Then, call the sing_me_a_song method. The output should be:

# mySong.sing_me_a_song();
# stairway.sing_me_a_song();

# ________________________________________________________________________________________________________

# Exercice 4:

class Zoo:
    animals=[];
    name="";
    def __init__(self, zoo_name):
        self.zoo_name = zoo_name;

    def add_animal(self,new_animal):
        Zoo.animals.append(new_animal);
    
    def get_animals(self):
        for animal in Zoo.animals:
            print(animal);

    def sell_animal(self,animal_sold):
        if animal_sold in Zoo.animals:
            Zoo.animals.remove(animal_sold);
            print("the animal was solden")
        
    def sort_animals(self):
        sortedAnimals=sorted(self.animals);
        animalsGroups={};
       
        for animal in sortedAnimals:
             firstLetter = animal[0];
             if firstLetter not in animalsGroups:
                 animalsGroups[firstLetter]= [];
            
             animalsGroups[firstLetter].append(animal);

        return animalsGroups;

    def get_groups(self):

        for key,val in self.sort_animals().items():
            print(f"{key}");
            for animal in val:
                print(animal);



new_york_zoo = Zoo("new_york_zoo");

new_york_zoo.add_animal("giraffe");
new_york_zoo.add_animal("Bear");
new_york_zoo.add_animal("Ants");
new_york_zoo.add_animal("elephant");
new_york_zoo.add_animal("eagle");

new_york_zoo.get_animals();

new_york_zoo.sell_animal("giraffe");
new_york_zoo.get_animals();
new_york_zoo.get_groups();
