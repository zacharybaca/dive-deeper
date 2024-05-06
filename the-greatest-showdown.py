"""Task 1: Identify the Greatest
Write a Python program that prompts the user to enter three numbers. The program should then identify and print out the largest number among the three."""

number_one = input("Enter Your First Number: ")
number_two = input("Enter Your Second Number: ")
number_three = input("Enter Your Third Number: ")

if number_two < number_one > number_three:
    print("The Largest Number is: ", number_one)
elif number_one < number_two > number_three:
    print("The Largest Number is: ", number_two)
elif number_one < number_three > number_two:
    print("The Largest Number is: ", number_three)

"""Task 2: Identify the Smallest
Extend your program from Task 1 to also determine the smallest number among the three and print it out."""

if number_two > number_one < number_three:
    print("The Smallest Number is: ", number_one)
elif number_one > number_two < number_three:
    print("The Smallest Number is: ", number_two)
elif number_one > number_three < number_two:
    print("The Smallest Number is: ", number_three)

"""Task 3: Equality Check
Enhance your program to handle cases where two or all of the numbers are equal. The program should display appropriate messages like "Two numbers are equal and the largest" or "All numbers are equal"."""

if number_one == number_two and number_one == number_three and number_two == number_three:
    print("All The Numbers Are Equal to Each Other")
elif number_one == number_three:
    print("There Are Two Numbers That Are Equal to Each Other: ", number_one, number_three)
elif number_two == number_three:
    print("There Are Two Numbers That Are Equal to Each Other: ", number_two, number_three)
elif number_one == number_two:
    print("There Are Two Numbers That Are Equal to Each Other: ", number_one, number_two)

"""Expected Outcome: If we provide the numbers 3, 3, and 4, it should print out that "The smallest number is 3. The largest number is 4. There are two numbers equal to each other." Printing out which numbers are equal would be a great added bonus."""
