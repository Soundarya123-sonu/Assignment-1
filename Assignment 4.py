#1. Check whether a number is even or odd

# num = int(input("Enter the number:"))
# if num % 2 == 0:
#     print("Even number")
# else:
#     print("Odd number")    

# 2.Write a program to find the largest of three numbers.

# a = int (input("Enter the 1st number:"))
# b = int(input("Enter the 2nd number:"))
# c = int(input("Enter the 3rd number:"))
# if a >= b and a >= c:
#     print("Largest first number")
# elif b >= a and b >= c:
#     print("Largest second number")   
# else:
#     print("Largest third numbers") 

# 3.Write a program to check whether a given number is prime.

# num = int(input("Enter the number:"))

# if num <= 1:
#     print("Not a prime number")
# else:
#     for i in range(2, num):
#         if num % i == 0:
#             print("Not a Prime Number")
#             break
#     else:
#         print("Prime Number")    


#4.Write a program to print the Fibonacci series up to n terms.

# num = int(input("Enter the number of  terms:"))
# a = 0
# b = 1
# for i in range(num):
#     print(a,end="")
#     a , b = b,a + b


# 5.Write a program to find the factorial of a number using a loop.

# num = int(input("Enter the number:"))

# fact = 1
# if num < 0:
#     print("Factrial is not in defined")
# else:
#     for i in range(1, num+1):
#         fact = fact* i

#     print("factroial =", fact)    

# 6.Write a program to reverse a string without using [::-1].

# text = input("Enter the string:")

# reverse = ""
# for ch in text:
#     reverse = ch + reverse

# print("Reverse =", reverse)    


# 7.Write a program to check whether a string is a palindrome.

# text = input("Enter the string:")
# reverse = ""
# for ch in text:
#     reverse = ch + reverse
# if text == reverse:
#     print("Palindrome")
# else:
#     print('Not palindrome ')        


# 8.Write a program to count the number of vowels and consonants in a string.

# text = input("Enter the string:")
# vowls = 0
# consatnts = 0
# for ch in text.lower():
#     if ch.isalpha():
#         if ch in "aeiou":
#             vowls += 1
#         else:
#             consatnts += 1 
# print("Vowels =", vowls)
# print("Constants =", consatnts)               


# 9.Write a program to find the sum of all elements in a list.

# numbers = [10,20,30,40,50]
# total = 0
# for num in numbers:
#     total = total + num
# print("Sum =", total)   


# 10.Write a program to find the largest and smallest element in a list without using max() or min().


# number = [10, 20, 5 , 30 , 45]
# largest = number [0]
# smallest = number[0]
# for num in number:
#     if num > largest:
#         largest = num
#     if num < smallest:
#         smallest = num
# print("Largesst =", largest)
# print("Smallest =", smallest)            


# 11.Write a program to remove duplicate elements from a list.

# numbers = [10, 20, 30, 10, 5, 40, 20, 4, 9, 5]

# result = []
# for num in numbers:
#     if num not in result:
#         result.append(num)
# print("List without duplicates:", result)        


# 12.Write a program to count how many times each element appears in a list using a dictionary.

# numbers = [10, 20, 10, 30, 20, 10, 40]

# count = {}

# for num in numbers:
#     if num in count:
#         count[num] += 1
#     else:
#         count[num] = 1

# print(count)


# 13.Write a program to find the second-largest number in a list.

# numbers = [10, 50, 20, 80, 40, 80]
# unique = []
# for num in numbers:
#     unique.append(num)

# if len(unique)< 2:
#     print("Second largets does not exist")
# else:
#     largest = unique[0]
#     second = unique[0]
#     for num in unique:
#         if num > largest:
#             second = largest
#             largest = num
#         elif num > second:
#             second = num
#     print("Second Largest =", second)            



# 14.Write a program to sort a list without using sort() or sorted().

# numbers = [20, 30, 3, 10, 8, 50]
# n = len(numbers)
# for i in range(n):
#     for j in range(0, n- i - 1):
#         if numbers[j] > numbers[j + 1]:
#             numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

# print("Sorted List:", numbers) 


# 15.Write a function that accepts a list of numbers and returns a list containing only the even numbers
# def even_numbers(numbers):
#     result = []
#     for num in numbers:
#         if num % 2== 0:
#             result.append(num)
#     return result
# numbers = [10, 15, 20, 25, 30, 35, 40]
# print("Even numbers :", even_numbers(numbers))        


#16.Write a program to find the frequency of each character in a string.

# text = input("Enter the text:")
# frequency = {}
# for ch in text:
#     if ch in frequency:
#         frequency [ch] += 1
#     else:
#         frequency [ch] = 1

# print("Character frequncy:", frequency)      


#17. Write a program to check whether two strings are anagrams of each other
# str1 = input("Enter first string:")
# str2 = input("Enter second string:")
# str1 = str1.replace(" ", "").lower()
# str2 = str2.replace(" ", "").lower()

# if sorted(str1) == sorted(str2):
#     print("Strings are Anagrams")
# else:
#     print("Strings are Not Anagrams")


#18.Write a program to find all duplicate values in a list.

# numbers = [10,20,30,40,10, 50, 60]
# duplicates = []
# for num in numbers:
#     if numbers.count(num) > 1 and num not in duplicates:
#         duplicates.append(num)

# print("Duplicate Values:", duplicates)

#19.Write a program that takes a sentence and finds the longest word.
# sentence = input("Enter the sentence:")
# words = sentence.split()
# longest = ""
# for word in words:
#     if len(word) > len(longest):
#         longest = word

# print("Longest Word:", longest)

#Create a simple student marks program that:
#accepts marks for 5 subjects,
#calculates the total and percentage,
#assigns a grade,and displays whether the student passed or failed.

marks = []

for i in range(1, 6):
    mark = int(input("Enter marks for subject " + str(i) + ": "))
    marks.append(mark)

total = sum(marks)
percentage = total / 5

print("\nTotal Marks =", total)
print("Percentage =", percentage, "%")

if any(mark < 35 or mark > 100 for mark in marks):
    print("Result: Fail")
    print("Grade: F")

elif percentage >= 90:
    print("Grade: A+")
    print("Result: Pass")

elif percentage >= 75:
    print("Grade: A")
    print("Result: Pass")

elif percentage >= 60:
    print("Grade: B")
    print("Result: Pass")

elif percentage >= 50:
    print("Grade: C")
    print("Result: Pass")

else:
    print("Grade: D")
    print("Result: Pass")
