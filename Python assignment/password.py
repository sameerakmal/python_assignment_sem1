def length(password):
    if len(password)<10:
        print("Password should be atleast 10 characters long.")

def uppercase(password):
    count=0
    for char in password:
        if char.isupper():
            count+=1
    if count<2:
            print("Password should contain atleast two capital letters.")

def lowercase(password):
    count=0
    for char in password:
        if char.islower():
            count+=1
    if count<2:
            print("Password should contain atleast two lower case letters.")

def digits(password):
    count=0
    for int in password:
          if int.isdigit():
               count+=1
    if count<2:
         print("Password should contain atleast two digits.")

def special(password):
    count=0
    for char in password:
        if char in ['@','#','$','%','&','*','!']:
            count+=1
    if count<2:
         print("Password should contain atleast two special characters.")

def repeat(password):
    for i in range(len(password)-3):
        if password[i:i+4] ==  password[i] * 4:
            print("Password should not contain repetition.")

def passcheck(password,old_pass):
     for i in range(len(old_pass)):
          if password == old_pass[i]:
            print("Password should not be same as the old password.")
            break

def usercheck(username,password):
    for i in range(len(username)-2):
         if username[i:i+3] in password:
              print("Password should not contain three consecutive characters from username")
              break

username=input("Enter the username : ")
password=input("Enter the password : ") 
pass1= input("enter old password1 :")
pass2= input("enter old password2 :")
pass3= input("enter old password3 :")
old_pass=[pass1,pass2,pass3]

length(password)
uppercase(password)
lowercase(password)
digits(password)
special(password)
repeat(password)
passcheck(password,old_pass)
usercheck(username,password)


