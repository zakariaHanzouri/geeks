

# Exercie 1

# print("Hello world\nHello world\nHello world\nHello world");

# --------------------------------------------------------------------------------------------------

# Exercice 2


# power = (99**3);
# result = power * 8;

# print(f"Result: {result}");


# --------------------------------------------------------------------------------------------------

# Exercice 3

# myName="zakaria";
# userName= input("What's your name: ").lower();

# if myName == userName:
#     print("Congrats we have the same name!!!!!");
# else:
#     print("Sorry we have diffirent names");    


# --------------------------------------------------------------------------------------------------

# Exercice 4

# validatedHeight= 145;
# userHeight= int(input("Enter your height in cm: "));

# if (userHeight >= validatedHeight):
#     print("You're tall enough to ride a roller coaster!!!");
# else:
#     print("Sorry, You're NOT tall enough");


# --------------------------------------------------------------------------------------------------

# Exercice 5

# my_fav_numbers= {1,2,3,4,5,6};

# my_fav_numbers.add(10);
# my_fav_numbers.add(11);

# my_fav_numbers.discard(11);

# friend_fav_numbers={6,7,8,9};

# our_fav_numbers= my_fav_numbers.union(friend_fav_numbers);

# print(our_fav_numbers);


# --------------------------------------------------------------------------------------------------

# Exercice 6

# numbers= {1,2,3,4,5,9}; # we can't add in a tuple because it's immutable data type 



# --------------------------------------------------------------------------------------------------

# Exercice 7

basket = ["Banana", "Apples", "Oranges", "Blueberries"];

# Remove Banana from the list.

# indexOfBanana= basket.index("Banana");

# basket.pop(indexOfBanana);

# --------------

# Remove Blueberries from the list.

# indexOfBlueBerries= basket.index("Blueberries");

# basket.pop(indexOfBlueBerries);

# basket.pop(-1);
# -------------------

# Add Kiwi to the end of the list.

# basket.append("Kiwi");
# -----------------

# Add Apples to the beginning of the list.
# basket.insert(0,"Apples");

# ---------------

# Count how many apples are in the basket.

# howManyApplesInTheBasket=0;

# for fruit in basket:
#     if fruit =="Apples":
#         howManyApplesInTheBasket += 1;


# print(basket);
# print(f"There are {howManyApplesInTheBasket} apples");

# ----------------

# Empty the basket.
# basket.clear();

# Print(basket)
# print(basket);

# -----------------------------------------------------------------

# Exercice 8

sandwich_orders = ["Tuna sandwich", "Pastrami sandwich","Pastrami sandwich", "Avocado sandwich", "Pastrami sandwich", "Egg sandwich", "Chicken sandwich", "Pastrami sandwich"];

finished_sandwiches=[];

counter = 0;

while counter < len(sandwich_orders):

    if sandwich_orders[counter] == "Pastrami sandwich":
        sandwich_orders.pop(counter);
    else:
        counter += 1;
    


for i in range(len(sandwich_orders)):
   order=sandwich_orders.pop(0);
   finished_sandwiches.append(order);
    
print(finished_sandwiches);
print(sandwich_orders);    


# 5

for order in finished_sandwiches:
    print(f"I made your {order}");