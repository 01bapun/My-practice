ch=input("1 Creat\n2 Login :")
if(ch=='1'):
    username=input("Enter your User name: ")
    password=input("Enter your Password: ")
    rpassword=input("Re-enter your Password: ")
    if(password==rpassword):
        string=""
        file=open("UserDetails.txt","a+")
        string+=f",{username}"
        string+=f",{password}"
        file.write(string)
        file.close()
elif(ch=='2'):
    file=open('userdetails.txt','r')
    temp=''
    for x in file.read():
        temp+=x
    temp=temp.split(",")
    mydict={}
    for x in range(1,len(temp),2):
        mydict[temp[x]]=temp[x+1]

    username=input("Enter username")
    password=input("Enter password")
    count=0
    for x in mydict.items():
        if(username==x[0] and password==x[1]):
            count+=1
    if(count==1):
        print("login sucess")
    else:
        print("Faild")   