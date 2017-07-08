"""
Find the contiguous subarray within an array (containing at least one number) 
which has the largest sum.

For example, given the array [-2,1,-3,4,-1,2,1,-5,4],
the contiguous subarray [4,-1,2,1] has the largest sum = 6.

Implemented Kadane's algorithm

Time Complexity = O(n)
Space Complexity = O(1)

"""
__author__  = "Ravi Kiran Chadalawada"
__email__   = "rchadala@usc.edu"
__credits__ = ["Leetcode.com"]
__status__  = "Prototype"



def max_subarray(number_list):
	""" Returns maximum sub array sum
	"""
	max_so_far = -float('inf')
	max_current = 0

	for number in number_list:
		max_current += number

		if max_so_far < max_current:
			max_so_far = max_current

		if max_current < 0:
			max_current = 0

	return max_so_far


if __name__=='__main__':

	number_list = [-2,1,-3,4,-1,2,1,-5,4]
	print(max_subarray(number_list))
