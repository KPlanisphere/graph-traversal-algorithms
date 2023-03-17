# Graph Traversal Algorithms

## Description
This project implements various graph traversal algorithms in Python using the NetworkX and Matplotlib libraries for visualization. The implemented algorithms include Breadth-First Search (BFS), Depth-First Search (DFS), and a heuristic-based traversal. These scripts provide a clear demonstration of how these algorithms work and how they can be visualized.

### Key Features
- **Breadth-First Search (BFS)**: Traverses the graph level by level.
- **Depth-First Search (DFS)**: Traverses the graph by exploring as far as possible along each branch before backtracking.
- **Heuristic-Based Traversal**: Uses a heuristic function to find the shortest path between nodes.

### Files
1. **BFS.py**
    - Implements the Breadth-First Search (BFS) algorithm.
    - **Key Code Snippet**:
        ```python
        import networkx as nx
        import matplotlib.pyplot as plt

        # Graph definition
        graph = {'A': ['B', 'F', 'C', 'G', 'E'],
                 'B': ['A', 'F'],
                 'C': ['A', 'E', 'D', 'H'],
                 'D': ['F', 'C', 'H'],
                 'E': ['G', 'A', 'C', 'I'],
                 'F': ['B', 'A', 'D'],
                 'G': ['A', 'E'],
                 'H': ['D', 'C', 'I'],
                 'I': ['E', 'H']}

        # BFS implementation
        def BFS(graph, start):
            # Code omitted for brevity
            pass

        # Visualization code omitted for brevity

        if __name__ == "__main__":
            orden_grafo_bfs, distancias = BFS(graph, 'A')
            print("Distancias: ", distancias)
            # Visualization code omitted for brevity
        ```
    - This script performs BFS on a graph and visualizes the traversal order and node distances.

2. **DFS.py**
    - Implements the Depth-First Search (DFS) algorithm.
    - **Key Code Snippet**:
        ```python
        import matplotlib.pyplot as plt
        import networkx as nx

        # Graph definition
        graph = {'A': ['B', 'F', 'C', 'G', 'E'],
                 'B': ['A', 'F'],
                 'C': ['A', 'E', 'D', 'H'],
                 'D': ['F', 'C', 'H'],
                 'E': ['G', 'A', 'C', 'I'],
                 'F': ['B', 'A', 'D'],
                 'G': ['A', 'E'],
                 'H': ['D', 'C', 'I'],
                 'I': ['E', 'H']}

        # DFS implementation
        def recursive_dfs(graph, source, path=[]):
            # Code omitted for brevity
            pass

        if __name__ == "__main__":
            path = recursive_dfs(graph, "A", [])
            print("DFS Path: ", path)
            # Visualization code omitted for brevity
        ```
    - This script performs DFS on a graph and visualizes the traversal path.

3. **Heuristica.py**
    - Implements a heuristic-based traversal algorithm.
    - **Key Code Snippet**:
        ```python
        import networkx as nx
        import matplotlib.pyplot as plt

        # Graph definition with weights
        grafo = {
            'G': {'A': 4, 'E': 3},
            'B': {'A': 5, 'F': 1},
            'A': {'G': 4, 'C': 7, 'F': 8, 'B': 5},
            'E': {'I': 3, 'C': 3, 'A': 2, 'G': 3},
            'F': {'D': 6, 'A': 8, 'B': 1},
            'D': {'C': 8, 'F': 6, 'H': 6},
            'C': {'D': 8, 'H': 3, 'E': 3, 'A': 7},
            'H': {'C': 3, 'D': 6, 'I': 2},
            'I': {'H': 2, 'E': 3}
        }

        if __name__ == "__main__":
            # Code to compute shortest path and heuristic omitted for brevity
            pass
        ```
    - This script calculates the shortest path using a heuristic and visualizes the graph with distances and weights.

### Project Structure
- **BFS.py**: Implementation and visualization of the Breadth-First Search algorithm.
- **DFS.py**: Implementation and visualization of the Depth-First Search algorithm.
- **Heuristica.py**: Implementation and visualization of a heuristic-based traversal algorithm.

## How to Use
1. **Installation**: Ensure you have Python installed along with the required libraries (`networkx` and `matplotlib`).
    ```bash
    pip install networkx matplotlib
    ```
2. **Running the Scripts**: Execute each script to see the respective graph traversal and visualization.
    ```bash
    python BFS.py
    python DFS.py
    python Heuristica.py
    ```

