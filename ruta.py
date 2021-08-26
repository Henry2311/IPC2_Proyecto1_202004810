class Vertice:	
	def __init__(self, i):
		self.id = i
		self.vecinos = []
		self.visitado = False
		self.padre = None
		self.costo = float('inf')

	def agregarVecino(self, v, p):
		
		if v not in self.vecinos:
			self.vecinos.append([v, p])

class Camino:
	def __init__(self):
		self.vertices = {}

	def agregarVertice(self, id):
		if id not in self.vertices:
			self.vertices[id] = Vertice(id)

	def agregarArista(self, a, b, p):
		if a in self.vertices and b in self.vertices:
			self.vertices[a].agregarVecino(b, p)
			self.vertices[b].agregarVecino(a, p)		
	
	def camino(self, a, b):
		camino = []
		actual = b
		while actual != None:
			camino.insert(0, actual)
			actual = self.vertices[actual].padre
		#return [camino, self.vertices[b].costo]
		return camino

	def minimo(self, l):
		if len(l) > 0:
			m = self.vertices[l[0]].costo
			v = l[0]
			for e in l:
				if m > self.vertices[e].costo:
					m = self.vertices[e].costo
					v = e
			return v
		return None

	def dijkstra(self, a):
		if a in self.vertices:
			self.vertices[a].costo = 0
			actual = a
			noVisitados = []
			
			for v in self.vertices:
				if v != a:
					self.vertices[v].costo = float('inf')
				self.vertices[v].padre = None
				noVisitados.append(v)

			while len(noVisitados) > 0:
		
				for vec in self.vertices[actual].vecinos:
					if self.vertices[vec[0]].visitado == False:
						if self.vertices[actual].costo + vec[1] < self.vertices[vec[0]].costo:
							self.vertices[vec[0]].costo = self.vertices[actual].costo + vec[1]
							self.vertices[vec[0]].padre = actual

				self.vertices[actual].visitado = True
				noVisitados.remove(actual)

				actual = self.minimo(noVisitados)
		else:
			return False


