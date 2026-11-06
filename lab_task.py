{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyOxc7lV2FCyi08H5u08L0/h",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/farhandawran/Python-Journey/blob/main/lab_task.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 8,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "mxr90uS1kZFG",
        "outputId": "f3bc5058-c239-4139-946a-ccd846ffbbc7"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "IDDFS, goal = J\n",
            "Depth limit 0: visited A                        ( 1 nodes) -> cutoff\n",
            "Depth limit 1: visited A B C                    ( 3 nodes) -> cutoff\n",
            "Depth limit 2: visited A B D E C F G            ( 7 nodes) -> cutoff\n",
            "Depth limit 3: visited A B D H I E J            ( 7 nodes) -> found\n",
            "Goal found at depth: 3\n",
            "Path: A -> B -> E -> J\n",
            "Total nodes visited by IDDFS (all iterations): 18\n",
            "\n",
            "BFS, goal = J\n",
            "Visited: A B C D E F G H I J\n",
            "Path: A -> B -> E -> J\n",
            "Total nodes visited by BFS: 10\n",
            "\n",
            "=== Comparison ===\n",
            "Algorithm Nodes visited  \n",
            "IDDFS     18             \n",
            "BFS       10             \n",
            "IDDFS visited 8 more nodes than BFS (1.8x)\n",
            "because it re-visits the upper levels in every iteration.\n"
          ]
        }
      ],
      "source": [
        "import networkx as nx\n",
        "import matplotlib.pyplot as plt\n",
        "from collections import deque\n",
        "\n",
        "tree = {\n",
        "    'A': ['B', 'C'],\n",
        "    'B': ['D', 'E'],\n",
        "    'C': ['F', 'G'],\n",
        "    'D': ['H', 'I'],\n",
        "    'E': ['J'],\n",
        "    'F': ['K'],\n",
        "    'G': [],\n",
        "    'H': [], 'I': [], 'J': [], 'K': []\n",
        "}\n",
        "\n",
        "# Depth-Limited Search -> ('found', path) / ('cutoff', None) / ('failure', None)\n",
        "def dls(node, goal, limit, visited_order, path):\n",
        "    visited_order.append(node)\n",
        "    path.append(node)\n",
        "    if node == goal:\n",
        "        return 'found', path\n",
        "    if limit == 0:\n",
        "        path.pop()\n",
        "        return 'cutoff', None\n",
        "    cutoff_occurred = False\n",
        "    for child in tree[node]:\n",
        "        res, p = dls(child, goal, limit - 1, visited_order, path)\n",
        "        if res == 'found':\n",
        "            return 'found', p\n",
        "        if res == 'cutoff':\n",
        "            cutoff_occurred = True\n",
        "    path.pop()\n",
        "    return ('cutoff', None) if cutoff_occurred else ('failure', None)\n",
        "\n",
        "# Returns (depth_found, path, total_nodes_visited_across_all_iterations)\n",
        "def iddfs(start, goal, max_depth=10):\n",
        "    total_visited = 0\n",
        "    for depth in range(max_depth + 1):\n",
        "        order, path = [], []\n",
        "        res, sol_path = dls(start, goal, depth, order, path)\n",
        "        total_visited += len(order)\n",
        "        visited = ' '.join(order)\n",
        "        print(f'Depth limit {depth}: visited {visited:<24} ({len(order):>2} nodes) -> {res}')\n",
        "        if res == 'found':\n",
        "            return depth, sol_path, total_visited\n",
        "        if res == 'failure':\n",
        "            return None, None, total_visited\n",
        "    return None, None, total_visited\n",
        "\n",
        "# Returns (path, visited_order)\n",
        "def bfs(start, goal):\n",
        "    queue = deque([[start]])\n",
        "    order = []\n",
        "    while queue:\n",
        "        path = queue.popleft()\n",
        "        node = path[-1]\n",
        "        order.append(node)\n",
        "        if node == goal:\n",
        "            return path, order\n",
        "        for child in tree[node]:\n",
        "            queue.append(path + [child])\n",
        "    return None, order\n",
        "\n",
        "GOAL_NODE = 'J'\n",
        "\n",
        "print('IDDFS, goal =', GOAL_NODE)\n",
        "depth_found, iddfs_path, iddfs_total = iddfs('A', GOAL_NODE)\n",
        "print('Goal found at depth:', depth_found)\n",
        "print('Path:', ' -> '.join(iddfs_path))\n",
        "print('Total nodes visited by IDDFS (all iterations):', iddfs_total)\n",
        "\n",
        "print()\n",
        "print('BFS, goal =', GOAL_NODE)\n",
        "bfs_path, bfs_order = bfs('A', GOAL_NODE)\n",
        "print('Visited:', ' '.join(bfs_order))\n",
        "print('Path:', ' -> '.join(bfs_path))\n",
        "print('Total nodes visited by BFS:', len(bfs_order))\n",
        "\n",
        "print()\n",
        "print('=== Comparison ===')\n",
        "print(f\"{'Algorithm':<10}{'Nodes visited':<15}\")\n",
        "print(f\"{'IDDFS':<10}{iddfs_total:<15}\")\n",
        "print(f\"{'BFS':<10}{len(bfs_order):<15}\")\n",
        "extra = iddfs_total - len(bfs_order)\n",
        "print(f'IDDFS visited {extra} more nodes than BFS ({iddfs_total / len(bfs_order):.1f}x)')\n",
        "print('because it re-visits the upper levels in every iteration.')"
      ]
    }
  ]
}