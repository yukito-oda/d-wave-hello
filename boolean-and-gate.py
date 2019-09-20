# %%
from dwave.system.samplers import DWaveSampler
from dwave.system.composites import EmbeddingComposite
sampler = EmbeddingComposite(DWaveSampler())
# not
# Q = {('x', 'x'): -1, ('x', 'z'): 2, ('z', 'x'): 0, ('z', 'z'): -1}

# and
Q = {('x1', 'x2'): 1, ('x1', 'z'): -2, ('x2', 'z'): -2, ('z', 'z'): 3}
response = sampler.sample_qubo(Q, num_reads=100)
for datum in response.data(['sample', 'energy', 'num_occurrences']):
    print(datum.sample, "Energy: ", datum.energy,
          "Occurrences: ", datum.num_occurrences)


# %%
