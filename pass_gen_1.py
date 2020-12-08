###############for unlimited password length#######################
import random
import string

length = int(input('Enter the length of password\t'))
charac =  string.ascii_lowercase + string.ascii_uppercase + string.punctuation + string.digits
password = ''.join(random.choice(charac) for x in range (length))
print(password)
