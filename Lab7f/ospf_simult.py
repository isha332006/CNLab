import networkx as nx

class RIPRouter:
    def __init__(self, router_id, neighbors):
        self.router_id = router_id
        self.neighbors = neighbors
        self.distance_vector = {}
        self.prev_distance_vector = {}

    def initialize(self, all_routers):
        for r in all_routers:
            if r == self.router_id:
                self.distance_vector[r] = (0, r)
            elif r in self.neighbors:
                self.distance_vector[r] = (1, r)  # hop cost = 1
            else:
                self.distance_vector[r] = (float('inf'), None)
        self.prev_distance_vector = self.distance_vector.copy()

    def send_distance_vector(self):
        return self.distance_vector.copy()

    def update(self, neighbor_vectors):
        self.prev_distance_vector = self.distance_vector.copy()
        updated = False
        for dest in self.distance_vector:
            min_cost, min_next_hop = self.distance_vector[dest]
            for neighbor_id, neighbor_vector in neighbor_vectors.items():
                cost_to_neighbor = 1  # hop cost
                neighbor_cost = neighbor_vector[dest][0]
                total_cost = cost_to_neighbor + neighbor_cost
                if total_cost < min_cost:
                    min_cost = total_cost
                    min_next_hop = neighbor_id
            if min_cost != self.distance_vector[dest][0]:
                updated = True
                self.distance_vector[dest] = (min_cost, min_next_hop)
        return updated

    def routing_table(self):
        return {dest: (cost, next_hop) for dest, (cost, next_hop) in self.distance_vector.items()}


def simulate_rip(network_graph, max_rounds=20):
    routers = {node: RIPRouter(node, list(network_graph.neighbors(node))) for node in network_graph.nodes}
    for r in routers.values():
        r.initialize(network_graph.nodes)

    converged = False
    rounds = 0
    total_messages = 0

    while not converged and rounds < max_rounds:
        updates = 0
        router_vectors = {rid: routers[rid].send_distance_vector() for rid in routers}
        for rid, router in routers.items():
            neighbor_vectors = {nid: router_vectors[nid] for nid in router.neighbors}
            if router.update(neighbor_vectors):
                updates += 1

        rounds += 1
        total_messages += sum(len(r.neighbors) for r in routers.values())
        if updates == 0:
            converged = True

    print("== RIP Simulation Converged in", rounds, "rounds ==")
    for rid, router in routers.items():
        print("\nRouter", rid, "Routing Table:")
        print(f"{'Dest':>6} {'Cost':>6} {'Next hop':>10}")
        for dest, (cost, next_hop) in router.routing_table().items():
            print(f"{dest:>6} {cost:>6} {str(next_hop):>10}")
    print("\nTotal messages exchanged (estimate):", total_messages)
    print("Convergence achieved:", converged)


if __name__ == "__main__":
    G = nx.Graph()
    edges = [('A','B'),('B','C'),('C','D'),('D','A'),('A','C'),('B','D')]
    G.add_edges_from(edges)
    simulate_rip(G)
