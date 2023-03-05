import networkx as nx
import numpy as np
import openpyxl
import pandas as pd
import planarity
import matplotlib.pyplot as plt



wb = openpyxl.load_workbook('/Users/chenweixun/Desktop/coding/論文/資料/weight_adjacency_matrix_m2.xlsx')
names = pd.read_excel('/Users/chenweixun/Desktop/coding/論文/資料/names.xlsx')

ws = wb.active
myList = []
for row in ws.values:
    myList.append(list(map(float, row)))
myArr = np.array(myList)
G = nx.from_numpy_matrix(myArr)
def sort_graph_edges(G):
    sorted_edges = []
    for source, dest, data in sorted(G.edges(data=True),
                                     key=lambda x: x[2]['weight'], reverse=True):
        sorted_edges.append({'source': source,
                             'dest': dest,
                             'weight': data['weight']})
        
    return sorted_edges

def compute_PMFG(sorted_edges, nb_nodes):
    PMFG = nx.Graph()
    for edge in sorted_edges:
        PMFG.add_edge(edge['source'], edge['dest'])
        if not planarity.is_planar(PMFG):
            PMFG.remove_edge(edge['source'], edge['dest'])
            
        if len(PMFG.edges()) == 3*(nb_nodes-2):
            break
        
    return PMFG
sorted_edges = sort_graph_edges(G)

nb_nodes = 120
PMFG = compute_PMFG(sorted_edges, nb_nodes)
print(len(PMFG.edges), "edges instead of", int(nb_nodes*(nb_nodes-1)/2))


##################################
edgelist = PMFG.edges
A = nx.Graph()    
A.add_edges_from(edgelist)
print(nx.average_shortest_path_length(A))
print(nx.average_clustering(A))