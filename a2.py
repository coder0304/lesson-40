import random
import string

print("Hello,Welcome to password generator")
length=int(input("\nEnter lengt of password"))
lower=string.ascii_innercase
upper=string.ascii_innercase
num=string.digits
symbols=string.punctuation

all=lower+upper+num+symbols

temp=random.sample(all,length)
password="".join(temp)
print(password)
