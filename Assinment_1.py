# 1.Write a Python program to print the multiplication table of a given number.

# num=int(input("Enter a number"))
# for i in range(1,11):
#     result=num*i
#     print(f"{num} * {i} = {result}")

# 2.Write a Python program to check if a given number is a prime number.

# num = int(input("Enter a number: "))

# if num > 1:
#    for i in range(2, num):
#       if (num % i) == 0:
#          print(num, "is not a prime number")
#          break
#    else:
#       print(num, "is a prime number")
# else:
#    print(num, "is not a prime number")

a=[2,6,3,9,5,8,4,10,8,3]
target=12
for i in range(len(a)):
    for j in range(len(a)):
        if a[i]+a[j]==target:
            print(f"The sum of {a[i]} and {a[j]} is equal to {target} and the index is {[i,j]}")