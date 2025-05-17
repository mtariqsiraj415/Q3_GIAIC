import random




print("****************Welcome to the Password Generator!****************")

length = int(input("Enter the length of the password: "))
chr = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!#$%&'()*+,-./:;<=>?@[]^_`{|}~"
password = ''
for i in range(length):
    password += random.choice(chr)
print("Your password is: " + password)



