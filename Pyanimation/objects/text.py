import tkinter as tk

DeltColor = "#eb00c3"


class Text:
	def __init__(self,text,pos):
		self.text = text
		self.pos = pos

	def render(self,canvas):
		x,y = self.pos

		canvas.create_text(x,y,text = self.text,font = ("Arial",24),fill = DeltColor,anchor = "center")
		
