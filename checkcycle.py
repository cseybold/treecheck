import random
from random import sample

class Graph:
    def __init__(self, verts):
        self.verts = verts
        self.adj = {v: [] for v in verts}

    def add_edge(self, u, v):
        self.adj[u].append(v)
        self.adj[v].append(u)

    def is_tree(self):
        visited = set()
        parent = {v: None for v in self.verts}

        if self.has_cycle(self.verts[0], visited, parent):
            return False

        if len(visited) != len(self.verts):
            return False

        return True

    def has_cycle(self, v, visited, parent):
        visited.add(v)

        for neighbor in self.adj[v]:
            if neighbor not in visited:
                if self.has_cycle(neighbor, visited, parent):
                    return True
            elif parent[v] != neighbor:
                return True

        return False


g = Graph([1, 2, 3, 4, 5, 6, 7, 8])

for x in range(1,9):
    v1, v2 = random.sample(range(1, 9), 2)
    if v2 not in g.adj[v1]:
        g.add_edge(v1, v2)
            
for i in range(1,9):
    print (i, g.adj[i])

if g.is_tree():
    print("The graph is a tree")
else:
    print("The graph is not a tree")
