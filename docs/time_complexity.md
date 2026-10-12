# Algorithmic Complexity Analysis

## Model

Let:

- $V$ be the number of traversable grid cells.
- $E$ be the number of legal orthogonal connections between those cells.
- $N$ be the grid width and height for the square grid used by the interface.

For a 4-connected grid, $V \le N^2$ and $E \le 4V$ (more precisely, a square grid has fewer than $4V$ directed neighbor checks because boundary cells have fewer neighbors). The browser currently submits a 15 x 15 grid, so $V \le 225$.

## Time Complexity

The backend uses A* with:

- A binary heap (`heapq`) for the open set.
- Hash maps for `g_score` and `came_from`.
- A hash set for the closed set.

Each expanded cell checks at most four neighbors. With a binary heap, the graph-search bound is:

$$O((V + E)\log V)$$

For this grid, $E = O(V)$, so the bound simplifies to:

$$O(V\log V)$$

In terms of the grid width:

$$O(N^2\log N)$$

The Manhattan heuristic does not change the formal worst-case bound, but it usually causes the search to expand far fewer cells than an uninformed search. In an open warehouse, it points the frontier toward the target; walls can force A* to explore additional alternatives.

The often-quoted $O(b^d)$ bound is a tree-search perspective, where $b$ is the branching factor and $d$ is solution depth. It is useful for intuition, but the bounded grid-graph bound above describes this implementation more accurately. With $h(n)=0$, A* becomes Dijkstra's algorithm; with unit edge costs, its behavior is closely related to breadth-first search.

## Space Complexity

The implementation stores:

- The input wall matrix: $O(N^2)$.
- The open heap, which can contain duplicate entries when a better score is discovered: $O(E)$ in the implementation's worst case.
- `g_score`, `came_from`, and `closed_set`: $O(V)$.
- The returned `explored` sequence and reconstructed `path`: $O(V)$.

Therefore, the overall space complexity is:

$$O(V + E) = O(V) = O(N^2)$$

For the current 15 x 15 interface, the algorithm operates over a small, bounded state space. The main practical cost is not memory pressure but the number of cells explored before the route is found or proven unreachable.

## Performance Metrics Shown in the UI

The interface reports two runtime values:

- **Nodes explored:** the number of cells returned in the backend's `explored` trace.
- **Path length:** the number of moves in the final route, excluding the starting cell.

These are observed results for the selected warehouse layout, not substitutes for the asymptotic bounds above.
