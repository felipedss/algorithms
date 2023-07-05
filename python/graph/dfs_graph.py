from collections import defaultdict

class Graph: 

    def __init__(self):
        self.graph = defaultdict(list)

    def dfs_walk(self, start, visited):

        # Mark the current node as visited
        # and print it
        visited.add(start)
        print(start, end=" ")

        # Recur for all the vertices
        # adjacent to this vertex
        for neighbour in self.graph[start]:
            if neighbour not in visited:
                self.dfs_walk(neighbour, visited)

    def dfs(self, start):
        # Mark all the vertices as not visited
        visited = set()
        self.dfs_walk(start, visited)

    def add_edge(self, vertex1, vertex2):
        self.graph[vertex1].append(vertex2)




graph = Graph()

graph.add_edge(0, 1)
graph.add_edge(0, 2)
graph.add_edge(1, 2)
graph.add_edge(2, 0)
graph.add_edge(2, 3)
graph.add_edge(3, 3)

print("Following is Depth First Traversal (starting from vertex 2)")
print(graph.dfs(2))

