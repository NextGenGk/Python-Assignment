def strCon(str) :
  arr = []
  for i in range(len(str)) :
    arr.append(str[i])
  return arr
str = input("Enter a String : ")
arr = strCon(str)
print(arr)