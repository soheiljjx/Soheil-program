from random import randint, choice

password = input('enter your password: ')
n = len(password)

alphabet = 'abcdefghijklmnopqrstuvwxyz1234567890'
passw = ''
counter = 0
while passw != password:
    passw = ''
    for i in range(n):
        passw += choice(alphabet)
        
    counter += 1

print('You Hacked')