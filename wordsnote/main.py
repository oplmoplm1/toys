import tkinter as tk
from tkinter import *
from words import Words
class Frame:
	def __init__(self):
		self.top = tk.Tk()
		self.init_tk()
		self.top.mainloop()

	def update_index(self):
		self.index2 = self.index2+1
		if(self.index2>99):
			self.index2 = 0
			self.index1 = self.index1 +1
		return self.index1,self.index2
		
	def get_list(self,index):
		w = Words()
		w.get_list(index)
		self.list = w.get_list_content()
		return self.list

	def set_data(self):
		self.update_index()
		self.get_list(self.index1)
		self.word.set(self.list[self.index2][0])
		self.text.delete(0.0,END)
	
	def get_exp(self):
		self.text.insert(END,"\n".join(self.list[self.index2][1:]))
	
	def init_tk(self):
		self.index1 = 1
		self.index2 = 0
		self.top.geometry('600x400')
		self.word = StringVar()
		self.label = tk.Label(self.top,textvariable=self.word)
		self.label.pack()
		self.text = tk.Text(self.top)
		self.text.pack()
		self.button = tk.Button(self.top,text='Next',command=lambda:self.set_data())
		self.button.pack()
		tk.Button(self.top,text='Explaination',command=lambda:self.get_exp()).pack()

Frame()




