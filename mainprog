class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.adj_list = {v: [] for v in vertices}

    def add_edge(self, u, v):
        self.adj_list[u].append(v)
        self.adj_list[v].append(u)

    def is_tree(self):
        visited = set()
        parent = {v: None for v in self.vertices}

        # Check for cycles using depth-first search
        if self.has_cycle(self.vertices[0], visited, parent):
            return False

        # Check if all vertices are visited
        if len(visited) != len(self.vertices):
            return False

        return True

    def has_cycle(self, v, visited, parent):
        visited.add(v)

        for neighbor in self.adj_list[v]:
            if neighbor not in visited:
                if self.has_cycle(neighbor, visited, parent):
                    return True
            elif parent[v] != neighbor:
                return True

        return False


# Example usage
g = Graph([1, 2, 3, 4, 5])
g.add_edge(1, 2)
g.add_edge(1, 3)
g.add_edge(2, 4)
g.add_edge(3, 5)

if g.is_tree():
    print("The graph is a tree")
else:
    print("The graph is not a tree")
