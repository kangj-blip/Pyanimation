import math
import tkinter as tk
import time

DeltColor = "#eb00c3"


class Graph:
	'''
	Parameters:
	---
	origin : tuple[int,int]
		(x,y) pixel position of origin (0,0) of graph

	x_range : tuple[int,int]
		(xmin,xmax) range for the graph

	y_range : tuple[int,int]
		(ymin,ymax) range for the graph

	x_length : tuple[int,int]
		x-axis length of graph on screen (pixels)

	y_length : tuple[int,int]
		y-axes length of graph on screen (pixels)
	'''
	def __init__(self,origin,x_range,y_range,x_length,y_length,x_name,y_name):
		self.origin = origin
		self.x_range = x_range
		self.y_range = y_range
		self.x_length = x_length
		self.y_length = y_length
		self.x_name = x_name
		self.y_name = y_name

	def points_to_coord(self,x,y):			# Conversion
		ox,oy = self.origin

		cx = ox + ( x - self.x_range[0] ) / ( self.x_range[1] - self.x_range[0] ) * self.x_length
		cy = oy - ( y - self.y_range[0] ) / ( self.y_range[1] - self.y_range[0] ) * self.y_length

		return cx,cy

	def render(self,canvas):
		ox,oy = self.points_to_coord(0,0)

		cx_min,_ = self.points_to_coord(self.x_range[0], 0)
		cx_max,_ = self.points_to_coord(self.x_range[1], 0)
		_,cy_min = self.points_to_coord(0, self.y_range[0])
		_,cy_max = self.points_to_coord(0, self.y_range[1])

		canvas.create_line(cx_min,oy,cx_max,oy,width = 3)			# x-axis 
		canvas.create_line(ox,cy_min,ox,cy_max,width = 3)			# y-axis 

		canvas.create_text(cx_max + 50,oy,text = self.x_name,font = ("Ariel",24),fill = DeltColor)
		canvas.create_text(ox,cy_max - 20,text = self.y_name,font = ("Ariel",24),fill = DeltColor)

	def move(self,canvas,delta_x,delta_y,steps):
		ox,oy = self.origin

		cx_min,_ = self.points_to_coord(self.x_range[0], 0)
		cx_max,_ = self.points_to_coord(self.x_range[1], 0)
		_,cy_min = self.points_to_coord(0, self.y_range[0])
		_,cy_max = self.points_to_coord(0, self.y_range[1])

		for i in range(steps + 1):
			'''	
			canvas.create_line(cx_min + delta_x * i / steps,oy + ,cx_max + delta_x * i / steps,oy,oy,width = 3)			# x-axis 
			canvas.create_line(ox,cy_min + delta_y * i / steps,oy,ox,cy_max + delta_y * i / steps,oy,width = 3)			# y-axis 
			'''
			canvas.delete("all")
			self.render(canvas)

			canvas.update()
			time.sleep(0.001)



class Function:
	'''
	Parameters:
	---
	graph : Graph(origin,x_range,y_range,x_length,y_length,x_name,y_name)
		the graph on which this function is drawn on

	func : f(x)
		a function

	x_range : tuple[int,int]
		(xmin,xmax) length for the function (same as x_range from its graph)

	n : int
		the number of division you want if showing Infinimum or supremum

	func_name : string
		name of the function shown at the end of the function

	color : string
		color of function and function name
	'''
	def __init__(self,graph,func,x_range,n,func_name,color):
		self.graph = graph
		self.func = func
		self.x_range = x_range
		self.n = n
		self.func_name = func_name
		self.color = color

	def render(self,canvas):
		coords = []
		xmin,xmax = self.x_range

		for i in range(steps + 1):
			x = xmin + (xmax - xmin) * i / steps
			y = self.func(x)

			cx,cy = self.graph.points_to_coord(x,y)

			coords.extend([cx,cy])

		canvas.create_line(*coords,fill = self.color,width = 3)

		cx = coords[-2]
		cy = coords[-1]

		canvas.create_text(cx + 30,cy - 30,text = self.func_name,font = ("Ariel",24),fill = self.color)

	def animate(self,canvas,steps):
		coords = []
		xmin,xmax = self.x_range

		for i in range(steps + 1):
			x = xmin + (xmax - xmin) * i / steps
			y = self.func(x)

			cx,cy = self.graph.points_to_coord(x,y)

			coords.extend([cx,cy])
			
			canvas.delete("all")
			self.graph.render(canvas)

			if len(coords) >= 4:
				canvas.create_line(*coords,fill = self.color,width = 3)

			canvas.update()
			time.sleep(0.001)

			canvas.create_text(cx + 50,cy,text = self.func_name,font = ("Arial",24),fill = self.color)

	def infimum(self,canvas):
		xmin,xmax = self.x_range
		limit_range = (xmax - xmin) / self.n

		for i in range(self.n):
			x = xmin + i * limit_range
			y = self.func(x)

			x1,y1 = self.graph.points_to_coord(x,0)
			x2,y2 = self.graph.points_to_coord(x + limit_range,y)

			cx,cy = self.graph.points_to_coord(x,y)

			canvas.create_polygon(x1,y1,x1,y2,x2,y2,x2,y1,outline = "blue",fill = '',width = 3)

	def supremum(self,canvas):
		xmin,xmax = self.x_range
		limit_range = (xmax - xmin) / self.n

		for i in range(self.n):
			x = xmax - i * limit_range
			y = self.func(x)

			x1,y1 = self.graph.points_to_coord(x,0)
			x2,y2 = self.graph.points_to_coord(x - limit_range,y)

			cx,cy = self.graph.points_to_coord(x,y)

			canvas.create_polygon(x1,y1,x1,y2,x2,y2,x2,y1,outline = "red",fill = '',width = 3)

'''	def move(self,canvas):
		coords = []
		xmin,xmax = self.x_range

		#for i in range(steps + 1):


'''

class Point:
	'''
	Parameters:
	---
	graph : Graph(origin,x_range,y_range,x_length,y_length,x_name,y_name)
		the graph on which this point is drawn on
	
	x : int
		the x-coordinate of the point

	y : int
		the y-coordinate of the point

	name : string
		name/label of the point

	color : string
		color of point and label
	'''
	def __init__(self,graph,x,y,name,color):
		self.graph = graph
		self.x = x
		self.y = y
		self.name = name
		self.color = color

	def render(self,canvas):
		cx,cy = self.graph.points_to_coord(self.x,self.y)

		canvas.create_oval(cx - 2,cy - 2,cx + 2,cy + 2,outline = self.color,fill = self.color,width = 3)
		canvas.create_text(cx + 20,cy + 20,text = self.name,font = ("Arial",24),fill = self.color,anchor = "center")

