import tkinter as tk


class Engine:
	def __init__(self,width = 1200,height = 800):
		self.root = tk.Tk()
		self.canvas = tk.Canvas(self.root,width = width,height = height)
		self.canvas.pack()

	def render(self,obj):
		obj.draw(self.canvas)

	def aniRender(self,obj):
		obj.animate(self.canvas)




	def display(self):
		self.root.mainloop()
