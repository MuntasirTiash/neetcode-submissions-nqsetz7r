class Graph:
    
    def __init__(self):
        self.adjList = {}

    def addEdge(self, src: int, dst: int) -> None:
        if src not in self.adjList:
            self.adjList[src] = set()
        if dst not in self.adjList:
            self.adjList[dst] = set()
        self.adjList[src].add(dst)        

    def removeEdge(self, src: int, dst: int) -> bool:
        if src in self.adjList and dst in self.adjList[src]:
            self.adjList[src].remove(dst)
            return True
        return False


    def hasPath(self, src: int, dst: int) -> bool:
        visit = set()
        queue = deque()
        visit.add(src)
        queue.append(src)

        while queue:
            for i in range(len(queue)):
                curr = queue.popleft()
                if curr == dst:
                    return True
                
                for neighbor in self.adjList[curr]:
                    if neighbor not in visit:
                        visit.add(neighbor)
                        queue.append(neighbor)

        return False

