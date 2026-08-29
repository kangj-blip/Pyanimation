import tkinter as tk
import time
import os
import subprocess
import shutil

class Engine:
	def __init__(self,width = 3840,height = 2160):
		self.root = tk.Tk()
		self.canvas = tk.Canvas(self.root,width = width,height = height,background = "black")
		self.canvas.pack()
		self.root.title("Subcribe to Delta mv")

		self.recording = False
		self.frame = 0
		self.frame_dir = "frames"


	# Recording
	def record(self):
		if os.path.exists(self.frame_dir):
			shutil.rmtree(self.frame_dir)

		os.makedirs(self.frame_dir)

		self.recording = True
		self.frame = 0

		print("recording...")

	def eachFrame(self):
		if not self.record:
			return

		self.root.update_idletasks()

		ps_file = os.path.join(self.frame_dir,f"frame_{self.frame:06d}.ps")

		ps_png = os.path.join(self.frame_dir,f"frame_{self.frame:06d}.png")


	# Renders
	def render(self,obj):
		'''
		Simple render of object
		DONE : Line, Arc (checked for Circle, SemiCircle), Polygon (checked for Rect, Square), Graph, Function, Point, Text
		'''
		obj.render(self.canvas)

	def animate(self,obj,steps):
		'''
		Animated render of object
		DONE : Line, Arc (checked for Circle #ISSUE), Polygon (checked for Rect, Square), Graph, Function (checked for func = lambda x: x)
		IN PROGRESS : Text
		MISSING : Point
		'''
		obj.animate(self.canvas,steps)

	def particleAnimate(self,obj,steps):
		'''
		Animation of particle movement along outline of object
		DONE : Line
		IN PROGRESS : Arc, Polygon, Func
		MISSING : Graph, Point, Text
		'''
		obj.particleAnimate(self.canvas,steps)


	# Function Renders
	def funcInf(self,func):
		func.infimum(self.canvas)

	def funcSup(self,func):
		func.supremum(self.canvas)


	# tranformers
	def move(self,obj,delta_x,delta_y,steps):
		'''
		Simple movement of object from original render, to x-axis change of delta_x, y-axis change of delta_y
		DONE : Line, Arc (checked for Circle), Polygon (checked for EqTriangle)
		IN PROGRESS : Graph, Function, Point, Text
		'''
		for i in range(steps + 1):
			self.canvas.delete("all")
			obj.move(self.canvas,delta_x,delta_y,steps,i)

			self.canvas.update()
			time.sleep(0.001)

	def size(self,obj,delta_size,steps):
		'''
		Simple resize of object from original render, to size change of delta_size
		DONE : Arc (checked for Circle)
		IN PROGRESS : Line, Polygon, Graph, Function, Point, Text
		'''
		for i in range(steps + 1):
			self.canvas.delete("all")
			obj.size(self.canvas,delta_size,steps,i)

			canvas.update()
			time.sleep(0.001)


	# Group Activity
	def groupRender(self,objects):
		for obj in objects:
			obj.render(self.canvas)

	def groupAnimate(self,objects):
		for obj in objects:
			obj.animate(self.canvas)

	def groupMove(self,objects,delta_x,delta_y,steps):
		for i in range(steps + 1):
			self.canvas.delete("all")

			for obj in objects:
				obj.move(self.canvas,delta_x,delta_y,steps,i)

			self.canvas.update()
			time.sleep(0.001)

	def groupSize(self,objects,delta_size,steps):
		for i in range(steps + 1):
			self.canvas.delete("all")

			for obj in objects:
				obj.size(self.canvas,delta_size,steps,i)

			self.canvas.update()
			time.sleep(0.001)




	def display(self):
		self.root.mainloop()
