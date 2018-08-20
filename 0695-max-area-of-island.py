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

import typing

from dataclasses import dataclass
from typing import List, Set

Vertex = typing.NamedTuple('Vertex', index_row=int, index_col=int)
Edge = typing.NamedTuple('Edge', v1=Vertex, v2=Vertex)


@dataclass
class Graph:
    vertexes: Set[Vertex]
    edges: Set[Edge]

    def add_vertex(self, v: Vertex):
        self.vertexes.add(v)

    def add_edge(self, edge: Edge):
        self.edges.add(edge)


def try_add_edge(graph: Graph, grid: List[List[int]], vertex_from: Vertex, index_row_to: int, index_col_to: int):
    if grid[index_row_to, index_col_to] == 1:
        vertex_to = Vertex(index_row_to, index_col_to)

        graph.add_edge(Edge(vertex_from, vertex_to))
        graph.add_edge(Edge(vertex_to, vertex_from))


class Solution:
    @staticmethod
    def grid_to_graph(grid: List[List[int]]) -> Graph:
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

    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """


def main():
    grid_a = [[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
              [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
              [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]]

    print(Solution.grid_to_graph(grid_a))


if __name__ == '__main__':
    main()
