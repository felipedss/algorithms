from collections import defaultdict

class Graph:

    def __init__(self):
        self.graph = defaultdict(list)

    # Function to add an edge to graph
    def add_edge(self, vertex1, vertex2):
        # Default dictionary to store graph
        self.graph[vertex1].append(vertex2)

    def bfs(self, node):

        # Mark all the vertices as not visited
        visited = [False] * (max(self.graph) + 1)        

        # Create a queue for BFS
        queue = []

        # Mark the source node as
        # visited and enqueue it
        queue.append(node)
        visited[node] = True

        while queue:

            # Dequeue a vertex from
            # queue and print it
            node = queue.pop(0)
            print(node, end=" ")

            for i in self.graph[node]:
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True


graph = Graph()
graph.add_edge(0, 1)
graph.add_edge(0, 2)
graph.add_edge(1, 2)
graph.add_edge(2, 0)
graph.add_edge(2, 3)
graph.add_edge(3, 3)

print(graph.graph)

print("Following is Breadth First Traversal"
        " (starting from vertex 2)")
graph.bfs(2)


