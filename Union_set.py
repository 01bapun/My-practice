# 1. Write a Python program to find the union of two sets without using the union() method.

s1={1,5,6,2,8,9,16,24}
s2={5,6,11,10,24,30,17,19}
s3=[]
for i in s1:
    if i not in s3:
        s3.append(i)
for j in s2:
    if j not in s3:
        s3.append(j)
print(set(s3))      

# 2. Explain the difference between a list and a set in Python with examples.


a=[1,1,2,3,4,4,5]
print(a) #out put = [1,1,2,3,4,4,5]  list store duplicate values
b={1,1,2,3,4,4,5}
print(b) #out put = {1,2,3,4,5}  a set can't have duplicate values



# 3. Write a Python program to remove duplicates from a list without changing its order.


l=[12,1,11,15,11,10,15,12,5,22,6,8,10]
l1=[]
for i in l:
    if i not in l1:
        l1.append(i)
print(l1)        

# 4. How would you iterate over a list and its indices simultaneously in Python?

name=["naba","abhisek", "Rahul","pabitra"]
for i in range(len(name)):
   print(f"Index{i}:{name[i]}")    

# 5. Write a Python program to check if all elements in a list are unique.
l=[12,1,11,15,11,10,15,12,5,22,6,8,10]
for i in range(len(l)):
    for j in range(i + 1, len(l)):
        if l[i] == l[j]:
            

# 6.Explain the purpose of the try, except, and finally blocks in Python's exception handling.





# 7.rite a Python program to read a text file line by line and print each line.

with open("UserDetails.txt", "r") as file:
    
    lines = file.readlines()


for line in lines:
    print(line.strip())


# 9.Write a Python program to count the number of occurrences of each word in a text file.






# 10.Explain the difference between the 'r', 'w', and 'a' file modes in Python.



 # 'r' mode 
with open('example.txt', 'r') as file:
    content = file.read()

    #  This mode is  used when you want to read from a file.
    # if the file not 