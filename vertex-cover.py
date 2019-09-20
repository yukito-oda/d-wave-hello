# %%
from dwave.system.composites import EmbeddingComposite
from dwave.system.samplers import DWaveSampler
import dwave_networkx as dnx
from dimod.reference.samplers import ExactSolver
import networkx as nx

# %%
s5 = nx.star_graph(4)
print(s5)
w5 = nx.wheel_graph(5)
c5 = nx.circular_ladder_graph(5)

# %%
# local cpu
sampler = ExactSolver()
# print(dnx.min_vertex_cover(s5, sampler))
# print(dnx.min_vertex_cover(w5, sampler))
print(dnx.min_vertex_cover(c5, sampler))

# %%
# d-wave
sampler = EmbeddingComposite(DWaveSampler())
print(dnx.min_vertex_cover(c5, sampler))


# %%
