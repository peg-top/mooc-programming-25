# Write your solution here

# Write your solution here

import random
import string

def generate_password(num):
    return "".join([random.choice(string.ascii_lowercase) for _ in range(num)])

# for i in range(10):
#     print(generate_password(8))