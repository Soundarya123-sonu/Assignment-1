#Write a Python program to reverse a number without converting it into a string.

# num = int(input("Enter a number: "))
# reverse = 0

# while num > 0:
#     digit = num % 10
#     reverse = reverse * 10 + digit
#     num = num // 10

# print("Reversed number:", reverse)

#2. Write a program to check whether a number is a palindrome.

# num = int(input("Enter a number: "))

# original = num
# reverse = 0

# while num > 0:
#     digit = num % 10
#     reverse = reverse * 10 + digit
#     num = num // 10

# if original == reverse:
#     print("Palindrome Number")
# else:
#     print("Not a Palindrome Number")

#3. Write a program to check whether a number is an Armstrong number.

# num = int(input("Enter a number: "))

# original = num
# digits = len(str(num))
# sum = 0

# while num > 0:
#     digit = num % 10
#     sum = sum + digit ** digits
#     num = num // 10

# if original == sum:
#     print("Armstrong Number")
# else:
#     print("Not an Armstrong Number")

#4. Write a program to find the factorial of a number using a loop.

# num = int(input("Enter a number: "))

# fact = 1

# if num < 0:
#     print("Factorial is not possible for negative numbers")
# else:
#     for i in range(1, num + 1):
#         fact = fact * i

#     print("Factorial =", fact)

#5. Write a program to generate the Fibonacci series up to N terms.

# n = int(input("Enter the number of terms: "))

# a = 0
# b = 1

# print("Fibonacci Series:")

# for i in range(n):
#     print(a, end=" ")

#     c = a + b
#     a = b
#     b = c


#6. Write a program to check whether a number is prime.

# num = int(input("Enter a number: "))

# if num <= 1:
#     print("Not a Prime Number")
# else:
#     for i in range(2, num):
#         if num % i == 0:
#             print("Not a Prime Number")
#             break
#     else:
#         print("Prime Number")

#7. Write a program to print all prime numbers between 1 and 100.

# for num in range(2, 101):
#     for i in range(2, num):
#         if num % i == 0:
#             break
#     else:
#         print(num, end=" ")


#8. Write a program to find the GCD and LCM of two numbers.

# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))

# x = a
# y = b

# while b != 0:
#     temp = b
#     b = a % b
#     a = temp

# gcd = a
# lcm = (x * y) // gcd

# print("GCD =", gcd)
# print("LCM =", lcm)

#9. Write a program to reverse a string without using slicing.

# text = input("Enter a string: ")

# reverse = ""

# for ch in text:
#     reverse = ch + reverse

# print("Reversed String:", reverse)


#10. Write a program to check whether a string is a palindrome.


# text = input("Enter a string: ")

# reverse = ""

# for ch in text:
#     reverse = ch + reverse

# if text == reverse:
#     print("Palindrome String")
# else:
#     print("Not a Palindrome String")


#11. Write a program to count vowels, consonants, digits and special characters in a string.


# text = input("Enter a string: ")

# vowels = 0
# consonants = 0
# digits = 0
# special = 0

# for ch in text:
#     if ch.isalpha():
#         if ch.lower() in "aeiou":
#             vowels += 1
#         else:
#             consonants += 1

#     elif ch.isdigit():
#         digits += 1

#     else:
#         special += 1

# print("Vowels:", vowels)
# print("Consonants:", consonants)
# print("Digits:", digits)
# print("Special Characters:", special)

#12. Write a program to find the frequency of each character in a string.

# text = input("Enter a string: ")

# freq = {}

# for ch in text:
#     if ch in freq:
#         freq[ch] += 1
#     else:
#         freq[ch] = 1

# print("Character Frequency:")

# for ch, count in freq.items():
#     print(ch, "=", count)

#13. Write a program to find the first non-repeating character in a string.


# text = input("Enter a string: ")

# freq = {}

# for ch in text:
#     if ch in freq:
#         freq[ch] += 1
#     else:
#         freq[ch] = 1

# for ch in text:
#     if freq[ch] == 1:
#         print("First non-repeating character:", ch)
#         break
# else:
#     print("No non-repeating character found")

#14. Write a program to remove duplicate characters from a string.

# text = input("Enter a string: ")

# result = ""

# for ch in text:
#     if ch not in result:
#         result = result + ch

# print("String after removing duplicates:", result)

#15. Write a program to check whether two strings are anagrams.

# str1 = input("Enter first string: ")
# str2 = input("Enter second string: ")

# if sorted(str1) == sorted(str2):
#     print("Anagram Strings")
# else:
#     print("Not Anagram Strings")

#16. Write a program to find the longest word in a sentence.

# sentence = input("Enter a sentence: ")

# words = sentence.split()

# longest = ""

# for word in words:
#     if len(word) > len(longest):
#         longest = word

# print("Longest word:", longest)
# print("Length:", len(longest))


#17. Find the second-largest element in a list without using sort().

# numbers = [10, 20, 5, 40, 30]

# largest = second = float('-inf')

# for num in numbers:
#     if num > largest:
#         second = largest
#         largest = num
#     elif num > second and num != largest:
#         second = num

# if second == float('-inf'):
#     print("Second largest element does not exist")
# else:
#     print("Second largest element:", second)


#18. Remove duplicate elements from a list without using set().

# numbers = [10, 20, 10, 30, 20, 40, 50]

# result = []

# for num in numbers:
#     if num not in result:
#         result.append(num)

# print("Original List:", numbers)
# print("List after removing duplicates:", result)

#19. Find the common elements between two lists.

# list1 = [10, 20, 30, 40, 50]
# list2 = [30, 40, 50, 60, 70]

# common = []

# for num in list1:
#     if num in list2:
#         if num not in common:
#             common.append(num)

# print("Common Elements:", common)

#20. Move all zeros to the end of a list without changing the order of other elements.

# numbers = [0, 1, 0, 3, 12, 0, 5]

# result = []

# for num in numbers:
#     if num != 0:
#         result.append(num)

# zeros = numbers.count(0)

# for i in range(zeros):
#     result.append(0)

# print("Original List:", numbers)
# print("Updated List:", result)

#21. Find the missing number in a list containing numbers from 1 to N.

# numbers = [1, 2, 4, 5, 6]

# n = 6

# for i in range(1, n + 1):
#     if i not in numbers:
#         print("Missing Number:", i)

#22. Find the maximum difference between two elements where the larger element appears after the smaller element.

# numbers = [2, 3, 10, 6, 4, 8, 1]

# max_diff = -1

# for i in range(len(numbers)):
#     for j in range(i + 1, len(numbers)):
#         diff = numbers[j] - numbers[i]

#         if diff > max_diff:
#             max_diff = diff

# print("Maximum Difference:", max_diff)

#23. Rotate a list to the right by K positions.

# numbers = [1, 2, 3, 4, 5]

# k = 2

# n = len(numbers)

# k = k % n

# result = []

# for i in range(n - k, n):
#     result.append(numbers[i])

# for i in range(0, n - k):
#     result.append(numbers[i])

# print("Original List:", numbers)
# print("Rotated List:", result)


#24. Find all pairs in a list whose sum equals a given target.

# numbers = [2, 4, 3, 5, 7, 8, 1]

# target = 9

# print("Pairs are:")

# for i in range(len(numbers)):
#     for j in range(i + 1, len(numbers)):
#         if numbers[i] + numbers[j] == target:
#             print(numbers[i], numbers[j])

#25. Write a program to count the frequency of each word in a paragraph.

# text = input("Enter a paragraph: ")

# words = text.lower().split()

# freq = {}

# for word in words:
#     if word in freq:
#         freq[word] += 1
#     else:
#         freq[word] = 1

# print("Word Frequency:")

# for word, count in freq.items():
#     print(word, "=", count)

#26. Write a program to merge two dictionaries. If a key exists in both, add their values.


# dict1 = {'a': 10, 'b': 20, 'c': 30}
# dict2 = {'b': 5, 'c': 15, 'd': 40}

# result = {}

# # Add values from first dictionary
# for key in dict1:
#     result[key] = dict1[key]

# # Merge second dictionary
# for key in dict2:
#     if key in result:
#         result[key] += dict2[key]
#     else:
#         result[key] = dict2[key]

# print("Merged Dictionary:", result)


#27. Write a program to sort a dictionary based on its values.


# Sort dictionary based on values

# my_dict = {'a': 50, 'b': 20, 'c': 40, 'd': 10}

# # Sort in ascending order
# sorted_dict = dict(sorted(my_dict.items(), key=lambda x: x[1]))

# print("Original Dictionary:", my_dict)
# print("Sorted Dictionary:", sorted_dict)

#28. Given a list of student dictionaries containing name and marks, find the student with the highest marks.

# List of student dictionaries

# students = [
#     {"name": "Rahul", "marks": 85},
#     {"name": "Priya", "marks": 95},
#     {"name": "Amit", "marks": 78},
#     {"name": "Sneha", "marks": 90}
# ]

# # Find student with highest marks
# top_student = max(students, key=lambda x: x["marks"])

# print("Student with Highest Marks:")
# print("Name:", top_student["name"])
# print("Marks:", top_student["marks"])


#29. Group words from a list based on their first character using a dictionary.


# words = ["apple", "ant", "banana", "ball", "cat", "car", "dog"]

# # Create an empty dictionary
# grouped_words = {}

# # Group words based on first character
# for word in words:
#     first_char = word[0]

#     if first_char not in grouped_words:
#         grouped_words[first_char] = []

#     grouped_words[first_char].append(word)

# # Display the result
# print("Grouped Words:", grouped_words)

#30. Convert two lists into a dictionary, where the first list contains keys and the second contains values.


# keys = ["name", "age", "city", "course"]
# values = ["Rahul", 22, "Pune", "Python"]


# my_dict = dict(zip(keys, values))

# print("Dictionary:", my_dict)

#31. Write a recursive function to calculate the factorial of a number.

# def factorial(n):
#     if n == 0 or n == 1:
#         return 1
#     else:
#         return n * factorial(n - 1)

# # Input from user
# num = int(input("Enter a number: "))


# if num < 0:
#     print("Factorial is not defined for negative numbers")
# else:
#     print("Factorial of", num, "is", factorial(num))


#32. Write a recursive function to find the sum of digits of a number.

# Recursive function to find sum of digits

# def sum_digits(n):
#     if n == 0:
#         return 0
#     else:
#         return (n % 10) + sum_digits(n // 10)

# # Input from user
# num = int(input("Enter a number: "))

# # Display result
# num = abs(num)
# print("Sum of digits:", sum_digits(num))


#33. Implement your own map() function without using Python's built-in map().

# def my_map(function, iterable):
#     result = []

#     for item in iterable:
#         result.append(function(item))

#     return result

# def square(n):
#     return n * n

# numbers = [1, 2, 3, 4, 5]

# output = my_map(square, numbers)

# print("Original List:", numbers)
# print("Squared List:", output)


#34. Implement a function that accepts a list and returns a new list containing only even numbers.

# def get_even_numbers(numbers):
#     even_list = []

#     for num in numbers:
#         if num % 2 == 0:
#             even_list.append(num)

#     return even_list
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# result = get_even_numbers(numbers)

# print("Original List:", numbers)
# print("Even Numbers:", result)


#35. Write a function to flatten a nested list.

# def flatten_list(nested_list):
#     result = []

#     for item in nested_list:
#         if isinstance(item, list):
#             result.extend(flatten_list(item))
#         else:
#             result.append(item)

#     return result

# my_list = [1, [2, 3], [4, [5, 6]], 7]

# output = flatten_list(my_list)

# print("Original List:", my_list)
# print("Flattened List:", output)

#36. Student Management System

# students = []

# def add_student():
#     name = input("Enter student name: ")
#     roll_no = int(input("Enter roll number: "))
#     marks = float(input("Enter marks: "))

#     student = {
#         "name": name,
#         "roll_no": roll_no,
#         "marks": marks
#     }

#     students.append(student)
#     print("Student added successfully!")

# def display_students():
#     if not students:
#         print("No student records found.")
#     else:
#         print("\nStudent Records:")
#         for student in students:
#             print(student)

# def search_student():
#     roll_no = int(input("Enter roll number to search: "))

#     for student in students:
#         if student["roll_no"] == roll_no:
#             print("Student Found:", student)
#             return

#     print("Student not found.")

# def update_student():
#     roll_no = int(input("Enter roll number to update: "))

#     for student in students:
#         if student["roll_no"] == roll_no:
#             student["name"] = input("Enter new name: ")
#             student["marks"] = float(input("Enter new marks: "))
#             print("Student updated successfully!")
#             return

#     print("Student not found.")

# def delete_student():
#     roll_no = int(input("Enter roll number to delete: "))

#     for student in students:
#         if student["roll_no"] == roll_no:
#             students.remove(student)
#             print("Student deleted successfully!")
#             return

#     print("Student not found.")

# while True:
#     print("\n===== STUDENT MANAGEMENT SYSTEM =====")
#     print("1. Add Student")
#     print("2. Display Students")
#     print("3. Search Student")
#     print("4. Update Student")
#     print("5. Delete Student")
#     print("6. Exit")

#     choice = input("Enter your choice: ")

#     if choice == "1":
#         add_student()
#     elif choice == "2":
#         display_students()
#     elif choice == "3":
#         search_student()
#     elif choice == "4":
#         update_student()
#     elif choice == "5":
#         delete_student()
#     elif choice == "6":
#         print("Thank you for using Student Management System!")
#         break
#     else:
#         print("Invalid choice! Please try again.")


#37. Bank Account Management

#Create a bank account program with:
#Create account
# Deposit money
# Withdraw money
# Check balance
# Display account details


# account = {}

# def create_account():
#     name = input("Enter account holder name: ")
#     account_no = input("Enter account number: ")
#     balance = float(input("Enter initial deposit: "))

#     if balance < 0:
#         print("Initial deposit cannot be negative!")
#         return

#     account["name"] = name
#     account["account_no"] = account_no
#     account["balance"] = balance

#     print("Account created successfully!")

# def deposit_money():
#     if not account:
#         print("Please create an account first!")
#         return

#     amount = float(input("Enter deposit amount: "))

#     if amount > 0:
#         account["balance"] += amount
#         print("Money deposited successfully!")
#     else:
#         print("Invalid deposit amount!")

# def withdraw_money():
#     if not account:
#         print("Please create an account first!")
#         return

#     amount = float(input("Enter withdrawal amount: "))

#     if amount <= 0:
#         print("Invalid withdrawal amount!")
#     elif amount <= account["balance"]:
#         account["balance"] -= amount
#         print("Money withdrawn successfully!")
#     else:
#         print("Insufficient balance!")

# def check_balance():
#     if not account:
#         print("Please create an account first!")
#     else:
#         print("Current Balance:", account["balance"])

# def display_details():
#     if not account:
#         print("Please create an account first!")
#     else:
#         print("\nAccount Details:")
#         print("Account Holder:", account["name"])
#         print("Account Number:", account["account_no"])
#         print("Balance:", account["balance"])


# while True:
#     print("\n===== BANK ACCOUNT MANAGEMENT =====")
#     print("1. Create Account")
#     print("2. Deposit Money")
#     print("3. Withdraw Money")
#     print("4. Check Balance")
#     print("5. Display Account Details")
#     print("6. Exit")

#     choice = input("Enter your choice: ")

#     if choice == "1":
#         if account:
#             print("Account already exists!")
#         else:
#             create_account()

#     elif choice == "2":
#         deposit_money()

#     elif choice == "3":
#         withdraw_money()

#     elif choice == "4":
#         check_balance()

#     elif choice == "5":
#         display_details()

#     elif choice == "6":
#         print("Thank you for using our banking system!")
#         break

#     else:
#         print("Invalid choice! Please try again.")


#38. Employee Salary Management

#Create a program to:
# Add employee details
# Calculate gross salary
# Calculate deductions
# Calculate net salary
# Display employee salary details

# employees = []

# def add_employee():
#     name = input("Enter employee name: ")
#     emp_id = input("Enter employee ID: ")
#     basic_salary = float(input("Enter basic salary: "))
#     hra = float(input("Enter HRA: "))
#     da = float(input("Enter DA: "))
#     deductions = float(input("Enter total deductions: "))

#     gross_salary = basic_salary + hra + da
#     net_salary = gross_salary - deductions

#     employee = {
#         "name": name,
#         "emp_id": emp_id,
#         "basic_salary": basic_salary,
#         "hra": hra,
#         "da": da,
#         "gross_salary": gross_salary,
#         "deductions": deductions,
#         "net_salary": net_salary
#     }

#     employees.append(employee)
#     print("Employee added successfully!")

# def display_employees():
#     if not employees:
#         print("No employee records found!")
#     else:
#         print("\n===== EMPLOYEE SALARY DETAILS =====")

#         for emp in employees:
#             print("\nEmployee Name:", emp["name"])
#             print("Employee ID:", emp["emp_id"])
#             print("Basic Salary:", emp["basic_salary"])
#             print("HRA:", emp["hra"])
#             print("DA:", emp["da"])
#             print("Gross Salary:", emp["gross_salary"])
#             print("Deductions:", emp["deductions"])
#             print("Net Salary:", emp["net_salary"])

# # Main Menu
# while True:
#     print("\n===== EMPLOYEE SALARY MANAGEMENT =====")
#     print("1. Add Employee")
#     print("2. Display Employee Salary Details")
#     print("3. Exit")

#     choice = input("Enter your choice: ")

#     if choice == "1":
#         add_employee()

#     elif choice == "2":
#         display_employees()

#     elif choice == "3":
#         print("Thank you!")
#         break

#     else:
#         print("Invalid choice! Please try again.")



#39. Library Management System

#Create a program to:
# Add books
# Display available books
# Issue a book
# Return a book
# Search books by title

# books = []

# def add_book():
#     title = input("Enter book title: ")
#     author = input("Enter author name: ")

#     book = {
#         "title": title,
#         "author": author,
#         "status": "Available"
#     }

#     books.append(book)
#     print("Book added successfully!")

# def display_books():
#     if not books:
#         print("No books available in library!")
#     else:
#         print("\n===== BOOK LIST =====")
#         for book in books:
#             print("Title:", book["title"])
#             print("Author:", book["author"])
#             print("Status:", book["status"])
#             print("--------------------")

# def issue_book():
#     title = input("Enter book title to issue: ")

#     for book in books:
#         if book["title"].lower() == title.lower():
#             if book["status"] == "Available":
#                 book["status"] = "Issued"
#                 print("Book issued successfully!")
#             else:
#                 print("Book is already issued!")
#             return

#     print("Book not found!")

# def return_book():
#     title = input("Enter book title to return: ")

#     for book in books:
#         if book["title"].lower() == title.lower():
#             if book["status"] == "Issued":
#                 book["status"] = "Available"
#                 print("Book returned successfully!")
#             else:
#                 print("Book is already available!")
#             return

#     print("Book not found!")

# def search_book():
#     title = input("Enter book title to search: ")

#     for book in books:
#         if title.lower() in book["title"].lower():
#             print("\nBook Found!")
#             print("Title:", book["title"])
#             print("Author:", book["author"])
#             print("Status:", book["status"])
#             return

#     print("Book not found!")

# while True:
#     print("\n===== LIBRARY MANAGEMENT SYSTEM =====")
#     print("1. Add Book")
#     print("2. Display Available Books")
#     print("3. Issue Book")
#     print("4. Return Book")
#     print("5. Search Book")
#     print("6. Exit")

#     choice = input("Enter your choice: ")

#     if choice == "1":
#         add_book()

#     elif choice == "2":
#         display_books()

#     elif choice == "3":
#         issue_book()

#     elif choice == "4":
#         return_book()

#     elif choice == "5":
#         search_book()

#     elif choice == "6":
#         print("Thank you for using Library Management System!")
#         break

#     else:
#         print("Invalid choice! Please try again.")

#40. Task Management Application

#Create a console-based task manager with:
# Add task
# View all tasks
# Update task
# Delete task
# Mark task as completed
# Filter completed and pending tasks


# Task Management Application

tasks = []

def add_task():
    task_name = input("Enter task name: ")

    task = {
        "name": task_name,
        "status": "Pending"
    }

    tasks.append(task)
    print("Task added successfully!")

def view_tasks():
    if not tasks:
        print("No tasks available!")
    else:
        print("\n===== ALL TASKS =====")

        for i, task in enumerate(tasks, start=1):
            print(i, ".", task["name"],
                  "-", task["status"])

def update_task():
    view_tasks()

    if not tasks:
        return

    task_no = int(input("Enter task number to update: "))

    if 1 <= task_no <= len(tasks):
        new_name = input("Enter new task name: ")
        tasks[task_no - 1]["name"] = new_name
        print("Task updated successfully!")
    else:
        print("Invalid task number!")

def delete_task():
    view_tasks()

    if not tasks:
        return

    task_no = int(input("Enter task number to delete: "))

    if 1 <= task_no <= len(tasks):
        tasks.pop(task_no - 1)
        print("Task deleted successfully!")
    else:
        print("Invalid task number!")

def complete_task():
    view_tasks()

    if not tasks:
        return

    task_no = int(input("Enter task number to complete: "))

    if 1 <= task_no <= len(tasks):
        tasks[task_no - 1]["status"] = "Completed"
        print("Task marked as completed!")
    else:
        print("Invalid task number!")

def filter_tasks():
    print("\n1. Completed Tasks")
    print("2. Pending Tasks")

    choice = input("Enter your choice: ")

    if choice == "1":
        status = "Completed"
    elif choice == "2":
        status = "Pending"
    else:
        print("Invalid choice!")
        return

    found = False

    print("\n===== FILTERED TASKS =====")

    for i, task in enumerate(tasks, start=1):
        if task["status"] == status:
            print(i, ".", task["name"])
            found = True

    if not found:
        print("No", status, "tasks found!")

# Main Menu
while True:
    print("\n===== TASK MANAGEMENT SYSTEM =====")
    print("1. Add Task")
    print("2. View All Tasks")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Mark Task as Completed")
    print("6. Filter Tasks")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_task()

    elif choice == "2":
        view_tasks()

    elif choice == "3":
        update_task()

    elif choice == "4":
        delete_task()

    elif choice == "5":
        complete_task()

    elif choice == "6":
        filter_tasks()

    elif choice == "7":
        print("Thank you for using Task Manager!")
        break

    else:
        print("Invalid choice! Please try again.")
