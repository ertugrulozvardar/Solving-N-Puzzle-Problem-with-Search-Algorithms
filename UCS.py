import queue as Q


class UCS:
    def __init__(self, graph, root):
        self.graph = graph
        self.visited = dict()
        self.queue = Q.PriorityQueue()
        self.counter = 0
        self.visited[root.UID] = root
        self.queue.put((0, root, int(root.UID)))

    def run(self, target):

        while(not self.queue.empty()):
            self.counter += 1
            depth, current_State, uid = self.queue.get()
            self.visited[current_State.UID] = current_State

            if(current_State.is_equal(target)):
                return True, self.counter, depth
                
            neighbor_nodes = self.graph.reveal_neighbors(current_State)

            for neighbor_node in neighbor_nodes:
                if(neighbor_node.UID not in self.visited.keys()):
                    self.queue.put((depth + 1,neighbor_node,int(neighbor_node.UID)))

        

        # return 3 items
        # a: bool (match found or not)
        # b: int (counter)
        # c: int (depth)
        return False, 0, 0
