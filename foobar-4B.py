class Graph:

    def __init__(self, graph):
        self.graph = graph
        self.row = len(graph)

    def bfs(self, s, t, parent):
        visited = [False]*(self.row)
        queue = []
        queue.append(s)
        visited[s] = True

        while queue:
            u = queue.pop(0)
            for i,val in enumerate(self.graph[u]):
                if visited[i] == False and val > 0:
                    queue.append(i)
                    visited[i] == True
                    parent[i] = u

        return True if visited[t] else False

    def ford_fulkerson(self, source, sink):
        parent = [-1]*(self.row)
        max_flow = 0

        while self.bfs(source, sink, parent):
            path_flow = 99999
            s = sink
            while(s != source):
                path_flow = min(path_flow, self.graph[parent[s][s]])
                s = parent[s]

            max_flow += path_flow

            v = sink
            while(v != source):
                u = parent[v]
                self.graph[u][v] -= path_flow
                self.graph[v][u] += path_flow
                v = parent[v]
            
            return max_flow


