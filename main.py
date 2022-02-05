def fizzbuzz(max_num):
  for num in range(1, max_num):
    if num % 3 == 0 and num % 5 == 0:
      print('{} is FizzBuzz'.format(num))
    elif num % 3 == 0:
      print(f'{num} is Fizz')
    elif num % 5 == 0:
      print(f'{num} is Buzz')
    else:
      print(f'{num} in not Fizz,Buzz or FizzBuzz')

# fizzbuzz(20)

# COMMENTS
# single line comment

"""
multi-line comment
another comment line
"""

# VARIABLES
# must be defined before being called
my_number = 15
# reassigning variables
my_number = 16
# my_number++ won't work
print('my_number: ', my_number)

# DATA TYPES
print(type(42))
print(type('hello world'))
print(type(True))