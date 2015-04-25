import re

class Words:
	words_p = re.compile(r"\[*\]")
	explain_p =re.compile(r"【")
	words_list = []
	def __init__(self):
		pass
		
	def get_one(self):
		while(self.fp.readable()): 
			line = self.fp.readline()
			if(line== ""):
				break
			if(self.words_p.search(line)!= None):
				self.words_list.append([line])
				return line
			elif(len(self.words_list)!=0):
				if(self.explain_p.search(line)!=None):
					self.words_list[-1].append(line)
		return None
		
	def fill_list(self):
		i = 0
		max=100
		self.words_list = []
		one = self.get_one()
		while(one!=None):
			if(i>max):
				break
			one = self.get_one()
			i = i+1
	
	def get_list(self,index=1):
		self.fp = open("words.txt","r",encoding="utf-8")
		for i in range(0,index):
			self.fill_list()
		self.fp.close();
	
	
	def get_list_content(self,index=-1):
		if(index==-1):
			return self.words_list
		return self.words_list[index]

