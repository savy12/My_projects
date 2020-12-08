###########for max 94 character length################
import string
import random

s1 = string.digits
s2 = string.ascii_lowercase
s3 = string.ascii_uppercase
s4 = string.punctuation
plen = int(input('Enter length of password:- '))
s=[]
s.extend(list(s1))
s.extend(list(s2))
s.extend(list(s3))
s.extend(list(s4))
random.shuffle(s)

password = ''.join(random.sample(s,plen))
print(password)
