import math

from scene import Scene
from objects.geometry import Arc, Circle, Polygon, Rect
from objects.function import Graph, Function
from objects.text import Text
from engine import Engine


scene = Scene()
engine = Engine()

# Middle is around (600,400)

'''
circle = Circle(300, (600,400))
scene.addObj(circle)
engine.aniRender(circle)

rect = Rect(100, 50, 200, 100)
scene.addObj(rect)
engine.aniRender(rect)


graph = Graph(origin = (100,700),x_range = (-5,5),y_range = (0,10),x_length = 900,y_length = 500)
f = Function(graph = graph,func = lambda x: x**2,x_range = (-5,5),size = 300)
engine.render(graph)
engine.aniRender(f)
'''


hello_world = Text("Hello World",(600,400))
engine.render(hello_world)

engine.display()
