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
	x1 : float
		x-coordinate of the beginning of Line

	y1 : float
		y-coordinate of the beginning of Line

	x2 : float
		x-coordinate of the end of Line

	y2 : float
		y-coordinate of the end of Line

	color : string
		color of Line
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
		x_range = abs(self.x2 - self.x1)
		y_range = abs(self.y2 - self.y1)

		for i in range(steps + 1):
			canvas.delete("all")
			canvas.create_line(self.x1,self.y1,self.x1 + x_range * i / steps,self.y1 + y_range * i / steps,fill = self.color,width = 3)

			canvas.update()
			time.sleep(0.001)

	def move(self,canvas,delta_x,delta_y,steps,i):
		canvas.create_line(self.x1 + delta_x * i / steps,self.y1 + delta_y * i / steps,self.x2 + delta_x * i / steps,self.y2 + delta_y * i / steps,fill = self.color,width = 3)

	def size(self,canvas,delta_size,steps,i):
		canvas.create_line(self.x1 + (delta_size / 2) * i / steps,self.y1 + (delta_size / 2) * i / steps,self.x2 + (delta_size / 2) * i / steps,self.y2 + (delta_size / 2) * i / steps,fill = self.color,width = 3)

	def particleAnimate(self,canvas,steps):
		x_range = self.x2 - self.x1
		y_range = self.y2 - self.y1

		particles = []

		for i in range(steps + 1):
			canvas.delete("all")

			if i % 20 == 0:
				particles.append(0)

			for j in range(len(particles)):
				progress = particles[j]

				canvas.create_oval(self.x1 + x_range * progress - 2,self.y1 + y_range * progress - 2,self.x1 + x_range * progress + 2,self.y1 + y_range * progress + 2,outline = self.color,fill = self.color,width = 3)
				particles[j] += 1 / steps

				particles[j] += 0.001

			particles = [p for p in particles if p <= 1]

			canvas.update()
			time.sleep(0.001)


class Arc:
	'''
	Parameters:
	---
	r : float
		radius of the Arc

	cen : tuple[float,float]
		(x,y) coordiates of the center of Arc rotation 

	start_ang : float
		RAD at which the Arc begins

	ang : float
		RAD that the Arc covers

	color : string
		color of Arc outline

	fill : string
		color of Arc fill IF self.ang = TAU (full circle)
		during animate, the fill is only done AFTER the animation of the outline
		IF you want an "empty" Circle, set fill = "black"
	'''
	def __init__(self,r,cen,start_ang,ang,color,fill):
		self.r = r
		self.cen = cen
		self.start_ang = start_ang
		self.ang = ang
		self.color = color
		self.fill = fill

	def render(self,canvas):
		x,y = self.cen

		if self.ang >= TAU:
			canvas.create_oval(x - self.r,y - self.r,x + self.r,y + self.r,outline = self.color,fill = self.fill,width = 3)
		else:
			canvas.create_arc(x - self.r,y - self.r,x + self.r,y + self.r,start = math.degrees(self.start_ang),extent = math.degrees(self.ang),style = tk.ARC,outline = self.color,width = 3)

	def animate(self,canvas,steps):
		x,y = self.cen

		for i in range(steps + 1):
			canvas.delete("all")
			canvas.create_arc(x - self.r,y - self.r,x + self.r,y + self.r,start = math.degrees(self.start_ang),extent = math.degrees(self.ang) * i / steps,style = tk.ARC,outline = self.color,fill = '',width = 3)

			canvas.update()
			time.sleep(0.001)

	def move(self,canvas,delta_x,delta_y,steps,i):
		x,y = self.cen

		next_x = x + delta_x * i / steps
		next_y = y + delta_y * i / steps

		if self.ang >= TAU:
			canvas.create_oval(next_x - self.r,next_y - self.r,next_x + self.r,next_y + self.r,outline = self.color,fill = self.fill,width = 3)
		else:
			canvas.create_arc(next_x - self.r,next_y - self.r,next_x + self.r,next_y + self.r,start = math.degrees(self.start_ang),extent = math.degrees(self.ang),style = tk.ARC,outline = self.color,width = 3)

	def size(self,canvas,delta_size,steps,i):
		r = self.r
		self.r = r + delta_size * i / steps

		self.render(canvas)
'''
	def particleAnimate(self,canvas,steps):	
		x,y = self.cen

		particles = []

		for i in range(steps + 1):
			canvas.delete("all")

			if i % 20 == 0:
				particles.append(0)

			for j in range(len(particles)):
				progress = particles[j]

				canvas.create_oval(x - self.r + x_range * progress - 2,self.y1 + y_range * progress - 2,self.x1 + x_range * progress + 2,self.y1 + y_range * progress + 2,outline = self.color,fill = self.color,width = 3)
				particles[j] += 1 / steps

				particles[j] += 0.001

			particles = [p for p in particles if p <= 1]

			canvas.update()
			time.sleep(0.001)

'''
class Circle(Arc):
	'''
	Arc(r,cen,start_ang,ang = -TAU,color,fill)

	Parameters:
	---
	'''
	def __init__(self,r,cen,start_ang,color,fill): 
		super().__init__(r = r,cen = cen,start_ang = start_ang,ang = TAU,color = color,fill = fill)


class SemiCircle(Arc):
	'''
	Arc(r,cen,start_ang,ang = -(TAU / 2),color,fill)

	Parameters:
	---
	'''
	def __init__(self,r,cen,start_ang,color):
		super().__init__(r = r,cen = cen,start_ang = start_ang,ang = (TAU / 2),color = color,fill = "black")


class Polygon:
	'''
	Parameters:
	---
	verticles : list[tuple[float,float]]
		a list of (x,y) coordinates for the Polygon vertices

	color : string
		color of Polygon outline

	fill : string
		color of Polygon fill 
		during animate, the fill is only done AFTER the animation of the outline
		IF you want an "empty" Polygon, set fill = "black"
	'''
	def __init__(self,vertices,color,fill):
		self.vertices = vertices
		self.color = color
		self.fill = fill

	def render(self,canvas):
		coords = [coord for vertex in self.vertices for coord in vertex]

		canvas.create_polygon(coords,outline = self.color,fill = self.fill,width = 3)

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

		canvas.create_polygon(coords,outline = self.color,fill = self.fill,width = 3)

	def move(self,canvas,delta_x,delta_y,steps,i):
		coords = []

		for vertex in self.vertices:
			x = vertex[0] + delta_x * i / steps
			y = vertex[1] + delta_y * i / steps

			coords.extend([x,y])

		canvas.create_polygon(coords,outline = self.color,fill = self.fill,width = 3)
'''
	def size(self,canvas,delta_size,steps,i):
		

'''


class Rect(Polygon):
	'''
	Polygon([(x,y),(x + width,y),(x + width,y + height),(x,y + height)],color,fill)

	Parameters:
	---
	x : float
		x-coordinate of top-left corner of the Rect

	y : float
		y-coordinate of top-left corner of the Rect

	width : float
		width of Rect

	height : float
		height of Rect

	color : string
		color of Rect outline

	fill : string
		color of Rect fill 
		during animate, the fill is only done AFTER the animation of the outline
		IF you want an "empty" Rect, set fill = "black"
	'''
	def __init__(self,x,y,width,height,color,fill):
		vertices = [(x,y),(x + width,y),(x + width,y + height),(x,y + height)]
		super().__init__(vertices,color = color,fill = fill)


class Square(Rect):
	'''
	Rect(x,x,width,width,color,fill)
	Polygon([(x,y),(x + width,y),(x + width,y + width),(x,y + width)],color,fill)

	Parameters:
	---
	x : float
		x-coordinate of top-left corner of the Square

	y : float
		y-coordinate of top-left corner of the Square

	width : float
		width of Square

	color : string
		color of Rect outline

	fill : string
		color of Square fill 
		during animate, the fill is only done AFTER the animation of the outline
		IF you want an "empty" Square, set fill = "black"
	'''
	def __init__(self,x,y,width,color,fill):
		super().__init__(x = x,y = y,width = width,height = width,color = color,fill = fill)


class EqTriangle(Polygon):
	'''
	Polygon([(x,y),(x + (width / 2),y - height),(x - (width / 2),y - height)],color,fill)

	Parameters:
	---

	'''
	def __init__(self,x,y,height,width,color,fill):
		vertices = [(x,y),(x + (width / 2),y + height),(x - (width / 2),y + height)]
		super().__init__(vertices,color = color,fill = fill)





