"""
Created on Wed Feb 28 16:06:11 2018

@author: w7
"""


import snap
import numpy as np
from scipy import linalg as la

def calculate_eigen():
	A=np.array([[5,-3,3],
			   [4,-2,3],
			   [4,-4,5]])

	e_vals, e_vecs = la.eig(A)

	print(e_vals.astype(float))
	A=np.array([[0,1,0],
			   [1,0,1],
			   [0,1,0]])

	e_vals, e_vecs = la.eig(A)

	print(e_vals)

calculate_eigen()
# create a graph PNGraph
G1 = snap.TNGraph.New()
G1.AddNode(1)
G1.AddNode(5)
G1.AddNode(32)
G1.AddEdge(1,5)
G1.AddEdge(5,1)
G1.AddEdge(5,32)




