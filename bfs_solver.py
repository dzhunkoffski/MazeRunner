import numpy as np
from queue import Queue

class Graph():
    adj_list = None
    hasVisited = None
    distance = None
    prev = None

    bfs_q = Queue()
    sz_x = 0
    sz_y = 0

    def __init__(self, x, y):
        self.sz_x = x
        self.sz_y = y
        self.distance = [[0 for _ in range(y)] for i in range(x)]
        self.hasVisited = [[False for _ in range(y)] for i in range(x)]
        self.prev = [[[] for _ in range(y)] for i in range(x)]

    def get_shortest(self, from_v, to_v, mz):
        from_x, from_y = from_v
        to_x, to_y = to_v

        self.bfs(from_v, mz)
        if from_v != to_v and self.distance[to_x][to_y] == 0:
            print("Sorry, can not be reached")
            return
        else:
            print(self.distance[to_x][to_y])

        path = []
        now = to_v
        while now != from_v:
            now_x, now_y = now
            path.append(now)
            now = self.prev[now_x][now_y]

        path.append(now)
        return path

    def bfs(self, start, mz):
        movement = [
            [-1, 0],
            [1, 0],
            [0, 1],
            [0, -1]
        ]

        start_x, start_y = start
        self.bfs_q.put(start)
        self.hasVisited[start_x][start_y] = True

        while not self.bfs_q.empty():
            now = self.bfs_q.get()
            now_x, now_y = now
            for move in movement:
                if self.isValid(now, move, mz):
                    neighbour_x = now_x + move[0]
                    neighbour_y = now_y + move[1]
                    if not self.hasVisited[neighbour_x][neighbour_y]:
                        self.hasVisited[neighbour_x][neighbour_y] = True
                        self.bfs_q.put([neighbour_x, neighbour_y])
                        self.distance[neighbour_x][neighbour_y] = self.distance[now_x][now_y] + 1
                        self.prev[neighbour_x][neighbour_y] = now

    def isValid(self, now, move, mz):
        if 0 <= now[0] + move[0] < self.sz_x and 0 <= now[1] + move[1] < self.sz_y:
            if mz[now[0] + move[0], now[1] + move[1]] == 0:
                return True
            else:
                return False
        else:
            return False

def solve(maze, start_pos, finish_pos, x, y):
    graph = Graph(x, y)
    return graph.get_shortest(start_pos, finish_pos, maze)
