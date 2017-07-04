"""
Given two strings s and t, write a function to determine if t is an anagram of s.

For example,
s = "anagram", t = "nagaram", return true.
s = "rat", t = "car", return false.

Note:
You may assume the string contains only lowercase alphabets.

"""
__author__  = "Ravi Kiran Chadalawada"
__email__   = "rchadala@usc.edu"
__credits__ = ["Leetcode.com"]
__status__  = "Prototype"

def is_anagram(s, t):
	""" Returns true if s and t are anagrams.
	else returns false
	"""
	if (''.join(sorted(s)) == ''.join(sorted(t))):
		return True
	else:
		return False


if __name__=='__main__':

	print(is_anagram('ravi', 'avi'))
