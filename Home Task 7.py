from queue import Queue, PriorityQueue
from time import time
# The Puzzle Node
class Puzzle:
    GOAL = [1, 2, 3, 4, 5, 6, 7, 8, 0] # The goal state of the puzzle
    count = 0
    def __init__(self, state, parent, action, cost, use_h = False):
        self.state = state
        self.parent = parent
        self.action = action
        self.g = (parent.g + cost) if parent else 0
        self.h = self.manhattan() if use_h else 0
        self.f = self.g + self.h
        Puzzle.count += 1
    def is_goal(self):
        return self.state == Puzzle.GOAL
# Heuristic Function: Sum of Manhattan Distance
    def manhattan(self):
        total = 0
        for i, val in enumerate(self.state):
            if val == 0:
                continue
            goal_index = Puzzle.GOAL.index(val)
            total += abs(i // 3 - goal_index // 3) + abs(i % 3 - goal_index % 3)
        return total
#Movement
    def children(self):
        blank = self.state.index(0)
        row, col = divmod(blank, 3)
        moves = {
            'U': blank -3,
            'D': blank +3,
            'L': blank -1,
            'R': blank +1
        }
        if row == 0: del moves['U']
        if row == 2: del moves['D']
        if col == 0: del moves['L']
        if col == 2: del moves['R']
        results = []
        for action, target in moves.items():
            s = self.state.copy()
            s[blank], s[target] = s[target], s[blank]
            results.append(Puzzle(s, self, action, 1, use_h = True))
        return results
# Solution Path
    def solution(self):
        path ,node = [] ,self
        while node.parent:
            path.append(node.action)
            node = node.parent
        return list(reversed(path))
# BFS Algorithm
    def bfs(start):
        frontier, explored = Queue(), set()
        frontier.put(Puzzle(start, None, None, 0))
        while not frontier.empty():
            node = frontier.get()
            if node.is_goal():
                return node.solution()
            explored.add(tuple(node.state))
            for child in node.children():
                if tuple(child.state) not in explored:
                    frontier.put(child)
# A* Algorithm
    def a_star(start):
        frontier, explored, counter = PriorityQueue(), set(), 0
        frontier.put((0, counter, Puzzle(start, None, None, 0, use_h=True)))
        while not frontier.empty():
            _, _, node = frontier.get()
            frontier_set = set()
            if node.is_goal():
                return node.solution()
            explored.add(tuple(node.state))
            for child in node.children():
                if tuple(child.state) not in explored:
                    counter += 1
                    frontier.put((child.f, counter, child))
# Example Usage
states = [
    [1, 3, 4, 8, 6, 2, 7, 0, 5],
    [2, 8, 1, 0, 4, 3, 7, 6, 5],
    [5, 6, 7, 4, 0, 8, 3, 2, 1]
]
for state in states:
    print(f"Start: {state}")
    for name, fn, h in [("BFS", Puzzle.bfs, False), ("A*", Puzzle.a_star, True)]:
        Puzzle.count = 0
        start_time = time()
        solution = fn(state)
        end_time = time()
        print(f"{name}: --> {solution}, | nodes: {Puzzle.count}, Time: {end_time - start_time:.4f} seconds")
    print()