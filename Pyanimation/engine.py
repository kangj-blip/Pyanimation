import tkinter as tk


class Engine:
	def __init__(self,width = 3840,height = 2160):
		self.root = tk.Tk()
		self.canvas = tk.Canvas(self.root,width = width,height = height,background = "black")
		self.canvas.pack()
		self.root.title("Subcribe to Delta mv")

	# Renders
	def render(self,obj):
		obj.render(self.canvas)

	def animate(self,obj,steps):
		obj.animate(self.canvas,steps)


	# Function Renders
	def funcInf(self,func):
		func.infimum(self.canvas)

	def funcSup(self,func):
		func.supremum(self.canvas)


	# tranformers
	def move(self,obj,delta_x,delta_y,steps):
		obj.move(self.canvas,delta_x,delta_y,steps)

	def size(self,obj,delta_size,steps):
		obj.size(self.canvas,delta_size,steps)


	# Group Activity
	def groupRender(self,objects):
		for obj in objects:
			obj.render(self.canvas)

	def groupAnimate(self,objects):
		for obj in objects:
			obj.animate(self.canvas)

	def groupMove(self,objects,delta_x,delta_y,steps):
		for obj in objects:
			obj.move(self.canvas,delta_x,delta_y,steps)

	def groupSize(self,objects,delta_size,steps):
		for obj in objects:
			obj.size(self.canvas,delta_size,steps)





	def display(self):
		self.root.mainloop()