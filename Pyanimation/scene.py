class Scene:
	def __init__(self):
		self.objects = []

	def addObj(self,obj):
		self.objects.append(obj)

	def removeObj(self,obj):
		self.objects.remove(obj)

	def clear(self):
		self.objects.clear()