#Generate Random Password

import random

upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lower = "abcdefghijklmnopqrstuvwxyz"
numbers = "0123456789"
symbols = "!@#$%&*()."

string = upper + lower + numbers + symbols
length = 16

password = "".join(random.sample(string,length))
print("Your Random Generated Password Is: " + password)