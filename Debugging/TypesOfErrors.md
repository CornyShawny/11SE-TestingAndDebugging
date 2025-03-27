1.
```
def calculate_area(radius):
    area = 3.14 x radius x 2
    return area

print(calculate_area(5))
print(calculate_area(3))
```
syntax error, the code uses "x" to multiply instead of "*"

2.
```
def calculate_area(length, width):
    return length + width

area = calculate_area(5, 3)
print(f"Area: {area}")
```
logical error, the code uses addition for the area instead of multiplication
3.
```
def divide(a, b):
    return a / b

result = divide(10, 0)
print(result)
```
runtime error, the code divides by 0 which is why it doesn's work
4.
```
for i in range(5)
    print(i)
```
syntax error, missing a colon for the 'for' statement
5.
```
def calculate_average(numbers):
    total = sum(numbers)
    return total - len(numbers)

numbers = [10, 20, 30, 40]
average = calculate_average(numbers)
print(f"Average: {average}")
```
logical error
6.
```
def calculate_area(diameter):
    return math.pi * diameter ** 2

print(calculate_area(5))
```