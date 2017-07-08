"""
Find the longest increasing subsequence in a given list

Time Complexity = O(n)
Space Complexity = O(1)

"""
__author__  = "Ravi Kiran Chadalawada"
__email__   = "rchadala@usc.edu"
__credits__ = ["Leetcode.com"]
__status__  = "Prototype"


def lis(number_list):
	""" Returns the length of longest incresing subsequence in a list
	"""
	current_length = 0
	max_length = 0

	previous_number = -float('inf')
	for number in number_list:
		if number > previous_number:
			current_length += 1
		else:
			current_length = 0

		if max_length < current_length:
			max_length = current_length
		
		previous_number = number
	return max_length



if __name__=='__main__':
	number_list = [1,2,3,-4,-5,6]
	print(lis(number_list))
