import string
import random

s1=list(string.ascii_lowercase)
s2=list(string.ascii_uppercase)
s3=list(string.digits)
s4=list(string.punctuation)

size_of_passsword=input("enter the size of the password:")
while(True):
    try:
        size_of_passsword=int(size_of_passsword)
        if (size_of_passsword<6):
            print("the smallest value is 6")
            size_of_passsword=input("enter the size of the password:")
        else:
            break
    except:
        print("please enter a number")
        size_of_passsword=input("enter the size of the password:")
random.shuffle(s1);
random.shuffle(s2);
random.shuffle(s3);
random.shuffle(s4);
part1=round(size_of_passsword*(30/100))
part2=round(size_of_passsword*(20/100))
password=[]
for i in range(part1):
    password.append(s1[i])
    password.append(s2[i])
for i in range(part2):
    password.append(s3[i])
    password.append(s4[i])
password="".join(password[0:])
print(password)