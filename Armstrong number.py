# Program to check if a 3-digit number is an Armstrong number
num = int(input("Enter a 3-digit integer: "))

temp = num
sum_of_cubes = 0

while temp > 0:
    digit = temp % 10  # Extract the last digit
    sum_of_cubes += digit ** 3  # Cube the digit and add to sum
    temp //= 10  # Remove the last digit

if num == sum_of_cubes:
    print(f"{num} is an Armstrong number!")
else:
    print(f"{num} is not an Armstrong number.")
