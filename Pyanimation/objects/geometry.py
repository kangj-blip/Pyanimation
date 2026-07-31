import math
import tkinter as tk
import time


TAU = math.pi * 2

# Objects that can be rendered in Scene
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
	def __init__(self,r,cen,start_ang,ang):
		self.r = r
		self.cen = cen
		self.start_ang = start_ang
		self.ang = ang

		self.visible_fraction = 1.0

	def draw(self,canvas):
		x,y = self.cen

		canvas.create_arc(x-self.r,y-self.r,x+self.r,y+self.r,start = math.degrees(self.start_ang),extent = math.degrees(self.ang),style = tk.ARC,outline = "red",width = 3)

	def animate(self,canvas):
		x,y = self.cen

		for i in range(101):
			canvas.delete("all")

			canvas.create_arc(x-self.r,y-self.r,x+self.r,y+self.r,start = math.degrees(self.start_ang),extent = math.degrees(self.ang) * i / 100,style = tk.ARC,outline = "red",width = 3)

			canvas.update()
			time.sleep(0.005)


class Circle(Arc):
	'''
	Arc(r,cen,start_ang,ang = 360)
	'''
	def __init__(self,r,cen):   	# What you'd like the User to input about Circle
		super().__init__(
			r = r,
			cen = cen,
			start_ang = 0,
			ang = TAU,				# Inherited from Arc
		)							# No need for draw()



class Polygon:
	'''
	Parameters:
	---
	verticles : list[tuple[float,float]]
		a list of (x,y) coordinates for the Polygon vertices
	'''
	def __init__(self,vertices):
		self.vertices = vertices

	def draw(self,canvas):
		coords = [coord for vertex in self.vertices for coord in vertex]

		canvas.create_polygon(coords,outline = "red",fill = '',width = 3)

	def animate(self,canvas):
		coords = []
		coords.extend(self.vertices[0])

		steps = 30

		for i in range(len(self.vertices)):
			x1,y1 = self.vertices[i]
			x2,y2 = self.vertices[(i + 1) % len(self.vertices)]

			for j in range(steps + 1):
				alpha = j / steps

				cx = x1 + alpha * (x2 - x1)
				cy = y1 + alpha * (y2 - y1)

				canvas.delete("all")

				canvas.create_line(*(coords + [cx, cy]),fill = "red",width = 3)

				canvas.update()
				time.sleep(0.005)

			coords.extend([x2, y2])


class Rect(Polygon):
	'''
	Polygon([(x1,y1),(x2,y2),(x3,y3),(x4,y4)])
	'''
	def __init__(self,x,y,width,height):
		vertices = [(x,y),(x+width,y),(x+width,y+height),(x,y+height)]
		super().__init__(vertices)