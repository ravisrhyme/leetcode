"""
Serialization is the process of converting a data structure or object into a
sequence of bits so that it can be stored in a file or memory buffer, or 
transmitted across a network connection link to be reconstructed later in the
same or another computer environment.

Design an algorithm to serialize and deserialize a binary tree. There is no 
restriction on how your serialization/deserialization algorithm should work. 
You just need to ensure that a binary tree can be serialized to a string and 
this string can be deserialized to the original tree structure.

For example, you may serialize the following tree

    1
   / \
  2   3
     / \
    4   5

as "[1,2,3,null,null,4,5]"

Preorder traversal helps here.

Time Complexity = O(n)
space Complexity = O(n)

"""
__author__  = "Ravi Kiran Chadalawada"
__email__   = "rchadala@usc.edu"
__credits__ = ["leetcode.com"]
__status__  = "Prototype"

class node:
	def __init__(self,value):
		self.data = value
		self.left = None
		self.right = None

def serialize(root,serialize_bt=[]):
	""" Returns the serialized Tree
	"""
	if root is None:
		serialize_bt.append(None)
		return
	else: 
		serialize_bt.append(root.data)
	
	serialize(root.left,serialize_bt)
	serialize(root.right,serialize_bt)


def deserialize(serialize_bt):
	"""" Returns root after building binary from serialized tree
	"""
	if serialize_bt is None:
		return None

	value = serialize_bt.pop(0)
	if value is not None:
		temp_node = node(value)
		temp_node.left = deserialize(serialize_bt)
		temp_node.right = deserialize(serialize_bt)
		return temp_node
	else:
		return None

	
def preorder_print(root):
	
	if root is None:
		return
	
	print (root.data)
	preorder_print(root.left)
	preorder_print(root.right)

if __name__=='__main__':

	a = node(1)
	b = node(2)
	c = node(3)

	a.left = b
	a.right = c
	
	preorder_print(a)
	serialize_bt = []
	serialize(a,serialize_bt)
	print(serialize_bt)
	temp = deserialize(serialize_bt)
	preorder_print(temp)
