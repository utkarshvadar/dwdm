import pandas as pd
import numpy as np
import networkx as nx

edgelist = pd.read_csv('web-Stanford.txt',comment='#',delimiter = '\t').values[:50000,:]
matrix = nx.to_numpy_matrix(nx.from_edgelist(edgelist))
A = matrix
AT = matrix.T
row,col = matrix.shape

u = np.ones((row,1))

for i in range(4):
	v = AT.dot(u)
	u = A.dot(v)

topa = u.T.argsort().A1
print("Top 10 Authoritative")
for i in topa[-10:][::-1]:
	print((i+1) ,"\t\t" ,u[i].A1[0])

toph = v.T.argsort().A1
print("Top 10 Hubby")
for i in toph[-10:][::-1]:
	print((i+1) ,"\t\t" ,v[i].A1[0])




	




