# # f string

# # name = "shivam kumar"

# # print("your name is {}".format(name))

# # print(f'Your name is {name}')


# # result = 2*(3+4)**2/5-6
# # print(ceil(result))


# # mgs = ("Hello is this python class")

# # lst = mgs.split()
# # print(lst)
# # print(type(lst))


# # for i in range (10):
# #     print(i)

# # i = 0 
# # while i < 10:
# #     print(i)
# #     i = i+1

# # me = "SHIVAM"
# # for she in me:
# #     if she == "V":
# #         print('VIDUSHI')
# #     else:
# #         print(she)


# # LIST
# name= ["shivam","shahi","data", "scientist"]
# print(name)

# # indexing 
# print(name[0])

# # adding new value into the list
# name.append("Python")
# print(name)

# # remove the value using the value name 

# name.remove("Python")
# print(name)

# # modifying the value
# name[0] = "SHIVAM"
# print(name)

# # adding new value into specific position
# name.insert(1,"top data scientist") #this will insert the data into 1st index 
# print(name)

# # deleting the specific value from the list using del function

# del name[1]
# print(name)

# # finding the length of the list 
# print(len(name))

# # sorting the list
# name.sort()
# print(name)

# name.reverse()
# print(name)


# # pop function (remove the last function of the list and show in the output)
# name.pop()
# removed_value =name.pop()
# print(removed_value) 
# print(name)



# # slicing of list

# # name= ["shivam","shahi","data", "scientist"]
# # print(name[0:3])
# # print(name[::3])

# # sell = [1,25,9,8,7,48,62,15]
# # sell.sort()
# # print(sell)

# # sell.sort(reverse=True)
# # print(sell)

# # timestamp :- 59:35


# #numeric list

# marks = [2,19,28,35,4,35]

# print(marks)


# print(min(marks))
# print(max(marks))
# print(sum(marks))

# # tuple

# days = ('mon', "tues", "wed","thursday")

# print (days[0])
# print(days.count("mon"))
# print(days.index("tues"))

# # dictonaries
# # store the data in key vlaue pairs

# marks = {"English": 32, "Hindi": 50,"Maths":68}

# print(marks)
# print(type(marks))
# print(marks["English"])
# print(marks.values())
# print(marks.items())
# print(marks.keys())

# marks["science"] = 80
# print(marks)

# del marks["Hindi"]
# print(marks)

# # sets {} unordered and no duplicates only unique values 

# set1 = {1,2,3,5,4,4,4,4,4,7,8,8,8,8,8}
# name = {"shivam", "shivam","shahi", "data science"}
# print(name)

# print(set1)

# # convert list into set 

# # lst = [1,2,2,2,2,365,78,9,9,9,9,9,5,4,1,1,1]
# # lst_st = set(lst)
# # print(lst_st)


# # user interaction 
# # user input 

# # name = input("Enter your name ? ")
# # print("Hello", name, "welcome to the new world ")
# # try:
# #     age = int(input("enter your age:-"))

# # except ValueError:
# #     print("The given input is not a digit \n kindlly enter your age in digit")

# # ifelse :

# # age = int(input("enter your age "))
# # if age >=18:
# #     print("your can vote in the election ")
# # else : 
# #     print("You cant vote this year ")


# # Age finder 
# # dob= int(input("Enter your DOB:"))
# # age = 2023- dob
# # print (f'Your age is {age}')


# # num = int(input ("Enter any number"))
# # if num % 2 == 0:
# #     print("number is even")
# # else:
# #     print("Number is odd ")






# # logical operators 
# # and and or 
# # and - if both conditions are true then true else False
# # or - if any of the condition is true then true

# # age = int(input("Enter your age "))
# # if age >= 18:
# #     voter_id = input("DO you have voter id card , yes or no:-  ")
# # if age >= 18 and voter_id.lower() == "yes":
# #     print("you can vote in the election ")
# # elif age >= 18 and voter_id.lower() == "no":
# #     print ("Sorry you cant vote \n You dont have voter id, kindly apply for voter id ")
# # else:
# #     print("You cant vote as you are not 18 yet")



# # for loops

# # execute a block of code for each item in the sequence 
# # such as a list, tuple, string or range

# # lst = [1,2,3,4,5,6,7]
# # for i in lst:
# #     print (i)

# # for i in range (1,20):
# #     print(i)

# # a= ["shivam", "kumar","shahi"]

# # for i in a:
# #     print (i)

# # marks = {"English": 32, "Hindi": 50,"Maths":68}

# # for subject, mark in marks.items():
# #     print(subject, mark)


# # for subject in marks.keys():
# #     print(subject)

# # for mark in marks.values():
# #     print(mark)


# # range function in forloops

# # for i in range(100):
# #     print(i)



# # fizzbuss project

# the program should add number from 1 to a specified number in a list. 
# for multiples of 3 it should be "FIZZ"
# for multiples of 5 , it should be "buzz"
# for numbers numtiples of both 3 and 5 it should be "FIZZBUZZ"
# print the list 

# print("fizz Buzz program")
# till_num = int(input("Enter any specified number"))
# lst = []
# for num in range (1, till_num+1):
#     result = ""
#     if num % 3 == 0:
#         result = result +"Fizz"
#         if num % 5 == 0:
#          result = result +"Buzz"
#     elif num % 5 == 0:
#          result = result +"Buzz"
#     else:
#         result = num
#     lst.append(result)
# print(lst)



# while loop

# user_input = ""
# while user_input != "q":
#     user_input = input("Enter any number or q for quit:- ")
#     if user_input.isdigit():
#         if int(user_input) % 2 ==0:
#             print("The given number is even ")
#         else:
#             print("the given number id odd")
        
# BREAK - TO STOP THE LOOP 
# CONTINUE - TO STOP THE CURRENT ITERATION OF LOOP AND START NEXT ITERATION

# num = [1,2,3,4,5,6,95,48]
# for n in num:
#     if n == 6:
#         break
#     print(n)

# num = [1,2,3,4,5,6,95,48]
# for n in num:
#     if n == 6:
#         continue
#     print(n)

# num = [1,2,3,4,5,6,95,48]
# for n in num:
#     if n < 6:
#         continue
#     print(n)


# FUNCTION

def welcome(name,age=None):
    print("*"*20)
    print(f"welcome {name} to the world")
    print(f"Your age is {age}")
    print(f"thankyou {name} for signing in")
    print("*"*20)


welcome("shivam", 20)

welcome("shahi")


