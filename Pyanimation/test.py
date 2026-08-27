import math

from engine import Engine
from objects.geometry import Line, Arc, Circle, Polygon, Rect, Square, SemiCircle
from objects.function import Graph, Function, Point
from objects.text import Text


#scene = Scene()
engine = Engine()
# end points are (0, ),(0,880)
# Middle is around (750,430)


# How to make a Circle (make ang negative to make the arc go clockwise)
circle = Circle(r = 300,cen = (750,430),start_ang = math.pi / 2,color = "white")
engine.animate(circle,steps = 20)

# How to move objects
engine.move(circle,20,-20,25)

# How to make a Rectangle
rect = Rect(100,50,200,100,"white")
engine.animate(rect,10)

# How to make a Square
sq = Square(100,50,"white")
engine.animate(sq,10)


# How to make a Graph and plot a Function
graph = Graph(origin = (110,710),x_range = (-5,10),y_range = (-5,10),x_length = 900,y_length = 500,x_name = "x-axis",y_name = "y-axis")
f = Function(graph = graph,func = lambda x: x,x_range = (0,10),n = 10,func_name = "f(x)",color = "white")
engine.render(graph)
engine.animate(f,30)

# How to display the Infimum and Supremum with division range n (from Function)
engine.funcInf(f)
engine.funcSup(f)

# How to add points onto graph
point1 = Point(graph = graph,x = 5,y = 5,name = "(5,5)",color = "white")
engine.render(point1)

# How to write Text
hello_world = Text(text = "Hello World",pos = (750,100))
engine.render(hello_world)
'''
# How to Group elements to move / transform them together
group = (graph,f,point1,hello_world)
group.groupRender()

# How to move Group
engine.move(group,20,20,30)
'''

engine.display()
