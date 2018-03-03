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
def makeGraphFromEdgeFile(filename):
#------------------ CREATING GRAPH from .edges file--------------------------------------
	file=open(filename,"r")
	lines=file.readlines()
	graph = snap.TUNGraph.New()
	for line in lines:
		line=line.strip("\n")
		line=map(int,line.split(" "))
		if not graph.IsNode(line[0]):
			graph.AddNode(line[0])
		if not graph.IsNode(line[1]):
			graph.AddNode(line[1])
		if not graph.IsEdge(line[0],line[1]):
			graph.AddEdge(line[0],line[1])
	#transverse_graph(graph)
	return graph

users=[0,107,348,414,686]
graphs=[]
for user in users: graphs.append(makeGraphFromEdgeFile("facebook/"+str(user)+".edges"))

for i,graph in enumerate (graphs):
	print "User: %d"%users[i]
	#------------------ FIND 5 GREATEST CENTRALITY BASED ON EIGENVECTOR-----------
	ce=CalculateEigenVectorCentr(graph)
	#Sorting DSC the ce(Centrality Eigenvector)
	ce=OrderedDict(sorted(ce.items(),key=lambda x:x[1],reverse=True))
	print "5 Greatest Centrality Based On EigenVector"
	for i in ce.keys()[:5]:
		print "node: %d have eigenvector: %f" % (i, ce[i])
	#------------------------------------------------------------------------------------------------
	#------------------ FIND 5 GREATEST CENTRALITY BASED ON EIGENVECTOR-----------
	cp=CalculatePageRank(graph,1,100)
	#Sorting DSC the ce(Centrality PageRank)
	cp=OrderedDict(sorted(cp.items(),key=lambda x:x[1],reverse=True))
	print "5 Greatest Centrality Based On Page Ranking"
	for i in cp.keys()[:5]:
		print "node: %d have page rank: %f" % (i, cp[i])
	#-------------------------------------------------------------------------------------------------
	print"--                                          --"
