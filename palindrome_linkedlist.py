"""
Given a singly linked list, determine if it is a palindrome.

Time Complexity : O(n)
Space Complexity : O(n)
"""
__author__  = "Ravi Kiran Chadalawada"
__email__   = "rchadala@usc.edu"
__credits__ = ["Leetcode.com"]
__status__  = "Prototype"

class node:
	def __init__(self,value):
		self.data = value
		self.next = None

def is_palindrome(head):
	
	no_of_nodes = 0
	current_node = head

	while current_node is not None:
		current_node = current_node.next
		no_of_nodes += 1

	if no_of_nodes%2 == 0:
		first_end = no_of_nodes/2 
		second_begin = first_end + 1
	else:
		first_end = int(no_of_nodes/2)
		second_begin = first_end + 2

	i = 1
	current_node = head
	data_stack = []
	while i <= first_end:
		data_stack.append(current_node.data)
		current_node = current_node.next
		i += 1	

	if no_of_nodes%2 != 0:
		current_node = current_node.next	 

	while current_node is not None:
		if current_node.data != data_stack.pop():
			return False
		current_node = current_node.next

	return True



if __name__== '__main__':

	a = node('r')
	b = node('a')
	c = node('a')
	d = node('r')

	a.next = b
	b.next = c
	c.next = d
	print(is_palindrome(a))
