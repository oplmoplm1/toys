class Rlist(object):
	""" A recursive list consisting of a first element and the rest"""
	class EmptyList(object):
		def __len__(self):
			return 0
	empty = EmptyList()
	def __init__(self, first, rest=empty):
		self.first =first
		self.rest = rest
	
	def __repr__(self):
		args = repr(self.first)
		if self.rest is not Rlist.empty:
			args +=',{0}'.format(repr(self.rest))
		return 'Rlist({0})'.format(args)
	
	def __len__(self):
		return 1+ len(self.rest)
	
	def __getitem__(self,i):
		if i==0:
			return self.first
		return self.rest[i-1]

def empty(s):
	return s is Rlist.empty

def  set_contains(s,v):
	"""return  True  if and only if set s contains v"""
	if empty(s):
		return False
	elif s.first == v:
		return True
	return set_contains(s.rest, v)

def adjoin_set(s,v):
	"""Return a set containing all elements of s and element values"""
	if set_contains(s,v):
		return s
	return Rlist(v, s)
	
def filter_rlist(s, fn):
	if s is Rlist.empty:
		return s
	rest = filter_rlist(s.rest, fn)
	if fn(s.first):
		return Rlist(s.first, rest)
	return rest
def intersect_set(set1, set2):
	return filter_rlist(set1, lambda v: set_contains(set2, v))

def union_set(set1, set2):
	set1_not_set2 = filter_rlist(set1, lambda v: not set_contains(set2, v))
	return extend_rlist(set1_not_set2, set2)
	