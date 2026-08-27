import math
import tkinter as tk
import time

TAU = math.pi * 2
DeltColor = "#eb00c3"


# Objects that can be rendered in Scene
class Line:
	'''	
	Parameters:
	---
	x1 : int
		the x-coordinate of the beginning of line

	y1 : int
		the y-coordinate of the beginning of line

	x2 : int
		the x-coordinate of the end of line

	y2 : int
		the y-coordinate of the end of line
	'''
	def __init__(self,x1,y1,x2,y2,color):
		self.x1 = x1
		self.y1 = y1
		self.x2 = x2
		self.y2 = y2
		self.color = color

	def render(self,canvas):
		canvas.create_line(self.x1,self.y1,self.x2,self.y2,fill = self.color,width = 3)

	def animate(self,canvas,steps):
		x_range = abs(self.x1 - self.x2)
		y_range = abs(self.y1 - self.y2)

		for i in range(steps + 1):
			canvas.create_line(self.x1,self.y1,self.x1 + x_range * i / steps,self.y1 + y_range * i / steps,fill = self.color,width = 3)

			canvas.update()
			time.sleep(0.001)

	def move(self,canvas,delta_x,delta_y,steps,i):
		canvas.create_line(self.x1 + delta_x * i / steps,self.y1 + delta_y * i / steps,self.x2 + delta_x * i / steps,self.y2 + delta_y * i / steps,fill = self.color,width = 3)

	def size(self,canvas,delta_size,steps,i):
		canvas.create_line(self.x1 + (delta_size / 2) * i / steps,self.y1 + (delta_size / 2) * i / steps,self.x2 + (delta_size / 2) * i / steps,self.y2 + (delta_size / 2) * i / steps,fill = self.color,width = 3)

	def particleAnimate(self,canvas,n,steps):
		x_range = abs(self.x1 - self.x2)
		y_range = abs(self.y1 - self.y2)

		for i in range(steps + 1):
			canvas.delete("all")
			canvas.create_oval(self.x1 + x_range * i / steps - 2,self.y1 + y_range * i / steps - 2,self.x1 + x_range * i / steps + 2,self.y1 + y_range * i / steps + 2,outline = self.color,fill = self.color,width = 3)

			canvas.update()
			time.sleep(0.001)


class Arc:
	'''
	Parameters:
	---
	r : float
		radius of the circle

	cen : tuple[float,float]
		(x,y) coordiates of the center of Arc rotation 

	start_ang : float
		rad at which the Arc begins

	ang : float
		rad angle that the Arc covers
	'''
	def __init__(self,r,cen,start_ang,ang,color):
		self.r = r
		self.cen = cen
		self.start_ang = start_ang
		self.ang = ang
		self.color = color

	def render(self,canvas):
		x,y = self.cen

		if self.ang >= TAU:
			canvas.create_oval(x - self.r,y - self.r,x + self.r,y + self.r,outline = self.color,width = 3)
		else:
			canvas.create_arc(x - self.r,y - self.r,x + self.r,y + self.r,start = math.degrees(self.start_ang),extent = math.degrees(self.ang),style = tk.ARC,outline = self.color,width = 3)

	def animate(self,canvas,steps):
		x,y = self.cen

		for i in range(steps + 1):
			canvas.create_arc(x - self.r,y - self.r,x + self.r,y + self.r,start = math.degrees(self.start_ang),extent = math.degrees(self.ang) * i / steps,style = tk.ARC,outline = self.color,fill = "black",width = 3)

			canvas.update()
			time.sleep(0.001)

	def move(self,canvas,delta_x,delta_y,steps,i):
		x,y = self.cen

		self.cen = (x + delta_x * i / 20, y + delta_y * i / 20)
			

	def size(self,canvas,delta_size,steps,i):
		r = self.r

		self.r = r + delta_size * i / steps

		self.render(canvas)


class Circle(Arc):
	'''
	Arc(r,cen,start_ang,ang = TAU)
	'''
	def __init__(self,r,cen,start_ang,color): 
		super().__init__(r = r,cen = cen,start_ang = start_ang,ang = TAU,color = color)


class SemiCircle(Arc):
	'''
	Arc(r,cen,start_ang,ang = TAU / 2)
	'''
	def __init__(self,r,cen,start_ang,color):
		super().__init__(r = r,cen = cen,start_ang = start_ang,ang = -(TAU / 2),color = color)


class Polygon:
	'''
	Parameters:
	---
	verticles : list[tuple[float,float]]
		a list of (x,y) coordinates for the Polygon vertices
	'''
	def __init__(self,vertices,color):
		self.vertices = vertices
		self.color = color

	def render(self,canvas):
		coords = [coord for vertex in self.vertices for coord in vertex]

		canvas.create_polygon(coords,outline = self.color,fill = "black",width = 3)

	def animate(self,canvas,steps):
		coords = []
		coords.extend(self.vertices[0])

		for i in range(len(self.vertices)):
			x1,y1 = self.vertices[i]
			x2,y2 = self.vertices[(i + 1) % len(self.vertices)]

			for j in range(steps + 1):
				alpha = j / steps

				cx = x1 + alpha * (x2 - x1)
				cy = y1 + alpha * (y2 - y1)

				canvas.delete("all")
				canvas.create_line(*(coords + [cx, cy]),fill = self.color,width = 3)

				canvas.update()
				time.sleep(0.001)

			coords.extend([x2, y2])
'''
	def move

	def size'''


class Rect(Polygon):
	'''
	Polygon([(x,y),(x + width,y),(x + width,y + height),(x,y + height)])
	'''
	def __init__(self,x,y,width,height,color):
		vertices = [(x,y),(x + width,y),(x + width,y + height),(x,y + height)]
		super().__init__(vertices,color = color)


class Square(Rect):
	'''
	Rect([(x,x),(x + width,x),(x + width,x + width),(x,x + width)])
	'''
	def __init__(self,x,width,color):
		super().__init__(x = x,y = x,width = width,height = width,color = color)