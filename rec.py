def fibonacci(num):
     if num <= 0:
          return 'Invalid Input'
     elif num == 1:
          return 0
     elif num == 2:
          return 1
     
     return fibonacci(num - 1) + fibonacci(num - 2)