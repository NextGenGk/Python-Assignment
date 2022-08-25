def factorial(n) :
  result = 1
  for i in range(2, n+1) :
    result = result * i
  return result

n = int(input("Enter a Number : "))
print("Factorial of", n , "is", factorial(n))