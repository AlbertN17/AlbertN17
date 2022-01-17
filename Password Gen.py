import random
chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@$%^&*().,?01234456789'
number = input('Amount of passwords to generate:')
number = int(number)
length = input('Input Your Password Length:')
length = int(length):
 print ( "\nhere are your passwords:")   
    for pwd in range(number):
        passwords = ''
        for c in range(length):
password += random.choice(chars)
print(passwords)

        
