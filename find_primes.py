"""
Count the number of prime numbers less than a non-negative number, n.

Time Complexity : O(n*sqrt(n))
space complexity : O(n)
"""
__author__  = "Ravi Kiran Chadalawada"
__email__   = "rchadala@usc.edu"
__credits__ = ["Leetcode.com"]
__status__  = "Prototype"


import math

def count_primes(n):

	prime_numbers = [True] * n
	prime_numbers[0] = False
	prime_numbers[1] = False
	limit = int(math.sqrt(n))
	count = 0

	#Sieve of Eratosthense algorithm. Sets every non prime to 1.
	for number in range(2,limit+1):
		if prime_numbers[number] == True:
			j = 2
			while (number * j) < n:
				prime_numbers[number * j] = False
				j += 1

	# Counting the number of primes
	for number in prime_numbers:
		if number == True:
			count += 1

	print(prime_numbers[1:])
	return count

if __name__ == '__main__':
	print(count_primes(10))
