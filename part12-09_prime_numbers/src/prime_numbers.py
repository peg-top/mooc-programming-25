# Write your solution here

def is_prime(number):
    if number <= 1:
        return False  
    if number <= 3:
        return True  
    if number % 2 == 0 or number % 3 == 0:
        return False  
    
    i = 5
    while i * i <= number:
        if number % i == 0 or number % (i + 2) == 0:
            return False
        i += 6
    return True

def prime_numbers():
    num = 2
    while True:
        if is_prime(num):
            yield num
        num+=1
if __name__ == "__main__":
    numbers = prime_numbers()
    for i in range(8):
        print(next(numbers))