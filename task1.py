# 1. Sum of Two Numbers
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("Sum:", a + b)


# 2. Odd or Even Checker
num = int(input("Enter a number: "))
if num % 2 == 0:
    print("Even")
else:
    print("Odd")


# 3. Factorial Calculation
n = int(input("Enter a number: "))
fact = 1
for i in range(1, n + 1):
    fact *= i
print("Factorial:", fact)


# 4. Fibonacci Sequence
n = int(input("Enter number of terms: "))
a, b = 0, 1
print("Fibonacci sequence:")
for i in range(n):
    print(a, end=" ")
    a, b = b, a + b
print()


# 5. String Reverse
s = input("Enter a string: ")
print("Reversed string:", s[::-1])


# 6. Palindrome Check
s = input("Enter a word: ")
if s == s[::-1]:
    print("Palindrome")
else:
    print("Not a palindrome")


# 7. Leap Year Check
year = int(input("Enter a year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Leap Year")
else:
    print("Not a Leap Year")


# 8. Armstrong Number
num = int(input("Enter a number: "))
order = len(str(num))
sum_val = 0

temp = num
while temp > 0:
    digit = temp % 10
    sum_val += digit ** order
    temp //= 10

if num == sum_val:
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")
