"""
Given an array of strings, group anagrams together.

For example, given: ["eat", "tea", "tan", "ate", "nat", "bat"], 
Return:

[
  ["ate", "eat","tea"],
  ["nat","tan"],
  ["bat"]
]

Time Complexity: O(n)
Assuming the sorting of strings to be O(44log(44)) at max as length of longest
word in english is 44
Space Complexity : O(n)

"""

__author__  = "Ravi Kiran Chadalawada"
__email__   = "rchadala@usc.edu"
__credits__ = ["Leetcode.com"]
__status__  = "Prototype"


#from collections import defaultdict

class Solution():

	def group_anagrams(self, strs):
		""" Groups anagrams in the given list.
		and returns a list of lists
		"""
		anagrams = {}
		result_list = []
		sum_word = 0
		for word in strs:
			sorted_word = ''.join(sorted(word))

			if sorted_word in anagrams:
				anagrams[sorted_word].append(word)    
			else:
				anagrams[sorted_word] = [word]
		for key,value in anagrams.items():
			result_list.append(value)
	
		return result_list


if __name__=='__main__':
	
	s = Solution()
	strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
	print(s.group_anagrams(strs))
