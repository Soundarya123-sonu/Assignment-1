#1)Check if a number is positive, negative, or zero.

'''number = int(input("Enter the number:"))

if number > 0:
    print("The number is positive")
elif number < 0:
    print("The number is negative")
else:
    print("The number is zero")'''        

#2)Check whether a number is even or odd.

'''num = int(input("Enter the number:"))

if num % 2 == 0:
    print("The even number")
else:
    print("The odd number")'''

#3)Find the greater of two numbers.

'''num1 = int(input("Enter the 1st number:"))
num2 = int(input("Enter the 2nd number:"))

if num1 > num2:
    print("The 1st number is greater")
else:
    print("The 2nd number is greater")'''


#4)Find the greatest of three numbers.

'''num1 = int(input("Enter thr 1st number:"))
num2 = int(input("Enter the 2nd number:"))
num3 = int(input("Enter the 3rd number:"))

if num1 > num2 and num1 > num3:
    print("The 1st number is greater")
elif num2 > num1 and num2 > num3:
    print("The 2nd number is greater")
else:
    print("The 3rd number is greater")'''

#5)Check if a person is eligible to vote (age ≥ 18).

'''number = int(input("Enter the number:"))

if number >= 18:
    print("You are eligible")
else:
    print("Your are not eligible")'''

#6)Check whether a year is a leap year.

'''num = int(input("Enter the year:"))

if num % 4 == 0:
    print("The leap year")
else:
    print("No leap year")'''

#7)Check if a character is a vowel or consonant.

'''ch = input("Enter the character:")

if ch in "aeiou AEIOU":
    print("The charchter is vowel")
else:
    print("The charchter is constant")'''


#8)Check whether a number is divisible by 5 and 11.

'''num = int(input("Enter  the number:"))

if num % 5 == 0 and num % 11 == 0:
    print("The number is divisible by both 5 and 11 ")
else:
    print("The number is not divisible by both 5 and 11")'''


#9)Check if a number is a multiple of both 3 and 7.

'''num = int(input("Enter the number:"))

if num % 3 == 0 and num % 7 == 0:
    print(" Multiply the both number 3 and 7")
else:
    print("Not multiply the both number 3 and 7 ")'''


#10)Assign grades based on marks:
#90–100: A
#80–89: B
#70–79: C
#60–69: D
#Below 60: F


'''marks = int(input("Enter the marks:"))

if marks == 90:
    print("Grade A")
elif marks == 80:
    print("Grade B")
elif marks == 70:
    print("Grade C")
elif marks == 60:
    print("Grade D")
else:
    print("you are fail")'''


#11)Check if a character is uppercase or lowercase.

'''ch = input("Enter the character:")

if ch.isupper():
    print("Upper letter")
elif ch.islower():
    print("Lower letter")
else:
    print("Not Alphabet")'''


#12)Find whether the entered alphabet is a vowel using if-elif.

'''ch = input("Enter the character:")

if ch == "a":
    print("Vowel")
elif ch == "e":
    print("vowel")
elif ch == "i":
    print("vowel")
elif ch == "o":
    print("Vowel")
elif ch == "u":
    print("Vowel")
else:
    print("Constant")'''


#13 Check if three sides can form a triangle.

'''a = int(input("Enter the first side:"))
b = int(input("Enter the second side:"))
c = int(input("Enter thr third side:"))

if a + b > c and a + c > b and b + c > a:
    print("Triangle can be formed") 
else:
    print("Triangle not be formed")'''


#14 Determine the type of triangle (Equilateral, Isosceles, Scalene).    

'''a = int(input("Enter first side: "))
b = int(input("Enter second side: "))
c = int(input("Enter third side: "))

if a == b == c:
    print("Equilateral Triangle")
elif a == b or b == c or a == c:
    print("Isosceles Triangle")
else:
    print("Scalene Triangle")'''

#15Find the largest among four numbers.

'''a = int(input("Enter the first number:"))
b = int(input("Enter the second number:"))
c = int(input("Enter the third number:"))
d = int(input("Enter the fourth number:"))

if a >= b and a >= c and a >= d:
    print("Largest number is", a)
elif b >= a and b >= c and b >= d:
    print("Largest number is", b)
elif c >= a and c >= b and c >= d:
    print("Largest number is", c)
else:
    print("Largest number is", d)'''

#16Check whether a number is a three-digit number.


'''num = int(input("Enter a number: "))

if num >= 100 and num <= 999:
    print("Three-digit number")
else:
    print("Not a three-digit number")'''


#17Calculate electricity bill using slab rates.

units = int(input("Enter units: "))

if units <= 100:
    bill = units * 2
elif units <= 200:
    bill = units * 3
else:
    bill = units * 5

print("Electricity Bill =", bill)




#18 Calculate income tax based on income slabs.




#19 Check if a student passes (minimum 35 marks in each subject).

'''m1 = int(input("Enter first subject marks: "))
m2 = int(input("Enter second subject marks: "))
m3 = int(input("Enter third subject marks: "))

if m1 >= 35 and m2 >= 35 and m3 >= 35:
    print("Student Passed")
else:
    print("Student Failed")'''


#20 Find whether a number is within a given range.

'''number = int(input("enter thr number:"))

if number >= 1 and number <= 100:
    print("Number within a range")
else:
    print("Not within a range ")'''


#21)Build a simple calculator using if-elif-else (+, -, *, /).

'''a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
op = input("Enter operator (+, -, *, /): ")

if op == '+':
    print("Result =", a + b)
elif op == '-':
    print("Result =", a - b)
elif op == '*':
    print("Result =", a * b)
elif op == '/':
    if b != 0:
        print("Result =", a / b)
    else:
        print("Cannot divide by zero")
else:
    print("Invalid operator")'''


#22) Check if a year is a century leap year.

'''year = int(input("Enter a year: "))

if year % 100 == 0 and year % 400 == 0:
    print("Century Leap Year")
else:
    print("Not a Century Leap Year")'''


#23)Determine the season based on the month number.

'''month = int(input("Enter month number (1-12): "))

if month in [2,3, 4, 5]:
    print("summer")
elif month in [6, 7, 8, 9]:
    print("rainy Season")
elif month in [10,11,12, 1, ]:
    print("winter")
else:
    print("Invalid month number")'''


#24)Find the number of days in a month.

'''month = int(input("Enter month number (1-12): "))

if month == 2:
    print("28 or 29 days")
elif month in [4, 6, 9, 11]:
    print("30 days")
elif month in [1, 3, 5, 7, 8, 10, 12]:
    print("31 days")
else:
    print("invalid month")''' 

#25) Check whether a password meets minimum conditions.

'''password = input ("Enter thr Password:")

if len(password) >= 8:
    print("Valid Password")
else:
    print("Invalid Password")'''


#26)Determine ticket price based on age category.

'''age = int(input("Enter the age:"))

if age < 5:
    print("ticket is free")
elif age <=12:
    print("ticket price is 50")
elif age <= 59:
    print("ticket price is 100")
else:
    print("ticket price is 60")'''

#27)Calculate discount based on purchase amount.

'''amount = int(input("Enter purchase amount: "))

if amount >= 5000:
    print("20% Discount")
elif amount >= 2000:
    print("10% Discount")
else:
    print("No Discount")'''

#28)Check if a person is eligible for a driving license.

'''age = int(input("Enter your age: "))
eyesight = input("Is eyesight normal? (yes/no): ")

if age >= 18 and eyesight == "yes":
    print("eligible for driving license")
else:
    print("not eligible")'''

#29)Create a login system with username and password validation.

'''username = input("enter username:")
password = input("Enter password:")

if username == "admin" and password == "1234":
    print("Login successfully")
else:
    print("Invalid username and password")'''

#30)Create a menu-driven program using if-elif-else with options like:
#Addition ,Subtraction, Multiplication, Division ,Exit


'''print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Exit")

choice = int(input("Enter your choice: "))

if choice == 1:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    print("Addition =", a + b)

elif choice == 2:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    print("Subtraction =", a - b)

elif choice == 3:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    print("Multiplication =", a * b)

elif choice == 4:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    if b != 0:
        print("Division =", a / b)
    else:
        print("cannot divide by zero")

elif choice == 5:
    print("Exit")

else:
    print("invalid choice")'''


