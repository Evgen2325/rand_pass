import random

symbols = '1234567890qwertyuiopasdfghjklzxcvbnm'
lenght = input('Input lenght password please: \n')
password = ''
for i in range(int(lenght)):
    password += random.choice(symbols)
print(password)
