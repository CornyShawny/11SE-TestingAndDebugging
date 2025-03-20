# Write test cases for boundary values for the following:
def is_safe_temperature(temp):
    return 0 <= temp <= 100
print(is_safe_temperature(0))
print(is_safe_temperature(101))
print(is_safe_temperature(-1))
print(is_safe_temperature(100))

# Write test cases for path coverage for the following:

def ticket_price(age):
    if age < 5:
        return "Free"
    elif 5 <= age <= 17:
        return "$5"
    elif 18 <= age <= 64:
        return "$10"
    else:
        return "Senior Discount - $7"

print(ticket_price(3))
print(ticket_price(10))
print(ticket_price(30))
print(ticket_price(70))

# Write test cases for faulty and abnormal data for the following:

def divide_numbers(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Error: Cannot divide by zero"
    except TypeError:
        return "Error: Invalid input, numbers required"

print(divide_numbers("x", "y"))
print(divide_numbers(1, 0))
print(divide_numbers(17, 38))