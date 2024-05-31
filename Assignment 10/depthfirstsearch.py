#Abhishek Subhash Swami 21 AIML
#Program for depth first search


#generate tree using dictionary 
tree={
    'A':['B','C','D'],
    'B':['E'],
    'C':['F','G'],
    'D':['H'],
    'E':['I','J'],
    'F':[],
    'G':[],
    'H':['K'],
    'I':[],
    'J':[],
    'K':[]
}

#create a set for storing visited node
visited=set()

#define a function dfs 

def dfs(tree,visited,node):
    if node not in visited:                     #check if node is visited or not
        print(node)
        visited.add(node)                       #add node to visited
        for neighbour in tree[node]:            #traverse neighbour 
            dfs(tree,visited,neighbour)         #call dfs recursively


#main
import time
start=time.time()
print("Folllowing is depth first search :\n")
dfs(tree,visited,'A')
end=time.time()
print("\ntime required is :",(end-start)*1000,"miliseconds")


#visualize a graph

# First networkx library is imported
# along with matplotlib
import networkx as nx
import matplotlib.pyplot as plt


# Defining a Class
class GraphVisualization:

	def __init__(self):
		self.visual = []
	def addEdge(self, a, b):
		temp = [a, b]
		self.visual.append(temp)
	def visualize(self):
		G = nx.Graph()
		G.add_edges_from(self.visual)
		nx.draw_networkx(G)
		plt.show()

G = GraphVisualization()
G.addEdge('A', 'B')
G.addEdge('A', 'C')
G.addEdge('A', 'D')
G.addEdge('B', 'E')
G.addEdge('C', 'F')
G.addEdge('C', 'G')
G.addEdge('D', 'H')
G.addEdge('E', 'I')
G.addEdge('E', 'J')
G.addEdge('H', 'K')

G.visualize()

