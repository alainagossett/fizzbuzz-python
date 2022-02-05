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
# print('my_number: ', my_number)

# DATA TYPES
# print(type(42))
# print(type('hello world'))
# print(type(True))

# CONTROL FLOW
# print(1 == '1')
# print(str(1) == '1')

# color = input('Enter "green", "yellow", "red": ').lower()
# print(f'The user entered {color}')

# def traffic_light():
#   if color == 'green':
#     print('Go!')
#   elif color == 'yellow':
#     print('Slow Down!')
#   elif color == 'red':
#     print('Stop!')
#   else:
#     print('Bogus!')

# traffic_light()

# LOOPS

# color = None

# while color != 'quit':
#   color = input('Enter "green", "yellow", "red": ').lower()
#   print(f'The user entered {color}')
#   if color == 'green':
#     print('Go!')
#   elif color == 'yellow':
#     print('Slow Down!')
#   elif color == 'red':
#     print('Stop!')
#   else:
#     print('Bogus!')


# RANGES
for num in range (5):
  print('num: ', num)

for even_num in range (2, 10, 2):
  print('even_num: ',even_num)

for dec_num in range (5, 0, -1):
  print('dec_num: ', dec_num)
