import sys

class Vertex:
    def __init__(self, node):
        self.id = node
        self.adjacent = {}
        # Set distance to infinity for all nodes
        self.distance = sys.maxint
        # Mark all nodes unvisited        
        self.visited = False  
        # Predecessor
        self.previous = None

    def add_neighbor(self, neighbor, weight=0):
        self.adjacent[neighbor] = weight

    def get_connections(self):
        return self.adjacent.keys()  

    def get_id(self):
        return self.id

    def get_weight(self, neighbor):
        return self.adjacent[neighbor]

    def set_distance(self, dist):
        self.distance = dist

    def get_distance(self):
        return self.distance

    def set_previous(self, prev):
        self.previous = prev

    def set_visited(self):
        self.visited = True

    def __str__(self):
        return str(self.id) + ' adjacent: ' + str([x.id for x in self.adjacent])

class Graph:
    def __init__(self):
        self.vert_dict = {}
        self.num_vertices = 0

    def __iter__(self):
        return iter(self.vert_dict.values())

    def add_vertex(self, node):
        self.num_vertices = self.num_vertices + 1
        new_vertex = Vertex(node)
        self.vert_dict[node] = new_vertex
        return new_vertex

    def get_vertex(self, n):
        if n in self.vert_dict:
            return self.vert_dict[n]
        else:
            return None

    def add_edge(self, frm, to, cost = 0):
        if frm not in self.vert_dict:
            self.add_vertex(frm)
        if to not in self.vert_dict:
            self.add_vertex(to)

        self.vert_dict[frm].add_neighbor(self.vert_dict[to], cost)
        self.vert_dict[to].add_neighbor(self.vert_dict[frm], cost)

    def get_vertices(self):
        return self.vert_dict.keys()

    def set_previous(self, current):
        self.previous = current

    def get_previous(self, current):
        return self.previous

def shortest(v, path):
    ''' make shortest path from v.previous'''
    if v.previous:
        path.append(v.previous.get_id())
        shortest(v.previous, path)
    return

import heapq

def dijkstra(aGraph, start, target):
    print '''Dijkstra's shortest path'''
    # Set the distance for the start node to zero 
    start.set_distance(0)

    # Put tuple pair into the priority queue
    unvisited_queue = [(v.get_distance(),v) for v in aGraph]
    heapq.heapify(unvisited_queue)

    while len(unvisited_queue):
        # Pops a vertex with the smallest distance 
        uv = heapq.heappop(unvisited_queue)
        current = uv[1]
        current.set_visited()

        #for next in v.adjacent:
        for next in current.adjacent:
            # if visited, skip
            if next.visited:
                continue
            new_dist = current.get_distance() + current.get_weight(next)
            
            if new_dist < next.get_distance():
                next.set_distance(new_dist)
                next.set_previous(current)

        # Rebuild heap
        # 1. Pop every item
        while len(unvisited_queue):
            heapq.heappop(unvisited_queue)
        # 2. Put all vertices not visited into the queue
        unvisited_queue = [(v.get_distance(),v) for v in aGraph if not v.visited]
        heapq.heapify(unvisited_queue)

def AvRA(bGraph, members):
	m_size = len(members) 
	if m_size < 2:
		return
       # dijkstra(g, g.get_vertex('i'), g.get_vertex('h'))
        dijkstra(g, members[0], members[1])
        #target = g.get_vertex('h')
        target =  members[1]
        path = [target.get_id()]
        shortest(target, path)
    	tree_path = path[::-1]
	print tree_path	

	for i in range(3, m):
	    tree_path = Hook(tree_path, members[i])
	        
if __name__ == '__main__':

    g = Graph()

    g.add_vertex('a')
    g.add_vertex('b')
    g.add_vertex('c')
    g.add_vertex('d')
    g.add_vertex('e')
    g.add_vertex('f')
    g.add_vertex('g')
    g.add_vertex('h')
    g.add_vertex('i')
    g.add_vertex('j')
    g.add_vertex('k')
    g.add_vertex('l')
    g.add_vertex('m')

    g.add_edge('a', 'c', 1)
    g.add_edge('a', 'd', 1)
    g.add_edge('a', 'e', 1)
    g.add_edge('a', 'f', 1)
    g.add_edge('b', 'e', 1)
    g.add_edge('b', 'g', 1)
    g.add_edge('c', 'h', 1)
    g.add_edge('d', 'i', 1)
    g.add_edge('e', 'j', 1)
    g.add_edge('e', 'f', 1)
    g.add_edge('e', 'k', 1)
    g.add_edge('f', 'g', 1)
    g.add_edge('f', 'j', 1)
    g.add_edge('f', 'k', 1)
    g.add_edge('f', 'l', 1)
    g.add_edge('g', 'l', 1)
    g.add_edge('g', 'm', 1)
    g.add_edge('i', 'j', 1)

    members_nodes = [g.get_vertex('i'), g.get_vertex('h'), g.get_vertex('m')]
    AvRA(g, members_nodes)


