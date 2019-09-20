# %%
# initialize
# https://docs.ocean.dwavesys.com/en/latest/examples/topology_samplers.html
import neal
import dimod
import dwave_networkx as dnx
import networkx as nx
import dwave.embedding
from dwave.system import DWaveSampler, EmbeddingComposite
import matplotlib.pyplot as plt

# %%
# Creating a Chimera Sapmler
C16 = dnx.chimera_graph(16)
# print(C16)
classical_sampler = neal.SimulatedAnnealingSampler()
sampler = dimod.StructureComposite(classical_sampler, C16.nodes, C16.edges)
h = {v: 0.0 for v in C16.nodes}
J = {(u, v): 1 for u, v in C16.edges}
sampleset = sampler.sample_ising(h, J)

embedding_sampler = EmbeddingComposite(sampler)

qpu_sampler = DWaveSampler(
    solver={'qpu': True, 'num_active_qubits__within': [2000, 2048]})
QPUGraph = nx.Graph(qpu_sampler.edgelist)
all(v in C16.nodes for v in QPUGraph.nodes)
all(edge in C16.edges for edge in QPUGraph.edges)


# %%
# Creating a Pegasus Sampler
P6 = dnx.pegasus_graph(6)
classical_sampler = neal.SimulatedAnnealingSampler()
sampler = dimod.StructureComposite(classical_sampler, P6.nodes, P6.edges)


# %%
# Working With Embeddings
# 全結合の40ノードを作りたい
num_variables = 40
embedding = dwave.embedding.chimera.find_clique_embedding(num_variables, 16)
max(len(chain) for chain in embedding.values())
# チェーン数は11


# %%
# 680 node Pegasus
num_variables = 40
embedding = dwave.embedding.pegasus.find_clique_embedding(num_variables, 6)
max(len(chain) for chain in embedding.values())
# チェーン数は6


# %%
# https://qiita.com/YuichiroMinato/items/dbc142ecb1efbebd6adf
chimera = dnx.chimera_graph(2, 2, 4)
dnx.draw_chimera(chimera)
plt.show()


# %%
P3 = dnx.pegasus_graph(2)
dnx.draw_pegasus(P3)
plt.show()


# %%
