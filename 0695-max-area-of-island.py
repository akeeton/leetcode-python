"""
Given a non-empty 2D array grid of 0's and 1's, an island is a group of 1's (representing land) connected
4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

Find the maximum area of an island in the given 2D array. (If there is no island, the maximum area is 0.)

Example 1:
[[0,0,1,0,0,0,0,1,0,0,0,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,1,1,0,1,0,0,0,0,0,0,0,0],
 [0,1,0,0,1,1,0,0,1,0,1,0,0],
 [0,1,0,0,1,1,0,0,1,1,1,0,0],
 [0,0,0,0,0,0,0,0,0,0,1,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,0,0,0,0,0,0,1,1,0,0,0,0]]

Given the above grid, return 6. Note the answer is not 11, because the island must be connected 4-directionally.

Example 2:
[[0,0,0,0,0,0,0,0]]

Given the above grid, return 0.

Note: The length of each dimension in the given grid does not exceed 50.
"""

from collections import namedtuple

Vertex = namedtuple('Vertex', ['index_row', 'index_col'])


class Graph:
    def __init__(self):
        self.vertexes = set()
        self.edges = {}

    def add_vertex(self, v):
        self.vertexes.add(v)
        if v not in self.edges:
            self.edges[v] = set()

    def add_edge(self, v1, v2):
        self.edges[v1].add(v2)


def try_add_edge(graph, grid, vertex_from, index_row_to, index_col_to):
    if grid[index_row_to][index_col_to] == 1:
        vertex_to = Vertex(index_row_to, index_col_to)

        graph.add_vertex(vertex_to)
        graph.add_edge(vertex_from, vertex_to)
        graph.add_edge(vertex_to, vertex_from)


class Solution:
    @staticmethod
    def grid_to_graph(grid):
        graph = Graph()

        for index_row, row in enumerate(grid):
            for index_col, tile in enumerate(grid[index_row]):
                if tile == 0:
                    continue

                vertex_tile = Vertex(index_row, index_col)
                graph.add_vertex(vertex_tile)

                # up
                if index_row > 0:
                    index_row_up = index_row - 1
                    index_col_up = index_col

                    try_add_edge(graph, grid, vertex_tile, index_row_up, index_col_up)

                # right
                if index_col < len(grid[index_row]) - 1:
                    index_row_right = index_row
                    index_col_right = index_col + 1

                    try_add_edge(graph, grid, vertex_tile, index_row_right, index_col_right)

                # left
                if index_col > 0:
                    index_row_left = index_row
                    index_col_left = index_col - 1

                    try_add_edge(graph, grid, vertex_tile, index_row_left, index_col_left)

                # down
                if index_row < len(grid) - 1:
                    index_row_down = index_row + 1
                    index_col_down = index_col

                    try_add_edge(graph, grid, vertex_tile, index_row_down, index_col_down)

        return graph

    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        graph = Solution.grid_to_graph(grid)
        visited_vertexes = set()
        max_subgraph_size = 0
        subgraph = 0

        for vertex_root in graph.vertexes:
            if vertex_root in visited_vertexes:
                continue

            # subgraph += 1
            # print("subgraph:", subgraph)

            subgraph_size = 0
            vertexes_to_visit = [vertex_root]

            while len(vertexes_to_visit) > 0:
                vertex = vertexes_to_visit.pop()

                if vertex in visited_vertexes:
                    continue

                subgraph_size += 1
                max_subgraph_size = max(max_subgraph_size, subgraph_size)
                # print(vertex)
                visited_vertexes.add(vertex)

                neighbors = graph.edges[vertex]

                for neighbor in neighbors:
                    if neighbor not in visited_vertexes:
                        vertexes_to_visit.append(neighbor)

        return max_subgraph_size


def main():
    sol = Solution()

    grid_a = [[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
              [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
              [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]]

    graph_a = Solution.grid_to_graph(grid_a)
    print("graph a:", graph_a)

    print(sol.maxAreaOfIsland(grid_a))

    grid_b = [[0, 0, 0, 0, 0, 0, 0, 0]]
    print(sol.maxAreaOfIsland(grid_b))


if __name__ == '__main__':
    main()
