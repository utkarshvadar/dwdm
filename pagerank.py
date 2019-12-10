import pandas as pd
import numpy as np
import networkx as nx

edgelist = pd.read_csv('web-Stanford.txt',comment='#',delimiter = '\t').values[:50000,:]
matrix = nx.to_numpy_matrix(nx.from_edgelist(edgelist))

row,col = matrix.shape

ranks = np.ones((row,1))

itr = 4
outdegree = np.sum(matrix,axis = 1)
indegree = np.sum(matrix,axis=0)

d = 0.85
for i in range(itr):
	ranks = (1-d) + d*(np.divide(ranks,outdegree).T.dot(matrix))
	ranks = ranks.T
	
print("Ranks of the page are: ")

toprankid = ranks.T.argsort().A1
print("pageID\t\trank")
for i in toprankid[-10:][::-1]:
	print((i+1) ,"\t\t" ,ranks[i].A1[0])


