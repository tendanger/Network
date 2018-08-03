#-*- coding:utf8-*-
#制作图表，添加节点和边

import networkx as nx
import matplotlib.pyplot as plt
#/Users/kun/Desktop/

G = nx.DiGraph()
G.add_node(1)
G.add_node(2)
G.add_nodes_from([3,4,5,6])

G.add_cycle([1,2,3,4])
G.add_edge(1,3)
G.add_edges_from([(3,5),(3,6),(6,7)])

nx.draw(G)

#write_pajek(G, path, encoding='UTF-8')

#nx.write_pajek(G,'' , encoding='UTF-8')

#nx.write_pajek(G, "D://111.net", encoding='UTF-8')

#plt.savefig("youxiangtu.png")

plt.show()
