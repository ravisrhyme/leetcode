"""
Write a function to find sum of elements in an array
given the indices
"""
__author__  = "Ravi Kiran Chadalawada"
__email__   = "rchadala@usc.edu"
__credits__ = ["leetcode.com"]
__status__  = "Prototype"


class NumArray(object):
	def __init__(self, nums):
		self.nums = nums
		self.sum_list = []
		self.sum_list.append(nums[0])
		for i in range(1,len(nums)):
			self.sum_list.append(self.sum_list[i-1] + nums[i])

	def sumRange(self, i, j):
		if i == 0:
			return self.sum_list[j]
		else :
			return self.sum_list[j] - self.sum_list[i-1]


if __name__ == "__main__":
	nums = [-2,0,3,-5,2,-1]
	obj = NumArray(nums)
	print(obj.sumRange(0,2))
	print(obj.sumRange(2,5))
	print(obj.sumRange(0,5))
