# https://docs.ocean.dwavesys.com/en/latest/examples/scheduling.html


from dimod.reference.samplers import ExactSolver
import dwavebinarycsp


def scheduling(time, location, length, mandatory):
    if time:                                 # Business hours
        # In office and mandatory participation
        return (location and mandatory)
    else:                                    # Outside business hours
        # Teleconference for a short duration
        return ((not location) and length)


csp = dwavebinarycsp.ConstraintSatisfactionProblem(dwavebinarycsp.BINARY)
csp.add_constraint(scheduling, ['time', 'location', 'length', 'mandatory'])

bqm = dwavebinarycsp.stitch(csp)
print(bqm.linear)
print(bqm.quadratic)

sampler = ExactSolver()
solution = sampler.sample(bqm)
print(solution)

min_energy = next(solution.data(['energy']))[0]
print(min_energy)

for sample, energy in solution.data(['sample', 'energy']):
    if energy == min_energy:
        time = 'business hours' if sample['time'] else 'evenings'
        location = 'office' if sample['location'] else 'home'
        length = 'short' if sample['length'] else 'long'
        mandatory = 'mandatory' if sample['mandatory'] else 'optional'
        print("During {} at {}, you can schedule a {} meeting that is {}".format(
            time, location, length, mandatory))
