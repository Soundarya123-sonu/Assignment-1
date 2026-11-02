#Print numbers from 1 to 50

'''def numbers():
    for i in range(1,51):
        print(i)

numbers()'''


#Print numbers from 50 to 1.

'''def numbers():
    for i in range(50,0,-1):
        print(i)
numbers()'''

#Print all even numbers from 1 to 100.

'''def Even_numbers():
    for i in range(1, 100):
        if i % 2 == 0:
            print(i)

Even_numbers()'''

#Print all odd numbers from 1 to 100.

'''def Odd_numbers():
    for i in range(1,101):
        if i % 2 != 0:
            print(i)

Odd_numbers()'''


#Print all numbers that are divisible by 5 from 1 to 100.

'''def divisible():
    for i in range(1,101):
        if i % 5 == 0:
            print(i)

divisible()'''


#Print the sum of numbers from 1 to 50.

'''def total():
    s = 0
    for i in range(1, 51):
        s += i
    print("Sum =", s)

total()'''


#Print the sum of all even numbers from 1 to 20.

'''def sumEven():
    s = 0
    for i in range(2, 21, 2):
        s += i
    print("sum =", s)

sumEven()'''

#Print the sum of all odd numbers from 1 to 20.


'''def sumEven():
    s = 0
    for i in range(1, 21, 2):
        s += i
    print("sum =", s)

sumEven()'''

#Print the first 20 natural numbers.

'''def natural():
    for i in range(1,21):
        print(i)

natural()'''


#Print the multiplication table of a number entered by the user.

'''def table():
    n = int(input("Enter a number: "))
    for i in range(1, 11):
        print(n, "x", i, "=", n * i)

table()'''

#Count how many numbers are there from 1 to N.

'''def count_numbers():
    n = int(input("Enter Nnumber: "))
    count = 0

    for i in range(1, n + 1):
        count += 1

    print("Count =", count)

count_numbers()'''

#Print the square of numbers from 1 to 10.

'''def square():
    for i  in range(1,11):
        print(i * i)
square()'''        


#Print the cube of numbers from 1 to 10.

'''def cube():
    for i in range(1,11):
        print(i * i * i)
cube()'''

#Print numbers from 100 to 1, decreasing by 5 each time.


'''def descering():
    for i in range(100, 1, -5):
        print(i)

descering()'''


#Print all numbers between 1 and 100 that are divisible by 3 and 4.

'''def divisible():
    for i in range(1,101):
        if i % 3 == 0 and i % 4 == 0:
            print(i)
divisible()'''


#Print the first 10 multiples of a given number.

'''def multiples():
    n = int(input("Enter a number: "))
    for i in range(1, 11):
        print(n * i)

multiples()'''



#Print all numbers between 1 and N that are divisible by 2.

'''def even_numbers():
    n = int(input("enter the no:"))
    for i in range(1, n + 1):
        if i % 2 == 0:
            print(i)

even_numbers()'''


#Print numbers from 1 to N, skipping numbers divisible by 3.

'''def Skkip_three():
    n = int(input("Enter the number:"))
    for i in range(1, n + 1):
        if i % 3 != 0:
            print(i)
Skkip_three()'''

# Print numbers from 1 to N and stop when the number reaches 20.
'''def stop_at_20():
    n = int(input("Enter No: "))
    for i in range(1, n + 1):
        if i == 20:
            break
        print(i)

stop_at_20()'''

#Print the following pattern:

def pattern():
    for i in range(1,6):
        print(str(i)* i)

pattern()        
    