#            1. Data Types

# 1.Find the data type of every value in a mixed list.

# my_list = [10,20,30,"Hello", "5j", "kanika", 70,True]

# for value in my_list:
#     print(value,":", type(value))


# 2.Convert a nested list into a tuple of tuples. 

# my_list = [[1,2,3],[4,5,6],[7,8,9]]

# result = tuple (tuple(i) for i in my_list) 
# print(result)


# 3. Remove all duplicate values from a mixed list while preserving the original order.

# my_list = [10, 20, "Hello", 50, 10, 45, "Sonu", True, 20 ,"Hello"]

# result = []

# for value in my_list:
#     if value not in result:
#         result.append(value)

# print(result)


#                   2. operators


# 4. Check whether a number is a power of 2 using operators.

# num = int(input("Enter the number:"))
# if num > 0 and (num & (num -  1)) == 0:
#     print("Power of 2 ")
# else:
#     print("Not Power of 2")    


#5. Swap two numbers using bitwise XOR. 

# a = 10 
# b = 20 

# print("Before swapping")
# print("a =", a)
# print("b =", b)
# a = a ^ b
# b = a ^ b
# a = a ^ b

# print("After swapping ")
# print("a =", a)
# print("b =", b)


# 6.Find whether a number is divisible by both 4 and 6 using logical operators.

# num = int(input ("Enter the number:"))

# if num % 4 == 0 and num % 6 == 0:
#     print("Divisible by  both 4 and 6 ")
# else:
#     print("not Divisible by both number 4 and 6")    


# 7.Calculate the total electricity bill using different unit rates.
# units = int(input("Enter electricity units: "))

# if units <= 100:
#     bill = units * 3

# elif units <= 200:
#     bill = (100 * 3) + (units - 100) * 5

# elif units <= 300:
#     bill = (100 * 3) + (100 * 5) + (units - 200) * 7

# else:
#     bill = (100 * 3) + (100 * 5) + (100 * 7) + (units - 300) * 10

# print("Total Electricity Bill = Rs.", bill)


#                   3. Conditional Statements

# 8. Check whether three sides can form a triangle. 

# a = int(input("Enter the first side:"))
# b = int(input("Enter the second side:"))
# c = int(input("Enter the third side:"))

# if a + b> c and a + c > b and b+ c > a:
#     print("Its is traingle")
# else:
#     print("Not traingale")    


#9. Determine the type of triangle (Equilateral, Isosceles, Scalene).

# a = int(input("Enter first side: "))
# b = int(input("Enter second side: "))
# c = int(input("Enter third side: "))

# if a + b > c and a + c > b and b + c > a:

#     if a == b == c:
#         print("Equilateral Triangle")

#     elif a == b or b == c or a == c:
#         print("Isosceles Triangle")

#     else:
#         print("Scalene Triangle")

# else:
#     print("Invalid Triangle")


#10. Create a simple ATM menu (Withdraw, Deposit, Balance). 
# balance = 5000

# while True:
#     print(" ATM MENU ")
#     print("1. Withdraw")
#     print("2. Deposit")
#     print("3. Balance")
#     print("4. Exit")

#     choice = int(input("Enter your choice: "))

#     if choice == 1:
#         amount = int(input("Enter withdraw amount: "))

#         if amount > 0 and amount <= balance:
#             balance = balance - amount
#             print("Withdrawal Successful")
#         else:
#             print("Insufficient Balance or Invalid Amount")

#     elif choice == 2:
#         amount = int(input("Enter deposit amount: "))

#         if amount > 0:
#             balance = balance + amount
#             print("Deposit Successful")
#         else:
#             print("Invalid Amount")

#     elif choice == 3:
#         print("Your Balance =", balance)

#     elif choice == 4:
#         print("Thank you for using ATM")
#         break

#     else:
#         print("Invalid Choice")



#11. Calculate income tax based on different tax slabs. 

# income = float(input("Enter your annual income: "))

# if income <= 250000:
#     tax = 0

# elif income <= 500000:
#     tax = (income - 250000) * 0.05

# elif income <= 1000000:
#     tax = (250000 * 0.05) + (income - 500000) * 0.20

# else:
#     tax = (250000 * 0.05) + (500000 * 0.20) + (income - 1000000) * 0.30

# print("Annual Income =", income)
# print("Total Income Tax =", tax)

#12. Create a menu-driven calculator using if-elif. 
# print("----- CALCULATOR -----")
# print("1. Addition")
# print("2. Subtraction")
# print("3. Multiplication")
# print("4. Division")

# choice = int(input("Enter your choice: "))

# a = float(input("Enter first number: "))
# b = float(input("Enter second number: "))

# if choice == 1:
#     print("Addition =", a + b)

# elif choice == 2:
#     print("Subtraction =", a - b)

# elif choice == 3:
#     print("Multiplication =", a * b)

# elif choice == 4:
#     if b != 0:
#         print("Division =", a / b)
#     else:
#         print("Cannot divide by zero")

# else:
#     print("Invalid Choice")


#                        4.loops

#13. Print all prime numbers between 1 and n.

# n = int(input("Enter the number:"))
# print("Prime numbers are:")

# for num in range(2, n + 1):
#     count = 0

#     for i in range(1, num + 1):
#         if num % i == 0:
#             count += 1

#     if count == 2:
#         print(num, end=" ")


# 14. Find the factorial of a number using a loop. 

# num = int(input("Enter the number:"))

# fact = 1
# if num < 0:
#     print("Not Factroial")

# else:
#     for i in range(1, num + 1):
#         fact = fact * i

#     print("Factorial =", fact)        



#15. Print the Fibonacci series up to n terms. 
# n = int(input("Enter the number of terms:"))

# a = 0 
# b = 1

# for i in range(n):
#     print(a, end=" ")

#     c = a + b
#     a = b
#     b = c


#16. Check whether a number is an Armstrong number. 
# num = int(input("Enter the numbers:"))
# temp = num
# power = len(str(num))
# total = 0

# while temp > 0:
#     digit = temp % 10
#     total = total + digit ** power
#     temp = temp // 10

# if num >= 0 and total == num:
#     print("Armstrong Number")
# else:
#     print("Not an Armstrong Number")


#17. Reverse a number and check if it is a palindrome. 

# num = int(input("enter the number:"))

# temp = num 
# reverse = 0
# while temp > 0:
#     digit = temp % 10
#     reverse = reverse * 10 + digit
#     temp = temp // 10
# print("Reverse number =", reverse)
# if num >= 0 and num == reverse:
#     print("Palindrome number") 
# else:
#     print("Not palindrome")       


# 18.Find the Greatest Common Divisor (GCD) of two numbers. 

# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))

# while b != 0:
#     a, b = b, a % b

# print("GCD =", abs(a))

#                         5.Function

#19.19. Write a function to check if a string is a palindrome. 

# def palindrome(text):
#     reverse = ""
#     for ch in text:
#         reverse = ch + reverse
#     if text == reverse:
#         print("Palindrome")
#     else:
#         print("Not palindrome")        
# text = input("Enter the string:")
# palindrome(text)        


# 20. Write a function to count vowels and consonants in a string. 

# def count_vowels_consonants(text):
#     vowels = 0
#     consonants = 0

#     for ch in text.lower():
#         if ch.isalpha():
#             if ch in "aeiou":
#                 vowels += 1
#             else:
#                 consonants += 1

#     print("Vowels =", vowels)
#     print("Consonants =", consonants)


# text = input("Enter a string: ")
# count_vowels_consonants(text)

#21. Create a function to calculate simple and compound interest. 
# def interest(p, r, t):
#     si = (p * r * t) / 100

#     ci = p * (1 + r / 100) ** t - p

#     print("Simple Interest =", si)
#     print("Compound Interest =", ci)


# p = float(input("Enter Principal Amount: "))
# r = float(input("Enter Rate of Interest: "))
# t = float(input("Enter Time in years: "))

# interest(p, r, t)


#22. Write a function to return all factors of a number. 
# def find_factors(num):
#     factors = []

#     for i in range(1, num + 1):
#         if num % i == 0:
#             factors.append(i)

#     return factors


# number = int(input("Enter a number: "))

# print("Factors =", find_factors(number))



#23. Write a function to find the second-largest number in a list. 
# def second_largest(numbers):
#     unique = []

#     for num in numbers:
#         if num not in unique:
#             unique.append(num)

#     if len(unique) < 2:
#         return "Second largest does not exist"

#     largest = unique[0]
#     second = unique[0]

#     for num in unique:
#         if num > largest:
#             second = largest
#             largest = num

#         elif num > second:
#             second = num

#     return second


# numbers = [10, 50, 20, 80, 40, 80]

# print("Second Largest =", second_largest(numbers))


#                             6.Lists 

#24. Merge two lists without duplicates.

# list1 = [1,2,3,4]
# list2 = [3,4,5,6]
# result = []
# for num in list1 + list2:
#     if num not in result:
#         result.append(num)

# print("Merged List =", result)



#25. Find the second-largest and second-smallest elements. 
# numbers = [10, 20, 5, 40, 30, 5]

# unique = []

# for num in numbers:
#     if num not in unique:
#         unique.append(num)

# unique.sort()

# if len(unique) >= 2:
#     print("Second Smallest =", unique[1])
#     print("Second Largest =", unique[-2])
# else:
#     print("Second largest and smallest do not exist")


#26. Rotate a list to the left by k positions.
# number = [1,2,3,4,5]
# k = 2
# k = k % len(number)
# rotated = number[k:] + number[:k]
# print("Roteted list =", rotated)

#27. Separate even and odd numbers into two lists. 

# numbers = [1,2,3,4,5,6,7,8]
# even = []
# odd = []
# for num in numbers:
#     if num % 2 == 0:
#         even.append(num)
#     else:
#         odd.append(num) 
# print("Even numbers =", even)
# print("Odd numbers =", odd)           


#28. Find the common elements between two lists.

# list1 = [1,2,3,4,5]
# list2 = [3,4,5,6,7]
# common = []
# for num in list1:
#     if num in list2 and num not in common:
#         common.append(num)
# print("Commom elements =", common)

#                               7. Tuples & Sets 

#29. Count the frequency of each element in a tuple.

# my_tuple = (1, 2, 3, 2, 4, 1, 2, 3)

# frequency = {}

# for num in my_tuple:
#     if num in frequency:
#         frequency[num] += 1
#     else:
#         frequency[num] = 1

# print("Frequency =", frequency)


#30. Find the union, intersection, and difference of two sets. 
# set1 = {1, 2, 3, 4, 5}
# set2 = {3, 4, 5, 6, 7}

# union = set1.union(set2)
# intersection = set1.intersection(set2)
# difference = set1.difference(set2)

# print("Union =", union)
# print("Intersection =", intersection)
# print("Difference =", difference)

#31. Check whether one set is a subset of another.
# set1 = {1,2,3}
# set2 = {1,2,3,4,5}
# if set1.issubset(set2):
#     print("Set1 is a subset of Set2")
# else:
#     print("Set1 is not a subset of Set2")

#                               8. Dictionaries

#32. Count the frequency of words in a sentence. 
# sentence = "python is easy and python is powerful"

# words = sentence.split()

# frequency = {}

# for word in words:
#     if word in frequency:
#         frequency[word] += 1
#     else:
#         frequency[word] = 1

# print("Word Frequency =", frequency)


#33. Create a dictionary from two lists (keys and values). 

# keys = ["name", "age", "city"]
# values = ["Soundarya", 22, "Pune"]

# my_dict = {}

# for i in range(len(keys)):
#     my_dict[keys[i]] = values[i]

# print("Dictionary =", my_dict)    


#34. Sort a dictionary by its values.
# my_dict = {
#     "Apple": 50,
#     "Banana": 20,
#     "Mango": 40,
#     "Orange": 30
# }

# sorted_dict = dict(sorted(my_dict.items(), key=lambda item: item[1]))

# print("Sorted Dictionary =", sorted_dict)

#                            9. File Handling
#35. Read a text file and count the number of lines, words, and characters.
# with open("sample.txt", "r") as file:
#     data = file.read()

# lines = data.splitlines()
# words = data.split()
# characters = len(data)

# print("Number of Lines =", len(lines))
# print("Number of Words =", len(words))
# print("Number of Characters =", characters)

#36. Copy only the even-numbered lines from one file to another.
# with open("input.txt", "r") as file:
#     lines = file.readlines()

# with open("output.txt", "w") as file:
#     for i in range(1, len(lines), 2):
#         file.write(lines[i])

# print("Even-numbered lines copied successfully!")


#                    10. Exception Handling

#37. Handle invalid integer input using try-except.

# try:
#     num = int(input("Enter an integer: "))
#     print("Number =", num)

# except ValueError:
#     print("Invalid input! Please enter an integer.")

#38. Handle file-not-found errors while reading a file.
# try:
#     with open("sample.txt", "r") as file:
#         data = file.read()
#         print(data)

# except FileNotFoundError:
#      print("Error: File not found!")

#                           11. Modules

#39. Create a random password generator using the random and string modules. 
# import random
# import string

# length = int(input("Enter password length: "))

# characters = string.ascii_letters + string.digits + string.punctuation

# password = ""

# for i in range(length):
#     password += random.choice(characters)

# print("Generated Password =", password)



#40. Use the datetime module to calculate the number of days between two dates.

from datetime import datetime

date1 = input("Enter first date (DD-MM-YYYY): ")
date2 = input("Enter second date (DD-MM-YYYY): ")

d1 = datetime.strptime(date1, "%d-%m-%Y")
d2 = datetime.strptime(date2, "%d-%m-%Y")

difference = abs((d2 - d1).days)

print("Number of Days =", difference)