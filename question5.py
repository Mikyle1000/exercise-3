# Question 5: Using a Function as an Argument

# TODO: Define a function called 'apply_operation' that takes a function and a number as parameters, and returns the result of applying the function to the number
def apply_operation (function, number):
  return function(number)

# TODO: Define a function called 'double' that takes a number as a parameter and returns its double
def double (number):
  return number*2

# TODO: Use the 'apply_operation' function with the 'double' function and the number 7, and print the result
apply_operation_double = apply_operation(double, 7)
print(apply_operation_double)

# TODO: Use the 'apply_operation' function with the 'square' function (defined in Question 3) and the number 3, and print the result
def square(number):
  return number**2

apply_operation_square = apply_operation(square, 3)
print(apply_operation_square)