import networkx as nx
import numpy as np
import pandas as pd
import planarity
from networkx.algorithms import tree
import matplotlib.pyplot as plt



df = pd.read_excel('/Users/chenweixun/Desktop/coding/論文/資料/adjacency_matrix1.xlsx')
names = pd.read_excel('/Users/chenweixun/Desktop/coding/論文/資料/names1.xlsx')
HHI_data = pd.read_excel('/Users/chenweixun/Desktop/coding/論文/資料/HHI_data1.xlsx')
market_share = pd.read_excel('/Users/chenweixun/Desktop/coding/論文/資料/market_share1.xlsx')
revenue = pd.read_excel('/Users/chenweixun/Desktop/coding/論文/資料/reve_data1.xlsx')


myList = []
for i in range(len(df)):
    myList.append(df.iloc[i])
myArr = np.array(myList)


G = nx.from_numpy_matrix(myArr)
mst = tree.minimum_spanning_edges(G, algorithm="kruskal", data=False)
edgelist = list(mst)


# G = nx.from_numpy_matrix(myArr)
# def sort_graph_edges(G):
#     sorted_edges = []
#     for source, dest, data in sorted(G.edges(data=True),
#                                      key=lambda x: x[2]['weight'], reverse=True):
#         sorted_edges.append({'source': source,
#                              'dest': dest,
#                              'weight': data['weight']})
        
#     return sorted_edges

# def compute_PMFG(sorted_edges, nb_nodes):
#     PMFG = nx.Graph()
#     for edge in sorted_edges:
#         PMFG.add_edge(edge['source'], edge['dest'])
#         if not planarity.is_planar(PMFG):
#             PMFG.remove_edge(edge['source'], edge['dest'])
            
#         if len(PMFG.edges()) == 3*(nb_nodes-2):
#             break
        
#     return PMFG


# sorted_edges = sort_graph_edges(G)
# nb_nodes = len(names)
# PMFG = compute_PMFG(sorted_edges, nb_nodes)
# edgelist = PMFG.edges


A = nx.Graph()    
A.add_edges_from(edgelist)

# nx.draw(A, node_color='gray', with_labels=True)
# plt.show()

# degree_centrailty = nx.degree_centrality(A)
# degree_max_top5 = sorted(degree_centrailty, key=degree_centrailty.get, reverse=True)[:5]

# print('degree centrailty')
# for node in degree_max_top5:
#     print(names.at[node, 'names'])




# weight_dgree_cnetrailty = {}
# for node in A.nodes():
#     neighbor_list = [n for n in A.neighbors(node)]
   
#     weight_dgree = (revenue.iloc[neighbor_list].sum().values + revenue.iloc[node].values)/revenue.sum().values
#     weight_dgree_cnetrailty[node] = float(weight_dgree)
 

# rank=sorted(weight_dgree_cnetrailty.items(), key =lambda x : x[1],reverse=True)[:5]
# top_five = []
# for i in range(5):
#     print(names.iloc[rank[i][0]])
#     top_five.append(rank[i][0])
# print(top_five)


# color_map = []
# for node in A:
#     if node in top_five:
#         color_map.append('red')
#     else: 
#         color_map.append('gray')      
# nx.draw(A, node_color=color_map, with_labels=True)
# plt.show()


# closeness_centrailty = nx.closeness_centrality(A)
# closeness_max_top5 = sorted(closeness_centrailty, key=closeness_centrailty.get, reverse=True)[:5]

# print('closeness centrailty')
# for node in closeness_max_top5:
    
#     print(names.at[node, 'names'])

# weight_closeness_cnetrailty = {}
# p = nx.shortest_path(A)

# for j in range(len(names)):
#     a = 0
#     for i in range(len(names)):
        
#         a = a + revenue.iloc[i].values/len(p[i][j])
#     weight_closeness_cnetrailty[j] = float(a/revenue.sum().values)


# rank=sorted(weight_closeness_cnetrailty.items(), key =lambda x : x[1],reverse=True)[:5]

# top_five = []
# for i in range(5):
#     print(names.iloc[rank[i][0]])
#     top_five.append(rank[i][0])
# print(top_five)


# color_map = []
# for node in A:
#     if node in top_five:
#         color_map.append('red')
#     else: 
#         color_map.append('gray')      
# nx.draw(A, node_color=color_map, with_labels=True)
# plt.show()

# weight_decay_cnetrailty = {}
# p = nx.shortest_path(A)

# for j in range(len(names)):
#     a = 0
#     for i in range(len(names)):
        
#         a = a + (0.4**len(p[i][j])) * revenue.iloc[i].values
#     weight_decay_cnetrailty[j] = float(a/revenue.sum().values)


# rank=sorted(weight_decay_cnetrailty.items(), key =lambda x : x[1],reverse=True)[:5] 

# top_five = []
# for i in range(5):
#     print(names.iloc[rank[i][0]])
#     top_five.append(rank[i][0])
# print(top_five)


# color_map = []
# for node in A:
#     if node in top_five:
#         color_map.append('red')
#     else: 
#         color_map.append('gray')      
# nx.draw(A, node_color=color_map, with_labels=True)
# plt.show()

###################

# betweenness_centrailty = nx.betweenness_centrality(A)
# betweenness_max_top5 = sorted(betweenness_centrailty, key=betweenness_centrailty.get, reverse=True)[:5]

# print('betweenness centrailty')
# for node in betweenness_max_top5:
    
#     print(names.at[node, 'names'])

weight_betweenness_cnetrailty = {}
all_short_path = []

for j in range(len(names)):
    for i in range((j+1)):
        
        all_short_path.append([p for p in nx.all_shortest_paths(A, source=j, target=i)]) 

a = 0
for i in range(93):
    for j in range(len(all_short_path)):
        if i in all_short_path[j][0]:
            a = a + revenue.at[all_short_path[j][0][0], 'reve_data_list[[i]]'] + revenue.at[all_short_path[j][0][-1], 'reve_data_list[[i]]']
    weight_betweenness_cnetrailty[f'{i}'] = float(a / (revenue.sum().values*len(names))) 
    
    a = 0

print(weight_betweenness_cnetrailty)

rank=sorted(weight_betweenness_cnetrailty.items(), key =lambda x : x[1],reverse=True)[:5] 

top_five = []
for i in range(5):
    print(names.iloc[int(rank[i][0])])
    top_five.append(int(rank[i][0]))
print(top_five)


color_map = []
for node in A:
    if node in top_five:
        color_map.append('red')
    else: 
        color_map.append('gray')      
nx.draw(A, node_color=color_map, with_labels=True)
plt.show()