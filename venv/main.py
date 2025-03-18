import matplotlib.pyplot as plt
import networkx as nx

class ResourceAllocationGraph:
    def __init__(self,processes, resources):
        self.graph = nx.DiGraph()
        self.processes = processes
        self.resources = resources

    def add_edge(self, process, resource):
        self.graph.add_edge(process, resource)

    def visualize(self):
        position = nx.spring_layout(self.graph)
        options={
            "font_size":20,
            "node_size":2000
        }
        nx.draw(self.graph, **options)
        plt.show()

    def detect_deadlock(self):
        cycles = list(nx.simple_cycles(self.graph))

        if cycles:
            print('Deadlock detected')
            print('processes and resources involved are:', cycles)
        else:
            print('No deadlocks detected')
        

if __name__ == "__main__":
    # process = ['p1','p2','p3']
    # resources = ['r1','r2','r3']
    # rag1 = ResourceAllocationGraph(process, resources)
    # rag1.add_edge('r1','p2')
    # rag1.add_edge('p2','r2')
    # rag1.add_edge('p3','r2')
    # rag1.add_edge('r3','p3')

    # process = ['p1','p2','p3']
    # resources = ['r1','r2','r3','r4']
    # rag1 = ResourceAllocationGraph(process, resources)
    # rag1.add_edge('p1','r1')
    # rag1.add_edge('r2','p1')
    # rag1.add_edge('r1','p2')
    # rag1.add_edge('r2','p2')
    # rag1.add_edge('p2','r3')
    # rag1.add_edge('r3','p3')
    # rag1.add_edge('p3','r3')

    process = ['p1','p2','p3','p4']
    resources = ['r1','r2']
    rag1 = ResourceAllocationGraph(process, resources)
    rag1.add_edge('p1','r1')
    rag1.add_edge('r2','p1')
    rag1.add_edge('r1','p2')
    rag1.add_edge('r1','p3')
    rag1.add_edge('p3','r2')
    rag1.add_edge('r2','p4')


""" I think it thinks there is a deadlock because it is mistaking a deadlock for a cycle there is a 
cycle but not a deadlock. there are more than 2 resources so the the other resources can solve the issue 
the hold and wait condition is not met
"""

    rag1.visualize()
    rag1.detect_deadlock()