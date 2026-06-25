import random


# def get_age():
#     while True:
#         try: 
#             age = random.randint(1, 100)
#             # age = int(input("Enter the age: "))
#             if age >= 18:
#                 # print("you can vote")
#                 return age
#             else:
#                 print("TOO young to vote")
            
#         except ValueError:
#             print("Invalid input!")

# user_age = get_age()
# print(f"Age entered: {user_age}")

#swap a input numbers

# num1 = int(input("Enter a num1: "))
# num2 = int(input("Enter the second num2: "))

# temp = num1
# num1 = num2
# num2 = temp

# print(num1, num2)

#Write a program that will give you the sum of 3 digits
# s= 0
# t = 10
# w = 12

# k = s+t+w
# print(k)

# Write a program that will reverse a four digit number.Also it checks whether the reverse is true.

def rev_num():
    digit = int(input("Enter a four digit number: "))
    try:
        if len(str(digit)) > 4:
            return "invalid"
        else:
            for char in str(digit):
                
        
            