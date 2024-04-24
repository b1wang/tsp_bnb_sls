import argparse
import numpy as np
import math
import random
import sys
import copy
from collections import deque

DEFAULT_TEMP = 50
DEFAULT_ALPHA = 0.8
DEFAULT_STOP = 0.001

# Main SLS function 
def simulated_annealing(cost_matrix, N, T=DEFAULT_TEMP, 
                        alpha=DEFAULT_ALPHA, stop=DEFAULT_STOP):
    current = generate_random_tour(N)
    while(T > stop):
        next = change_path(current)
        error_diff = total_path_cost(cost_matrix, current) - total_path_cost(cost_matrix, next)
        if (error_diff > 0):
            current = next          # Change tour if cost is lower
        else:
            probability = random.randint(0,100) / 100
            if (probability < math.exp(-error_diff/T)):
                current = next      # Change tour even if cost is higher based on T
        T *= alpha
    return current

# Returns a randomized tour 
def generate_random_tour(N):
    tour = np.arange(N)             # Creates an array of [0,...,N-1]
    np.random.shuffle(tour[1:])     # Randomizes the tour
    tour = np.append(tour, tour[0]) # Returns to start
    return tour                

# Optimization Function:
#   Input = the current tour
#   Output = Tour with two locations swapped (excluding start and end)
def change_path(curr_tour):
    tour = curr_tour
    node1, node2 = random.sample(range(len(tour)-2), 2) 
    node1 += 1
    node2 += 1
    tour[node1], tour[node2] = tour[node2], tour[node1]
    return tour

# Return the tour cost on the TSP + returning to the start node
def total_path_cost(cost_matrix, curr_tour):
    path_cost = 0
    for i in range(len(curr_tour)-1):
        path_cost += cost_matrix[curr_tour[i]][curr_tour[i+1]]  
    return path_cost       

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--tsp_file', help='foo help')
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
    
    best_assignment = simulated_annealing(tsp_matrix, int(N))

    print('best assignment found: ', best_assignment)
    print(f'Cost: {total_path_cost(tsp_matrix, best_assignment)}')

if __name__ == "__main__":
    main()