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

fizzbuzz(20)