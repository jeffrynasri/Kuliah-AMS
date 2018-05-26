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


def RankDegreeGraphDSC(graph):
	output={}
	#NIdEigenH = snap.TIntFltH()
	#snap.GetEigenVectorCentr(graph, NIdEigenH)
	#for item in NIdEigenH:
		#print "node: %d have centrality: %f" % (item, NIdEigenH[item])
		#output[item]=NIdEigenH[item]
	
	result_degree = snap.TIntV()
	snap.GetDegSeqV(graph, result_degree)
	for i in range(0, result_degree.Len()):
		output[i]=result_degree[i]
	
	#Sorting DSC
	output=OrderedDict(sorted(output.items(),key=lambda x:x[1],reverse=True))
	return output
def Select_m_VertexAsSeed(m):
	print("")
def isVertexNear(graph,vertex1,vertex2):
	print("")
if __name__=="__main__":
	'''
	. Input graph, m = jumlah seed(diambil berapa teratas), sampling rate,x= sample size
	. buat fungsi RankDegreeGraphDSC
	. buat fungsi selectMvertexAsSeed
	. buat fungsi isVertexesNearest
	'''
	users=[0]#,107,348,414,686
	graphs=[]
	m=2 #JUMLAH SEED YG DIAMBIL. Graph yg telah diurutkan degreenya akan diambil m nodes TERATAS
	x=25 #UKURAN SUBGRAPH OUTPUT
	for user in users: graphs.append(makeGraphFromEdgeFile("facebook/"+str(user)+".edges"))

	for i,graph in enumerate (graphs):
		print "User: %d"%users[i]
		#------------------ RANGKING GRAPH BERDASARKAN DEGREE SECARA DESCENDING-----------
		sortedDictionary=RankDegreeGraphDSC(graph)
		
		for i in sortedDictionary.keys()[:5]:
			print "node: %d have eigenvector: %f" % (i, sortedDictionary[i])
		#------------------------------------------------------------------------------------------------
	