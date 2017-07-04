"""
Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in
the tree.

Time Complexity = O(n)
Space Complexity = O(log(n)) for a balanced binary tree
				   O(n) worst case
"""

__author__  = "Ravi Kiran Chadalawada"
__email__   = "rchadala@usc.edu"
__credits__ = ["Leetcode.com"]
__status__  = "Prototype"


class node:
	
	def __init__(self,data):
		self.data = data
		self.left  = None
		self.right = None

def find_lca(root,p,q):

	if root is None:
		return None

	if root in [p,q]:
		return root.data

	path1 = find_path(root,p)
	path2 = find_path(root,q)
	
	print(path1)
	print(path2)
	
	
	if (path1 is not None) and (path2 is not None):
		return find_lca_utility(path1,path2)
	else:
		return None



def find_path(root,dest):
	
	node_stack = [(root,[root.data])]
	
	while len(node_stack) != 0:
		
		node ,path = node_stack.pop()
		#node = node_info[0]
		#path = node_info[1]

		if node is dest:
			return path

		if node.left is not None:
			temp = path + [node.left.data]
			node_stack.append((node.left,temp))

		if node.right: 
			temp = path + [node.right.data]
			node_stack.append((node.right,temp))

	return None


def find_lca_utility(path1,path2):
	
	length = min(len(path1),len(path2))

	i = 0
	last_node = None
	while i < length:
		if path1[i] == path2[i]:
			last_node = path1[i]
		else:
			return last_node
		i += 1


# Works only if all nodes are present in tree
# Fails if any of p/q is not in tree. Leet code
# solution it is
def pythonic_lowestCommonAncestor(root, p, q):
	if root in (None, p, q): return root
	left, right = (pythonic_lowestCommonAncestor(kid, p, q) for kid in (root.left, root.right))
	return root if left and right else left or right


if __name__=='__main__':
	a = node(1)
	b = node(2)
	c = node(3)
	d = node(4)
	e = node(5)
	f = node(6)
	g = node(7)
	h = node(8)

	a.left = b
	a.right = c
	b.left = d
	b.right = e
	e.left = f
	e.right = g
	print(find_lca(a,d,h))

	#print(pythonic_lowestCommonAncestor(a,d,e).data)
