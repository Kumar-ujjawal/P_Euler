#The prime factors of 13195 are 5,7,13 and 29.
#What is the largest prime factor of the number 600851475143

# Python program to print prime factors

import math

l1 = []
# def primeFactors(n):
	

# 	while n % 2 == 0:
# 		print(2)
# 		n = n // 2

# 	for i in range(3,int(math.sqrt(n))+1,2):
		

# 		while n % i== 0:
# 			print(i)
# 			n = n // i
			
# 	if n > 2:
# 		l1.append(n)
# 	return l1
# Using anonymous function
prime_factors = lambda n: [i for i in range(2, n+1) if n%i == 0 and all(i % j != 0 for j in range(2, int(i**0.5)+1))]
n = 600851475143
factors = []
while n > 1:
	for factor in prime_factors(n):
		factors.append(factor)
		n //= factor
print(*factors)


# print("maximum prime factor of 600851475143 is :",max(primeFactors(600851475143)))
