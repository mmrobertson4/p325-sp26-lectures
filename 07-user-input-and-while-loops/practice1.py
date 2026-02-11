#a, b, c = input("Enter 3 numbers: ")
a = float(input("Enter a number: "))
b = float(input("Enter another number: "))
c = float(input("Enter 1 more number: "))
print(f'{a}x^2 + {b}x + {c} = 0')

from math import sqrt
x1 = (-b + sqrt(b**2 - 4*a*c))/(2*a)
x2 = (-b - sqrt(b**2 - 4*a*c))/(2*a)

print(f'Solution 1: {x1}')
print(f'Solution 2: {x2}')