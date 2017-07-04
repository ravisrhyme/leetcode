"""
Write a program to find the node at which the intersection of two singly linked
lists begins.

For example, the following two linked lists:

A:          a1 → a2
                   ↘
                     c1 → c2 → c3
                   ↗            
B:     b1 → b2 → b3

begin to intersect at node c1.

Notes:

* If the two linked lists have no intersection at all, return null.
* The linked lists must retain their original structure after the function returns
* You may assume there are no cycles anywhere in the entire linked structure.
* Your code should preferably run in O(n) time and use only O(1) memory.

Time Complexity : O(n)
Space Complexity : O(1)

Beautiful idea it is !! Moving the pointers of lists to point to point to other 
list once it reaches the end and keep rolling till both meet !! Needs a deep 
thought
"""
__author__  = "Ravi Kiran Chadalawada"
__email__   = "rchadala@usc.edu"
__credits__ = ["leetcode.com"]
__status__  = "Prototype"


class node:
	def __init__(self,value):
		self.data = value
		self.next = None


def find_intersection(head1,head2) :

	if head1 is None or head2 is None:
		return None
	
	temp1 = head1
	temp2 = head2
	
	while temp1 != temp2:

		if temp1 is None:
			temp1 = head2
		else:
			temp1 = temp1.next
		
		if temp2 is None:
			temp2 = head1
		else:
			temp2 = temp2.next

	return temp1


if __name__=='__main__':
	
	a = node(1)
	b = node(3)
	c = node(5)
	d = node(7)
	e = node(9)
	f = node(11)

	g = node(2)
	h = node(4)


	a.next = b
	b.next = c
	c.next = d
	d.next = e
	e.next = f
	
	g.next = h
	#h.next = e

	intersection = find_intersection(a,g)
	
	if intersection is not None:
		print(intersection.data)
	else:
		print(intersection)
