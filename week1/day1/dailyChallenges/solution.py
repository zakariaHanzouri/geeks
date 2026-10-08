# Challenge 1

# number = int(input("Enter a number: "));
# length = int(input("Enter a length: "));


# multiplicationList=[];

# for i in range(1,length+1):
#     multiplicationList.append(i*number);


# print(f"number: {number} - length {length} -> {multiplicationList}");    

# ------------------------------------------------------------------------------------


# Challenge 2


string = input("Enter a word: ");

string_list=[];

for i in range(len(string)):

   string_list.append(string[i]);

   
i=0;

while i < len(string_list):
    j = i+1;

    while j < len(string_list):
        if string_list[i] == string_list[j]:
            string_list.pop(j);
        else:
            j +=1;

    i += 1;


finalResult="";
for i in range(len(string_list)):
    finalResult += string_list[i];


print(f"user's word: {string} -> {finalResult}");



