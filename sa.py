from functools import partial

def multiply(x, y):
    return x * y

# Create a new function that multiplies by 2
double = partial(multiply, 3)

# Call the new function
result = double(5)
print(result)  # Output: 10
