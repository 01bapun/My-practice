# file=open('abc.txt','w') #open a file that will written and over written if it exists
# msg=input("Enter the message:")
# file.write(msg)
# file.close


# .................................
# anather exp of file handling........
'''
try:
    file=open('abc.txt','w')
    msg=input("Enter the message:")
    file.write(msg)
    print("Message saved successfully.")
except IOError:
    print("Error: Unable to open or write to the file.")
finally:
    file.close() '''

    # ..........................
# add content at end  of existing file...
file=open('abc.txt', 'a')
msg=input("Enter the message:")
file.write(msg)



# Read the exiting  data from file
file=open('abc.txt', 'r')
x=file.read()
print("The content of the file is :",x)
file.close()