class Vertex:
    def __init__(self, n):
        self.name = n
        self.neighbors = []
        self.discovery = 0
        self.finish = 0
        self.color = 'black'

    def add_neighbor(self, v):
        if v not in self.neighbors:
            self.neighbors.append(v)
            self.neighbors.sort()

    def __repr__(self):
        return f"{self.name}: {self.neighbors} D:{self.discovery} F:{self.finish}"


class Graph:
    def __init__(self):
        self.vertices = {}
        self.time = 0

    def add_vertex(self, vertex):
        if isinstance(vertex, Vertex) and vertex.name not in self.vertices:
            self.vertices[vertex.name] = vertex
            return True
        return False

    def add_edge(self, u, v):
        if u in self.vertices and v in self.vertices:
            self.vertices[u].add_neighbor(v)
            self.vertices[v].add_neighbor(u)
            return True
        return False

    def get_vertex(self, name):
        return self.vertices.get(name)

    def get_discovery_finish(self):
        return {v.name: (v.discovery, v.finish) for v in self.vertices.values()}

    def dfs(self, start_vertex):
        if start_vertex.name not in self.vertices:
            raise ValueError("Start vertex not in graph")
        self.time = 1
        for v in self.vertices.values():
            v.color = 'black'
            v.discovery = 0
            v.finish = 0
        self._dfs(start_vertex)

    def _dfs(self, vertex):
        vertex.color = 'red'
        vertex.discovery = self.time
        self.time += 1
        for v_name in vertex.neighbors:
            neighbor = self.vertices[v_name]
            if neighbor.color == 'black':
                self._dfs(neighbor)
        vertex.color = 'blue'
        vertex.finish = self.time
        self.time += 1
