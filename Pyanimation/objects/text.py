import tkinter as tk


class Text:
	def __init__(self,text,origin):
		self.text = text
		self.origin = origin

	def draw(self,canvas):
		x,y = self.origin

		canvas.create_text(x,y,text = self.text,font = ("Ariel",24),fill = "red",anchor = "center")
		
