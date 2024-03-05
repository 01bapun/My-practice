# sum .......................

a =[23,54,56,3,50,45]
count=0
for i in range(0,len(a)):
    count = count+a[i]
print(count)

#    minimum..................

a =[23,54,56,3,50,45]
min=a[0]
for i in range(0,len(a)):
    if (a[i]<min):
         min=a[i]
print(min)

# maximum......................

a =[23,54,56,3,50,45]
max=a[0]
for i in range(0,len(a)):
    if(a[i]>len(a)):
        max=a[i]
print(max)        

# Length.................

a =[23,54,56,3,50,45]
count=0
for i in a:
    count=count+1
print(count)    

# Reverse.................

a =[23,54,56,3,50,45]

print(a[::-1])