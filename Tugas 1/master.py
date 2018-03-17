"""
Created on Wed Feb 28 16:06:11 2018

@author: w7, erka
"""


import snap
import numpy as np
from scipy import linalg as la
from collections import OrderedDict
import matplotlib.pyplot as plt
import networkx as nx

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

def CalculateBetweennessCentrality(graph):
	nodes = snap.TIntFltH()
	edges = snap.TIntPrFltH()
	snap.GetBetweennessCentr(graph, nodes, edges, 1.0)
	output={}
	for node in nodes:
		output[node]=nodes[node]
	return output

def CalculateClusteringCoefficient(graph):
	#output={}
	NIdCCfH = snap.TIntFltH()
	snap.GetNodeClustCf(graph, NIdCCfH)
	print "CLUSTERRING COEFFICIENT"
	for item in NIdCCfH:
		print "Node %d th have coefficient %f" % (item, NIdCCfH[item])

def CalculateClosenessCentrality(graph):
	output = []
	for NI in graph.Nodes():
		CloseCentr = snap.GetClosenessCentr(graph, NI.GetId())
		output.append([NI.GetId(), CloseCentr]);
		# print "node: %d centrality: %f" % (NI.GetId(), CloseCentr)
	return output

def CalculatePowerLawDistribution(graph, user):
	DegToCntV = snap.TIntPrV()
	snap.GetDegCnt(graph, DegToCntV)
	x = []
	y = []
	for item in DegToCntV:
		x.append(item.GetVal2())
		y.append(item.GetVal1())
		# print "%d nodes with degree %d" % (item.GetVal2(), item.GetVal1())
	plt.plot(x, y, 'ro')
	plt.show()

def CalculateAveragePathLength(graph):
	Num = 100
	Dist = snap.GetBfsEffDiam(graph, Num)
	return Dist

def VisualizeGraph():
	graph = nx.read_edgelist("facebook/facebook_combined.txt", create_using=nx.Graph(), nodetype=int)
	print nx.info(graph)
	sp = nx.spring_layout(graph)
	plt.axis('off')
	nx.draw_networkx(graph, pos=sp, with_labels=False, node_size=35)
	plt.show()

#return output
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

# ------------------ VISUALIZE GRAPH-------------------------------------------------------
VisualizeGraph()
# -----------------------------------------------------------------------------------------

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
	#------------------ FIND 5 GREATEST CENTRALITY BASED ON PAGERANK-----------
	cp=CalculatePageRank(graph,1,100)
	#Sorting DSC the ce(Centrality PageRank)
	cp=OrderedDict(sorted(cp.items(),key=lambda x:x[1],reverse=True))
	print "5 Greatest Centrality Based On Page Ranking"
	for i in cp.keys()[:5]:
		print "node: %d have page rank: %f" % (i, cp[i])
	#-------------------------------------------------------------------------------------------------
	#------------------ FIND 5 GREATEST CENTRALITY BASED ON BETWEENESS CENTRALITY----
	cp=CalculateBetweennessCentrality(graph)
	#Sorting DSC the cb(Beetweenes Centrality)
	cp=OrderedDict(sorted(cp.items(),key=lambda x:x[1],reverse=True))
	print "5 Greatest Centrality Based On Beetweenes Centrality"
	for i in cp.keys()[:5]:
		print "node: %d have page rank: %f" % (i, cp[i])
	#-------------------------------------------------------------------------------------------------
	#------------------ CALCULATE ALL COEFFICIENT CLUSTERRING IN GRAPh----
	# CalculateClusteringCoefficient(graph)
	#-------------------------------------------------------------------------------------------------
	# print"--                                          --"
	#------------------ FIND 5 GREATEST CENTRALITY BASED ON CLOSENESS CENTRALITY-----------------------
	cp=CalculateClosenessCentrality(graph)
	cp=sorted(cp,key=lambda x:x[1],reverse=True)
	print "5 Greatest Centrality Based On Closeness Centrality"
	for i in range(5):
		print "node: %d have closeness: %f" % (cp[i][0], cp[i][1])
	#--------------------------------------------------------------------------------------------------
	# ------------------ FIND POWER LAW DISTRIBUTION---------------------------------------------------
	# CalculatePowerLawDistribution(graph, users[i])
	# -------------------------------------------------------------------------------------------------
	# ------------------ FIND AVERAGE PATH LENGTH------------------------------------------------------
	avg_dist = CalculateAveragePathLength(graph)
	print "Average Path Length"
	print avg_dist
	# -------------------------------------------------------------------------------------------------