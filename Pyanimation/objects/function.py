import math
import tkinter as tk
import time


class Graph:
	'''
	Parameters:
	---
	origin : tuple[int,int]
		(x,y) = (0,0) origin of graph

	x_range : tuple[int,int]
		(xmin,xmax) for the function

	y_range : tuple[int,int]
		(ymin,ymax) for the function

	x_length : tuple[int,int]
		x axis length of graph

	y_length : tuple[int,int]
		y axes length of graph
	'''
	def __init__(self,origin,x_range,y_range,x_length,y_length):
		self.origin = origin
		self.x_range = x_range
		self.y_range = y_range
		self.x_length = x_length
		self.y_length = y_length


	def points_to_coord(self,x,y):			# Conversion
		px,py = self.origin

		cx = px + ( x - self.x_range[0] ) / ( self.x_range[1] - self.x_range[0] ) * self.x_length
		cy = py - ( y - self.y_range[0] ) / ( self.y_range[1] - self.y_range[0] ) * self.y_length

		return cx,cy


	def draw(self,canvas):
		cx,cy = self.origin

		canvas.create_line(cx,cy,cx + self.x_length,cy,width = 3)		# x-axis
		canvas.create_line(cx,cy,cx,cy - self.y_length,width = 3)		# y-axis

class Function:
	def __init__(self,graph,func,x_range,size):
		self.graph = graph
		self.func = func
		self.x_range = x_range
		self.size = size

	def draw(self,canvas):
		coords = []
		xmin,xmax = self.x_range

		for i in range(self.size + 1):
			x = xmin + (xmax - xmin) * i / self.size
			y = self.func(x)

			cx,cy = self.graph.points_to_coord(x,y)

			coords.extend([cx,cy])

		canvas.create_line(*coords,width = 3)

	def animate(self,canvas):
		coords = []

		xmin,xmax = self.x_range

		for i in range(self.size + 1):
			x = xmin + (xmax - xmin) * i / self.size
			y = self.func(x)

			cx,cy = self.graph.points_to_coord(x,y)

			coords.extend([cx,cy])
			
			canvas.delete("all")
			self.graph.draw(canvas)

			if len(coords) >= 4:
				canvas.create_line(*coords,fill = "red",width = 3)

			canvas.update()
			time.sleep(0.005)