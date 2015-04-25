class Number(object):
	""" 数值类"""
	def __init__(self,value):
		self.value = value
	
	def to_py(self):
		return repr(self.value)
	
class Boolean(object):
	""" bool class"""
	def __init__(self, value):
		self.value = value
	
	def to_py(self):
		return repr(self.value)

class Variable(object):
	""" Variable class"""
	def __init__ (self, name):
		self.name = name
	
	def to_py(self):
		return repr(self.name)
		

		
class Add(object):
	def __init__(self, left, right):
		self.left = left
		self.right = right
	
	def to_py(self):
		left =repr(self.left.to_py())
		right = repr(self.right.to_py())
		return 'eval({left},globals()) + eval({right},globals())'.format(**locals())
		 
class Multiply(object):
	def __init__(self, left, right):
		self.left = left
		self.right = right
	
	def to_py(self):
		left =repr(self.left.to_py())
		right = repr(self.right.to_py())
		return 'eval({left},globals())*eval({right},globals())'.format(**locals())
	
class LessThan(object):
	def __init__(self,left,right):
		self.left =left
		self.right = right
		
	def to_py(self):
		left =repr(self.left.to_py())
		right = repr(self.right.to_py())
		return 'eval({left},globals())<eval({right},globals())'.format(**locals())
	

class DoNothing(object):
	def to_py(self):
		return ""

class Assign(object):
	def __init__(self, name, expression):
		self.name = name
		self.expression = expression
	
	def to_py(self):
		name = self.name
		expression = repr(self.expression.to_py())
		return '{name} = eval({expression},globals())'.format(**locals())

class If(object):
	def __init__(self,condition, consequence, alternative):
		self.condition = condition
		self.consequence = consequence
		self.alternative = alternative
	
	def to_py(self):
		condition = self.condition.to_py()
		consequence = self.consequence.to_py()
		alternative = self.alternative.to_py()
		return 'if {condition} :\n    {consequence}\nelse:\n    {alternative}'.format(**locals())
	
class Sequence(object):
	def __init__(self, first, second):
		self.first = first
		self.second = second
	
	def to_py(self):
		first = self.first.to_py()
		second = self.second.to_py()
		return 	'{first}\n{second}'.format(**locals())		

class While(object):
	def __init__(self, condition, body):
		self.condition = condition
		self.body = body
		
	def to_py(self):
		condition = self.condition.to_py()
		body = self.body.to_py()
		return 'while{condition}:\n    {body}'.format(**locals())

proc = Number(5).to_py()
print(proc)
		
num = eval(proc,{})
print(num, end = '\n\n')

proc = Boolean(True).to_py()
print(proc)
thing = eval(proc,{})
print(thing, end = '\n\n')                                                                                                       

##变量表达式
proc = Variable('x').to_py()
print(proc)
var = eval(proc,{'x':7})
print(var, end = '\n\n')

##环境
environment = {'x':3}
print(environment, end = '\n\n')

##加法表达式
aaa = Add(Variable('x'), Number(1)).to_py()
print(aaa)
result = eval(aaa, environment)
print(result, end = '\n\n')

"""

class Machine(object):
	 virtual Machine 
	def __init__(self,expression, environment):
		self.expression = expression
		self.environment = environment
	
	def step(self):
		self.expression = self.expression.reduce(self.environment)
	
	def run(self):
		while self.expression.reducible():
			print(self.expression.to_s())
			self.step()
		print(self.expression.value)

statement = Sequence(
    Assign('x', Add(Number(1), Number(1))),
    Assign('y', Add(Variable('x'), Number(3)))
    )
print(statement.evaluate({}))
print(dict([(k, v.value) for k,v in statement.evaluate({}).items()]))

statement = While(
    LessThan(Variable('x'), Number(5)),
    Assign('x', Multiply(Variable('x'), Number(3)))
    )
	
print(statement.evaluate({'x': Number(1)}))
print(dict([(k, v.value) for k,v in statement.evaluate({'x': Number(1)}).items()]))

class Machine(object):
	def __init__(self,statement, environment):
		self.statement = statement
		self.environment = environment
	
	def step(self):
		self.statement, self.environment = self.statement.reduce(self.environment)
	
	def run(self):
		while self.statement.reducible():
			print(self.statement.to_s(), end=',')
			print(dict([(k,v.value) for k, v in self.environment.items()]))
			self.step()
		print(self.statement.to_s(), end=",")
		print(dict([(k,v.value) for k, v in self.environment.items()]))
		
		
Machine(
    If(
        Variable('x'),
        Assign('y', Number(1)),
        Assign('y', Number(2))
        ),
    {'x':Boolean(False)}
    ).run()
Machine( LessThan(Variable('x'), Number(5)),{'x':Number(1)}).run()		
"""