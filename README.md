# Depth-First Search (DFS) with Path Tracking

## 📌 Description

This project implements the **Depth-First Search (DFS)** algorithm in Python to search for a goal node in a graph. It uses a stack to explore nodes and keeps track of the path from the starting node to the goal node.

The program starts from node `1` and searches for the goal node `7`. When the goal is found, it displays the path taken to reach it.

## 🎯 Objectives

* Understand the Depth-First Search (DFS) algorithm.
* Implement DFS using a stack in Python.
* Search for a specific goal node in a graph.
* Track and display the path from the start node to the goal node.

## 🛠️ Technologies Used

* **Programming Language:** Python 3
* **Concepts:** Graphs, Stack, Tree Traversal, Search Algorithms

## 📂 Graph Representation

The graph is represented using a Python dictionary, where each node is associated with a list of its neighboring nodes.

```python
graph = {
    1: [2, 3, 4],
    2: [5, 6],
    3: [],
    4: [7],
    5: [],
    6: [],
    7: []
}
```

### Graph Structure

```text
        1
      / | \
     2  3  4
    / \     \
   5   6     7
```

## ⚙️ How the Program Works

1. **Initialize the Stack:** The starting node and its path are pushed onto the stack.
2. **Pop a Node:** Remove the last added node from the stack.
3. **Visit the Node:** Display the node being visited.
4. **Check the Goal:** If the current node matches the goal, display a success message and the path.
5. **Explore Neighbors:** Add neighboring nodes and their paths to the stack.
6. **Repeat:** Continue until the goal is found or the stack becomes empty.
7. **Goal Not Found:** If the stack becomes empty without finding the goal, display a message indicating that the goal was not found.

## ▶️ How to Run the Program

### Prerequisites

Install Python 3 on your system.

### Steps

1. Download or clone this repository.
2. Open a terminal or Command Prompt in the project folder.
3. Run the following command:

```bash
python dfs.py
```

## 💻 Sample Output

```text
DFS search with path:
Visiting Node:1
Visiting Node:4
Visiting Node:7
Goal node 7 found!!
Path: 1->4->7
```

## 📚 Algorithm

1. Start with the initial node and its path.
2. Push the starting node and its path onto the stack.
3. While the stack is not empty:

   * Pop the top node and its path.
   * Print the current node.
   * If the node is the goal, print the path and stop.
   * Otherwise, push each neighbor and its updated path onto the stack.
4. If no goal is found, print `Goal not found`.

## ⏱️ Time and Space Complexity

* **Time Complexity:** O(V + E) is the standard complexity for DFS with a visited set. This implementation does not use a visited set and stores paths in the stack, so its actual performance can be worse on graphs with cycles or repeated paths.
* **Space Complexity:** Depends on the number of pending paths stored in the stack. In the worst case, it can grow significantly because each stack entry includes a path.

Here, **V** represents the number of vertices and **E** represents the number of edges.

## ✅ Conclusion

This project demonstrates how Depth-First Search explores a graph using a stack and finds a path from the starting node to the goal node. It is a beginner-friendly example for understanding graph traversal and search algorithms in Python.
