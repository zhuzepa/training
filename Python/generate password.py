# generate password which is tough to break for hacker

import random
lower_case = "abcdefghijklmnopqrstuvwxyz"
upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
number = "0123456789"
symbols = "@#$%&*/\?"

Use_for = lower_case + upper_case + number + symbols
length_for_pass = 8

password = "".join(random.sample(Use_for, length_for_pass))

print("Your Generated Password is: ")
