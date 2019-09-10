# https://docs.ocean.dwavesys.com/en/latest/examples/map_kerberos.html

import matplotlib.pyplot as plt
from hybrid.reference.kerberos import KerberosSampler
import dwave_networkx as dnx
import networkx as nx
G = nx.read_adjlist('usa.adj', delimiter=',')

coloring = dnx.min_vertex_coloring(
    G, sampler=KerberosSampler(), chromatic_ub=4, max_iter=10, convergence=3)
set(coloring.values())

node_colors = [coloring.get(node) for node in G.nodes()]

print(node_colors)

# not works. Error "networkx.exception.NetworkXError: Node 'ND' has no position."

# adjust the next line if using a different map
# if dnx.is_vertex_coloring(G, coloring):
#     nx.draw(G, pos=nx.shell_layout(G, nlist=[list(G.nodes)[x:x+10] for x in range(0, 50, 10)] + [
#             [list(G.nodes)[50]]]), with_labels=True, node_color=node_colors, node_size=400, cmap=plt.cm.rainbow)
# plt.show()
