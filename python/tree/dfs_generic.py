
class Tree: 

    def __init__(self):
        self.graph = {} 

    
    def dfs(self, start, target, visited=None):

        if visited is None:
           visited = set()
        else:
            if start in visited:
                return False

        visited.add(start)

        if start == target:
            return True

        for neighbor in self.graph.get(start, []): # caso não exista retornará uma lista vazia aqui
            if self.dfs(neighbor, target, visited):
                return True
        
        return False

    def add_edge(self, vertex1, vertex2):
        if vertex1 in self.graph:
            self.graph[vertex1].append(vertex2)
        else:
            self.graph[vertex1] = [vertex2]        


tree = Tree()

tree.add_edge('A', 'B')
tree.add_edge('A', 'C')
tree.add_edge('B', 'D')
tree.add_edge('B', 'E')
tree.add_edge('C', 'F')
tree.add_edge('E', 'F')

print(tree.dfs('A', 'F')) # True
print(tree.dfs('B', 'G')) # False
