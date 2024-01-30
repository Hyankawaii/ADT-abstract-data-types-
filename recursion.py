def factorial(n):
  x = 1
  while(n > 1):
    x = x * n
    n = n - 1
  return(x)


def compounding(Principle, Rate, Year):
  if Year == 0:
    return Principle
  else:
    Principle = Principle *(1 + Rate)
    return(compounding(Principle, Rate, (Year - 1)))

def fibonacci(num1, num2, repititions):
  if repititions != 0:
    x = num1 + num2 
    print(x)
    num1 = num2
    num2 = x
    fibonacci(num1, num2, repititions - 1)


def fibonacci2(num1, num2, repititions):
  if repititions != 0:
    print(num2)
    fibonacci(num2, (num1 +num2), repititions - 1)
fibonacci2(0, 1, 4)

