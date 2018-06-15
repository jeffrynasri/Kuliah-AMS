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

def countAllNode(graph):
	count=0
	for NI in graph.Nodes():
		count=count+1
	return count

def transverse_graph(graph):
	for NI in graph.Nodes():
		print "node: %d, degree %d" % ( NI.GetId(), NI.GetDeg())
		for br in NI.GetOutEdges():
			print br
def getNeighbours(graph,node):
	neighbours=[]
	for NI in graph.Nodes():
		if(NI.GetId() == node):
			for br in NI.GetOutEdges():
				neighbours.append(br)
	return neighbours
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
	sortedGraphDictionary=RankDegreeGraphDSC(graph) #DICITIONARY GRAPH UTAMA
	NodeVec = snap.TIntV()
	snap.GetNodesAtHop(graph, nodeCenter, 1, NodeVec, False)
	#NodeVec=getNeighbours(graph,nodeCenter)
	for item in NodeVec:
		output[item]=sortedGraphDictionary.get(item)

	#Sorting DSC
	output=OrderedDict(sorted(output.items(),key=lambda x:x[1],reverse=True))
	#print(output)
	return output
def GenerateRandomGraph():
	g = snap.TUNGraph.New()
	'''
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
	'''
	#GRAPH DI GOOGLE SLIDE
	g.AddNode(1)#OSCAR
	g.AddNode(2)#DAVE
	g.AddNode(3)#ALICE
	g.AddNode(4)#CARLOS
	g.AddNode(5)#LMOTHEP
	g.AddNode(6)#CAROL
	g.AddNode(7)#EVE
	g.AddNode(8)#CHUCK
	g.AddNode(9)#BOB
	g.AddNode(10)#ISHAC

	g.AddEdge(1,2)
	g.AddEdge(1,3)
	g.AddEdge(2,3)
	g.AddEdge(3,4)
	g.AddEdge(4,5)
	g.AddEdge(5,6)
	g.AddEdge(5,7)
	g.AddEdge(5,8)
	g.AddEdge(6,7)
	g.AddEdge(7,8)
	g.AddEdge(7,9)
	g.AddEdge(7,10)
	g.AddEdge(8,9)
	g.AddEdge(8,10)
	g.AddEdge(9,10)
	return g

def RankDegreeGraphDSC(graph):
	output={}
	'''
	result_degree = snap.TIntV()
	snap.GetDegSeqV(graph, result_degree)
	for i in range(0, result_degree.Len()):
		output[i+1]=result_degree[i]
	'''
	for NI in graph.Nodes():
		output[NI.GetId()]=NI.GetDeg()
	#Sorting DSC
	output=OrderedDict(sorted(output.items(),key=lambda x:x[1],reverse=True))
	return output
	
def Select_m_VertexAsSeed(graph,subgraph,dictionary,m):

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
			#print("NODE %d dengan degree %d akan dimasukkan ke SUBGRAPH" % (dictionary.keys()[i],dictionary.get(dictionary.keys()[i])))
			m=m-1
def isVertexNear(graph,vertexStart,vertexEnd): #DIKATAKAN TIDAK DEKAT, JIKA 2 VERTEX TERPISAH 2 EDGE
	NodeVec = snap.TIntV()
	snap.GetNodesAtHop(graph, vertexStart, 1, NodeVec, False)
	#NodeVec=getNeighbours(graph,vertexStart)
	
	neighbours=[]
	for item in NodeVec:
		neighbours.append(item)
	
	if vertexEnd in neighbours:
		#print("TETANGGAN")
		return True
	else :
		return False
		#print("AMAN BOS")

def degreeCentrality(graph, x):
	degCent = []
	for NI in graph.Nodes():
		DegCentr = snap.GetDegreeCentr(graph, NI.GetId())
		# print "node: %d centrality: %f" % (NI.GetId(), DegCentr)
		degCent.append([NI.GetId(), DegCentr])
	degCent = sorted(degCent, key=lambda x: x[1], reverse=True)
	degCent = degCent[:int(x)]
	return degCent

def betweenessCentrality(graph, x):
	betCent = []
	Nodes = snap.TIntFltH()
	Edges = snap.TIntPrFltH()
	snap.GetBetweennessCentr(graph, Nodes, Edges, 1.0)
	for node in Nodes:
		# print "node: %d centrality: %f" % (node, Nodes[node])
		betCent.append([node, Nodes[node]])
	betCent = sorted(betCent, key=lambda x: x[1], reverse=True)
	betCent = betCent[:int(x)]
	# print(betCent)
	return betCent

def getAccuracy(subgraph, degCent, betCent):
	#degree centrality acc
	deg_acc = 0
	bet_acc = 0
	for node in subgraph:
		for node_deg in degCent:
			if(node == node_deg[0]):
				deg_acc+=1
				break
		for node_bet in betCent:
			if(node == node_bet[0]):
				bet_acc+=1
				break
	return float(deg_acc)/len(subgraph), float(bet_acc)/len(subgraph)

if __name__=="__main__":
	samplingRates=[0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1]
	users=[0,107,348,414,686,698,1684,1912,3437,3980]#,0,107,348,414,686,698,1684,1912,3437,3980
	graphs=[]
	m=2 #JUMLAH SEED YG DIAMBIL. Graph yg telah diurutkan degreenya akan diambil m nodes TERATAS
	samplingRate=0.1 #SAMPLING RATE
	
	for user in users: graphs.append(makeGraphFromEdgeFile("facebook/"+str(user)+".edges"))
	
	for i,graph in enumerate (graphs):
		''' 
		#HAPUS KOMEN INI, UNTUK MENGGUNAKAN GRAP yg DI GGOGLE SLIDE
		graph=GenerateRandomGraph() 
		VisualizeGraph(graph)
		'''
		
		'''
		graph = snap.TUNGraph.New()
	
		graph.AddNode(13)
		graph.AddNode(2)
		graph.AddNode(3)
		graph.AddNode(4)
		graph.AddNode(5)
		graph.AddEdge(13,2)
		graph.AddEdge(2,3)
		graph.AddEdge(3,4)
		graph.AddEdge(4,5)
		graph.AddEdge(3,5)
		graph.AddEdge(13,5)
		
		print(RankDegreeGraphDSC(graph))
		'''
		print "Graph User: %d"%users[i]
		print "Graph noder: %d"%countAllNode(graph)
		
		for itemRate in samplingRates  :
			print itemRate
			samplingRate=itemRate
			subgraph=[]
			seed=[]
			x=samplingRate*snap.CntNonZNodes(graph)/10 #UKURAN SUBGRAPH OUTPUT
			

			#------------------ RANGKING GRAPH BERDASARKAN DEGREE SECARA DESCENDING-----------
			sortedGraphDictionary=RankDegreeGraphDSC(graph)
			
			#------------------ INISIALISASI SUBGRAPH DG MEMILIH m NODE TERATAS -----------
			subgraph=Select_m_VertexAsSeed(graph,subgraph,sortedGraphDictionary,m)
			seed=list(subgraph)
			
			Si=m
			while (Si<x):
				newseed=[]
				for itemSeed in seed:
					#Rank adjacent vertices of si based on degree values
					sortedAdjacentNodeDictionary=RankDegreeAdjacentNodeDSC(graph,itemSeed)
					#Select adjacent vertex w with highest degree put to seed and Subgraph
					for i in range(0,len(sortedAdjacentNodeDictionary)):
						if (sortedAdjacentNodeDictionary.keys()[i] not in subgraph):
							newseed.append(sortedAdjacentNodeDictionary.keys()[i])
							subgraph.append(sortedAdjacentNodeDictionary.keys()[i])
							#print("NODE %d dengan degree %d akan dimasukkan ke SUBGRAPH" % (sortedAdjacentNodeDictionary.keys()[i],sortedAdjacentNodeDictionary.get(sortedAdjacentNodeDictionary.keys()[i])))
							Si=Si+1
							break
					
				seed=list(newseed)
				
			print("OUTPUT Subgraph = " + str( subgraph))

			degCent = degreeCentrality(graph, x)
			betCent = betweenessCentrality(graph, x)
			print getAccuracy(subgraph, degCent, betCent)
			
			print("---------------------------------------")
	