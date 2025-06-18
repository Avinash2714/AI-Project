# Graph represented as an adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'C', 'D'],
    'C': ['A', 'B', 'E'],
    'D': ['B', 'E'],
    'E': ['C', 'D']
}

# To store visited nodes
visitedNodes = []

# To store nodes in queue
queueNodes = []

# BFS function definition
def bfs(visitedNodes, graph, snode):
    visitedNodes.append(snode)
    queueNodes.append(snode)
    print("\nRESULT :")
    
    while queueNodes:
        s = queueNodes.pop(0)  # Dequeue a node
        print(s, end=" ")      # Process the node
        
        # Visit all adjacent nodes
        for neighbour in graph[s]:
            if neighbour not in visitedNodes:
                visitedNodes.append(neighbour)
                queueNodes.append(neighbour)

# Main Code
snode = input("Enter Starting Node (A, B, C, D, or E): ").upper()

# Check if input is valid
if snode in graph:
    bfs(visitedNodes, graph, snode)
else:
    print("Invalid starting node! Please enter A, B, C, D, or E.")
