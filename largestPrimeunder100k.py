def is_prime(n): 
    for i in range(2, int(n**0.5)+1): 
        if n % i == 0: 
            return False
    return True


def largestprimenumber(num): 
    largestprime = 0
    for i in range(2, num+1): 
        if isprime(i): 
            largestprime = i 
    return largestprime 


print(largestprimenumber(100000))
