import queue as Q


class AStar:
    def __init__(self, graph, root):
        self.graph = graph
        self.root = root
        self.visited = dict()
        self.queue = Q.PriorityQueue()
        self.counter = 0

    def run(self, target):
        self.queue.put((0 + self.manhattan_distance(self.root, target), self.root, int(self.root.UID)))
        while(not self.queue.empty()):
            self.counter += 1
            price, current_State, uid = self.queue.get()
            self.visited[current_State.UID] = current_State

            if(current_State.is_equal(target)):
                return True, self.counter, current_State.step
                
            neighbor_nodes = self.graph.reveal_neighbors(current_State)

            for neighbor_node in neighbor_nodes:
                if(neighbor_node.UID not in self.visited.keys()):
                    self.queue.put((price + self.manhattan_distance(neighbor_node, target) + 1, neighbor_node,int(neighbor_node.UID)))

        

        # return 3 items
        # a: bool (match found or not)
        # b: int (counter)
        # c: int (depth)
        return False, 0, 0

    def manhattan_distance(self, node, end):
        arr = [0] * (self.graph.size + 1)
        brr = [0] * (self.graph.size + 1)
        for i in range(len(node.g_node)):
            for j in range(len(node.g_node[i])):
                arr[node.g_node[i][j]] = [i, j]

        for i in range(len(end.g_node)):
            for j in range(len(end.g_node[i])):
                brr[end.g_node[i][j]] = [i, j]
        dist = 0
        for i in range(1, len(arr)):
            dist += abs(arr[i][0] - brr[i][0]) + abs(arr[i][1] - brr[i][1])
        return dist
