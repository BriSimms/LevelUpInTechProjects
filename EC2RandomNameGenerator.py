import random
import string 

number = int(input('How many EC2 instances do you want names for?'))
department = input('Please enter the name of your department:')
randomgenerator = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
c=0
while c<number:
    c=c+1
    randomgenerator = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
    print(department + randomgenerator)