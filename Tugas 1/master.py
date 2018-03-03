"""
Created on Wed Feb 28 16:06:11 2018

@author: w7
"""


import snap
import numpy as np
from scipy import linalg as la
from collections import OrderedDict

def CalculateEigenVectorCentr(graph):
	output={}
	NIdEigenH = snap.TIntFltH()
	snap.GetEigenVectorCentr(graph, NIdEigenH)
	
	for item in NIdEigenH:
		#print "node: %d have centrality: %f" % (item, NIdEigenH[item])
		output[item]=NIdEigenH[item]
	return output
		
def CalculatePageRank(graph,alpha,number_iteration):
	PRankH=snap.TIntFltH()
	snap.GetPageRank(graph,PRankH,alpha, 1e-4, number_iteration)
	output={}
	for item in PRankH:
		output[item]=PRankH[item]
	return output
def transverse_graph(graph):
	for NI in graph.Nodes():
		print "node: %d, degree %d" % ( NI.GetId(), NI.GetDeg())
		for br in NI.GetOutEdges():
			print br

#------------------ CREATING GRAPH from .edges file--------------------------------------
file=open("facebook/0.edges","r")
lines=file.readlines()
G1 = snap.TUNGraph.New()
for line in lines:
	line=line.strip("\n")
	line=map(int,line.split(" "))
	if not G1.IsNode(line[0]):
		G1.AddNode(line[0])
	if not G1.IsNode(line[1]):
		G1.AddNode(line[1])
	if not G1.IsEdge(line[0],line[1]):
		G1.AddEdge(line[0],line[1])
#transverse_graph(G2)
#------------------------------------------------------------------------------------------------
#------------------ FIND 5 GREATEST CENTRALITY BASED ON EIGENVECTOR-----------
ce=CalculateEigenVectorCentr(G1)
#Sorting DSC the ce(Centrality Eigenvector)
ce=OrderedDict(sorted(ce.items(),key=lambda x:x[1],reverse=True))
print "5 Greatest Centrality Based On EigenVector"
for i in ce.keys()[:5]:
	print "node: %d have eigenvector: %f" % (i, ce[i])


#------------------------------------------------------------------------------------------------
#------------------ FIND 5 GREATEST CENTRALITY BASED ON EIGENVECTOR-----------
cp=CalculatePageRank(G1,1,100)
#Sorting DSC the ce(Centrality PageRank)
cp=OrderedDict(sorted(cp.items(),key=lambda x:x[1],reverse=True))
print "5 Greatest Centrality Based On Page Ranking"
for i in cp.keys()[:5]:
	print "node: %d have page rank: %f" % (i, cp[i])
#-------------------------------------------------------------------------------------------------

