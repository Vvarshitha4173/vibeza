"""1)Write a Python program that performs the following tasks:
1. Ask the user to enter a positive integer `n`.
2. Use a `for` loop to print all numbers from `1` to `n` on separate lines.
3. Use a `while` loop to calculate the sum of all numbers from `1` to `n` and print the result."""

# Task 1: Ask the user to enter a positive integer n
n = int(input("Enter a positive integer: "))

# Task 2: Use a for loop to print all numbers from 1 to n on separate lines
print("\nNumbers from 1 to", n, "using for loop:")
for i in range(1, n+1):
    print(i)

# Task 3: Use a while loop to calculate the sum of all numbers from 1 to n and print the result
sum_of_numbers = 0
i = 1
while i <= n:
    sum_of_numbers += i
    i += 1

print("\nSum of all numbers from 1 to", n, "using while loop:", sum_of_numbers)
print('\n')
'''*******************************************************************************'''

'''2)Write a Python program that includes a user-defined function to perform the following tasks:
1. Define a function named calculate_square that takes a single argument `n` and returns the square of `n`.
2. In the main program, ask the user to input a positive integer.
3. Call the calculate_square function with the user-provided number and display the result.'''


# Task 1: Define the function calculate_square
def calculate_square(n):
    return n ** 2  # Return the square of n

# Task 2: Ask the user to input a positive integer
n = int(input("Enter a positive integer: "))

# Task 3: Call the calculate_square function with the user-provided number and display the result
square = calculate_square(n)
print(f"The square of {n} is: {square}")





