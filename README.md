# Traveling Salesman Problem: Branch and Bound vs SLS

The traveling salesman problem is a well known graph problem that is NP-hard. 
The goal is to find the shortest path cost that traverses through every node once and returns to the start. 
To solve this problem, two different algorithms with heuristics will be implemented and explored. 
The two algorithms are the Branch and Bound Depth First Search (BnB-DFS) and the StochasticLocal Search (SLS).

## Branch and Bound DFS

Branch and Bound is an optimal-solution algorithm that prunes suboptimal pathways through a bound condition.  
We used the minimum remaining cost heuristic as a greedy heuristic for searching for the optimal path. 

While testing it was also noticed that lower standard deviation problems take longer to generate a
path. This is because it uses the minimum remaining cost heuristic and there are more branches
to check since values will be very close to U. This also leads to results that may not be optimal
since every path cost is different by only a small margin. By contrast it was also found that the
approach works better when standard deviation is higher since the difference between the
remaining path costs will be much larger, thus leading to the heuristic being more effective.
To improve the heuristics a normalization technique could be used when the
standard deviation is low and the path costs are very similar which would make the standard
deviation seem higher in order to distinguish different path costs.

## Simulated Annealing SLS

The simulated annealing is an SLS algorithm that does not gurantee optimality, where the goal is to find the global minima of
some objective function. In the Traveling Salesman Problem, the objective function was defined
to be the total path cost of a complete tour. To escape local minima, a temperature variable is
used. When temperature is high, the probabilities of selecting a specific neighbor from the
current node is roughly equal (blind algorithm), with no regards for cost. As temperature
decreases over every iteration by a rate of alpha, these probabilities start favoring minimum cost
paths, until eventually the search becomes a greedy algorithm. Eventually, the algorithm stops
once temperature is lower than a given stopping threshold.

The nearest neighbor and simulated annealing heuristics were selected to help maximize the
simplicity of the challenge and to minimize the cost of the algorithm.

## Conclusion 
After running both algorithms through TSP tests (see source code), the following conclusions were made:

**Branch and Bound**: Optimal solution with higher computational cost and works best with smaller datasets with high standard deviation.

**Simulated Annealing**: Non-optimal solution that requires numerous runs for best optimality, and works best with larger datasets. 
