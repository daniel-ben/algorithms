########## Making Graphs ############

from collections import deque


class Graph:
    def __init__(self):
        self.adjacency_list = {}

    ########## Make Graph ############

    def add_node(self, node):
        self.adjacency_list[node] = {}

    def add_unweighted_directed_edge(self, node_a, node_b):
        # {} is treated as dict, so set() to make empyt {} be treated as set
        self.adjacency_list[node_a] = set(self.adjacency_list[node_a])
        self.adjacency_list[node_a].add(node_b)

    def add_unweighted_undirected_edge(self, node_a, node_b):
        self.add_unweighted_directed_edge(node_a, node_b)
        self.add_unweighted_directed_edge(node_b, node_a)

    def add_weighted_directed_edge(self, node_a, node_b, weight):
        self.adjacency_list[node_a][node_b] = weight

    def add_weighted_undirected_edge(self, node_a, node_b, weight):
        self.add_weighted_directed_edge(node_a, node_b, weight)
        self.add_weighted_directed_edge(node_b, node_a, weight)

    ########## Lateral Search ############

    # add node to line
    # get node neighbors and iterate trough them
    # if neighbor is target, return True
    # else add neighbor neighbors to line
    # repeat
    def lateral_search(self, start, target):
        graph = self.adjacency_list
        search_line = deque()
        search_line += graph[start]  # add start node edges
        verified = [start]  # to prevent loops

        while search_line:
            item = search_line.popleft()  # remove and return first item in line
            if not item in verified:
                if item == target:
                    return True
                elif item != '':
                    # if not, add node edges to line
                    search_line += graph[item]
        return False  # if while ends, target is not on graph

    ########## Dijkstra Algorithm ############

    # create empty control list, empty tree hashtable
    # make costs hashtable with inf values
    # set starting costs value to 0
    # iterate through all nodes
    # get node with lowest value and it's neighbors
    # if current neighbor cost < node cost + node[neighbor] value, update neighbor cost
    # remove current node and repeat for next lowest value node
    # return costs from start to every node and tree with cheapest path

    def dijkstra_algorithm(self, start):
        graph = self.adjacency_list
        done_nodes = []
        tree = {}

        costs = {node: float('inf') for node in graph}
        costs[start] = 0

        node = find_lowest_value_in_hashtable(costs, done_nodes)
        node_cost = costs[node]
        while node != None:
            node_cost = costs[node]
            for neighbor in graph[node]:
                if costs[neighbor] > node_cost + graph[node][neighbor]:
                    costs[neighbor] = node_cost + graph[node][neighbor]
                    tree[neighbor] = node

            node = find_lowest_value_in_hashtable(costs, done_nodes)

        return costs, tree

    def get_shortest_path_to_target(self, start, target):
        costs, tree = self.dijkstra_algorithm(start)
        path = [target]
        branch = target
        while branch != start:
            path.append(tree[branch])
            branch = tree[branch]

        path.reverse()
        return path


def find_lowest_value_in_hashtable(hash, done_items):
    lowest_value = float('inf')
    lowest_item = None

    for item in hash.keys():
        if hash[item] < lowest_value and item not in done_items:
            lowest_item = item
            lowest_value = hash[item]

    done_items.append(lowest_item)
    return lowest_item
