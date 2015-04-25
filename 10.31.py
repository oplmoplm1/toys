def count_leaves(tree):
	if type(tree) != tuple:
		return 1
	return sum(map(count_leaves, tree))
	
def map_tree(tree, fn):
	if type(tree) != tuple:
		return fn(tree)
	return tuple(map_tree(branch, fn) for branch in tree)
	
def square(n):
	return n*n
class Tree(object):
	def __init__(self, entry, left=None, right=None):
		self.entry = entry
		self.left = left
		self.right = right
	def __repr__(self):
		args = repr(self.entry)
		if self.left or self.right:
			args += ',{0},{1}'.format(repr(self.left),repr(self.right))
			return 'Tree({0})'.format(args)
			
class fib_tree(n):
	if n == 1:
		return Tree(0)
	if n == 2:
		return Tree(1)
	left = fib_tree(n-2)
	right = fib_tree(n-1)
	return Tree(left.entry + right.entry, left, right)