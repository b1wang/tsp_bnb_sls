import argparse
import numpy as np
import sys
import copy
from collections import deque
import time


def get_neighbors(cur_node, visited, N):
    if len(visited) == N:
        return {visited[0]}
    
    all_node = set(range(N))
    unvisited = all_node.difference(set(visited))

    return unvisited
  
def minimum_remaining_path(cost_matrix, cur_node, visited, N):
    if len(visited) == N:
        return cost_matrix[visited[-1]][visited[0]]
    
    cur_visited = copy.deepcopy(visited)
    cur_visited.append(cur_node)

    all_node = set(range(N))
    unvisited = all_node.difference(set(visited))

    unvisited_cost = np.array([cost_matrix[cur_node][node] for node in unvisited])

    min_cost = np.amin(unvisited_cost)
    min_node = np.argmin(unvisited_cost)

    return min_cost + minimum_remaining_path(cost_matrix, min_node, cur_visited, N)
    
def BNB_TSP(cost_matrix, N):
    cur_node = 0
    travel_stack = deque()
    best_assignment = None
    U = sys.maxsize

    # initialize travel stack
    init_neighbors = get_neighbors(cur_node, [0], N)

    for neighbor in init_neighbors:
        travel_stack.append(([0], copy.deepcopy(neighbor), 0))
    
    while travel_stack:
        cur_visited, target, travel_cost = travel_stack.pop()
        cur_node = cur_visited[-1]

        min_remain_path = minimum_remaining_path(
            cost_matrix, 
            target, 
            cur_visited, 
            N
        )

        travel_cost += cost_matrix[cur_node][target]

        if (travel_cost + min_remain_path) >= U:
            continue

        if len(cur_visited) == N:
            U = travel_cost + min_remain_path
            cur_visited.append(target)
            best_assignment = cur_visited
        else:
            cur_visited.append(target)
            neighbors = get_neighbors(target, cur_visited, N)
            for neighbor in neighbors:
                travel_stack.append((copy.deepcopy(cur_visited), copy.deepcopy(neighbor), travel_cost))
        
    return best_assignment    

def total_path_cost(tsp_matrix, best_assignment):
    path = best_assignment

    path_cost = 0
    for i in range(len(path) - 1):
        path_cost += tsp_matrix[path[i]][path[i + 1]]

    return path_cost

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--tsp_file', help='the tsp_file.out that is generated from generate_travelling_salesman_problem.py')
    args = parser.parse_args()
    
    # preprocessing file to read in info
    lines = ''
    with open(args.tsp_file) as f:
        lines = f.read().splitlines()

    N = lines[0]
    tsp_matrix = lines[1:]
  
    list_tsp_matrix = []

    for row in tsp_matrix:
        list_tsp_matrix.append(row.split(' '))

    tsp_matrix = np.array(list_tsp_matrix, dtype=float)

    # start the timer process
    s = time.time()

    print("finding best path using BnB-DFS...")
    
    best_assignment = BNB_TSP(tsp_matrix, int(N))

    print('best assignment found: ', best_assignment)
    print(f'Cost: {total_path_cost(tsp_matrix, best_assignment)}')
    print(f"timer: {(time.time() - s):.9f}s")

if __name__ == "__main__":
    main()