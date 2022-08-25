import math
a = int(input("Enter a number : "))
sum = 1
for i in range(1, a+1) :
  fact = 1 / math.factorial(i)
  sum = sum + fact
print("answer is : ", sum)