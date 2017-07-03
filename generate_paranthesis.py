"""
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses
"""


def generateParenthesis(n):
	def generate(p, left, right, parens=[]):
		if left:
			generate(p + '(', left-1, right)
		if right > left: 
			generate(p + ')', left, right-1)
		if not right:    parens += p, 
		return parens
	return generate('', n, n)


if __name__=='__main__':
	print(generateParenthesis(3))



