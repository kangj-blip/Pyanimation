import tkinter as tk

DeltColor = "#eb00c3"


class Text:
	def __init__(self,text,pos,color):
		self.text = text
		self.pos = pos
		self.color = color

	def render(self,canvas):
		x,y = self.pos

		canvas.create_text(x,y,text = self.text,font = ("Arial",24),fill = self.color,anchor = "center")
		
class LaTeX:
	def __init__(self,math,pos,color):
		self.math = math
		self.pos = pos
		self.color = color