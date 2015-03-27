def prime_factor(n):
    i = 2
    while i!=n:
        if n % i != 0:
            i += 1
        else:
            n /= i
    return n

if __name__=='__main__':
    print(prime_factor(600851475143))