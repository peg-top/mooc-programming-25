# Write your solution here

def factorials(n: int):
    factorials_dict = {}
    fact = 1

    for i in range(1, n + 1):
        fact *= i
        factorials_dict[i] = fact
    
    return factorials_dict


if __name__ == "__main__":

    k = factorials(5)
    print(k[1])
    print(k[3])
    print(k[5])

    