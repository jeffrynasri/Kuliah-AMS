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
import os

def VisualizeGraph(graph):
	file = open("temp.txt", mode='w')
	for NI in graph.Nodes():
			for br in NI.GetOutEdges():
				file.write(str(NI.GetId()) + " " + str(br) + "\n")
	file.close()
	graph = nx.read_edgelist("temp.txt", create_using=nx.Graph(), nodetype=int)
	os.remove("temp.txt")
	#print nx.info(graph)
	sp = nx.spring_layout(graph)
	plt.axis('off')
	nx.draw_networkx(graph, pos=sp, with_labels=True, node_size=35)
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

def RankDegreeAdjacentNodeDSC(graph,nodeCenter):
	output={}
	NodeVec = snap.TIntV()
	sortedGraphDictionary=RankDegreeGraphDSC(graph) #DICITIONARY GRAPH UTAMA
	
	snap.GetNodesAtHop(graph, nodeCenter, 1, NodeVec, False)
	for item in NodeVec:
		output[item]=sortedGraphDictionary.get(item)

	#Sorting DSC
	output=OrderedDict(sorted(output.items(),key=lambda x:x[1],reverse=True))
	#print(output)
	return output
def GenerateRandomGraph():
	g = snap.TUNGraph.New()
	g.AddNode(1)
	g.AddNode(2)
	g.AddNode(3)
	g.AddNode(4)
	g.AddNode(5)
	g.AddEdge(1,2)
	g.AddEdge(2,3)
	g.AddEdge(3,4)
	g.AddEdge(4,5)
	g.AddEdge(3,5)
	g.AddEdge(1,5)
	
	return g

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
		output[i+1]=result_degree[i]
	
	#Sorting DSC
	output=OrderedDict(sorted(output.items(),key=lambda x:x[1],reverse=True))
	return output
def Select_m_VertexAsSeed(graph,subgraph,dictionary,m):
	#print(dictionary.keys()[0])
	for i in range(0,len(dictionary)):
		if(m<=0):
			return subgraph
		
		flag_dekat=0
		#Cek apakah data yang akan dimasukkan ke subgraph DEKAT DENGAN data yang sudah ada di subgraph
		for subg in subgraph:
			if(isVertexNear(graph,subg,dictionary.keys()[i])):
				flag_dekat=1
				
		if(flag_dekat==0):
			subgraph.append(dictionary.keys()[i])
			m=m-1
def isVertexNear(graph,vertexStart,vertexEnd): #DIKATAKAN TIDAK DEKAT, JIKA 2 VERTEX TERPISAH 2 EDGE
	NodeVec = snap.TIntV()
	snap.GetNodesAtHop(graph, vertexStart, 1, NodeVec, False)
	neighbours=[]
	for item in NodeVec:
		neighbours.append(item)
	
	if vertexEnd in neighbours:
		#print("TETANGGAN")
		return True
	else :
		return False
		#print("AMAN BOS")
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
	x=10 #UKURAN SUBGRAPH OUTPUT
	for user in users: graphs.append(makeGraphFromEdgeFile("facebook/"+str(user)+".edges"))
	
	for i,graph in enumerate (graphs):
		subgraph=[]
		seed=[]
		print "User: %d"%users[i]
		#------------------ RANGKING GRAPH BERDASARKAN DEGREE SECARA DESCENDING-----------
		sortedGraphDictionary=RankDegreeGraphDSC(graph)
		
		#------------------ INISIALISASI SUBGRAPH DG MEMILIH m NODE TERATAS -----------
		subgraph=Select_m_VertexAsSeed(graph,subgraph,sortedGraphDictionary,m)
		seed=Select_m_VertexAsSeed(graph,seed,sortedGraphDictionary,m)
		print(subgraph)
	
		Si=m
		while (Si<x):
			newseed=[]
			for itemSeed in seed:
				#Rank adjacent vertices of si based on degree values
				sortedAdjacentNodeDictionary=RankDegreeAdjacentNodeDSC(graph,itemSeed)
				#Select adjacent vertex w with highest degree put to seed
				newseed.append(sortedAdjacentNodeDictionary.keys()[0])
				#Select adjacent vertex w with highest degree put to subgraph
				subgraph.append(sortedAdjacentNodeDictionary.keys()[0])
				Si=Si+1
			seed=newseed
			
		print(subgraph)
	'''			
	g= GenerateRandomGraph()
	subgraph=[]
	sortedGraphasDictionary=RankDegreeGraphDSC(g)
	subgraph=Select_m_VertexAsSeed(g,subgraph,sortedGraphasDictionary,m)
	print(subgraph)
	
	'''
	#VisualizeGraph(g)
	