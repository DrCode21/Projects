import random

print('Welcome To Your Password Geberator')

chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*(),.?0123456789'

number = input('Amount of passwords to generate: ')
number = int(number)

length = input('Input Your password length')
length = int(length)

print ('Here are your passwords: ')

for pwd in range(number):
    passwords = ''
    
    for c in range(length):
        passwords += random.choice(chars)
    print(passwords)