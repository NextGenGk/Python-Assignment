year = int(input("Enter Your Year : "))
if (year%400==0 or (year%100!=0 and year%4==0)):
  print("It is a Leap Year")
else:
  print("Not a leap year")