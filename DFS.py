class DFS:
    def __init__(self, graph, root):
        self.graph = graph
        self.visited = dict()
        self.stack = list()
        self.stack.append(root)
        self.counter = 0

    def run(self, target):
        while(len(self.stack) > 0):
            self.counter += 1
            current_State = self.stack.pop(len(self.stack) - 1)
            self.visited[current_State.UID] = current_State

            if(current_State.is_equal(target)):
                depth = current_State.step
                return True, self.counter, depth
            
            neighbor_nodes = self.graph.reveal_neighbors(current_State)

            for neighbor_node in neighbor_nodes:
                if(neighbor_node.UID not in self.visited.keys()):
                    self.stack.append(neighbor_node)

        # return 3 items
        # a: bool (match found or not)
        # b: int (counter)
        # c: int (depth)
        return False, 0, 0
