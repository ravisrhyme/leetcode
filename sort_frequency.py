"""
Given a string, sort it in decreasing order based on the frequency of characters

Time complexity = O(n)
space Complexity = O(n)
"""
__author__  = "Ravi Kiran Chadalawada"
__email__   = "rchadala@usc.edu"
__credits__ = ["Leetcode.com"]
__status__  = "Prototype"

from collections import defaultdict

def sort_string(s):

	alphabet_count = defaultdict(int)
	count_to_alphabet = {}
	result = ''
	for i in range(len(s)+1):
		count_to_alphabet[i] = []

	for char in s:
		alphabet_count[char] += 1
		
	for key,value in alphabet_count.items():
		count_to_alphabet[value].append(key)

	for i in range(len(s),0,-1):
		temp_list = count_to_alphabet[i]
		for char in temp_list:
			result += (char * i)

	return result



if __name__=='__main__':
	print(sort_string('raviaar')) 
