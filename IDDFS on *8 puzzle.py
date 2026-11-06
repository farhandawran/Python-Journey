{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyNwC8PhEhhTUFWV+65SWcSC"
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
      "cell_type": "code",
      "execution_count": 9,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "mxr90uS1kZFG",
        "outputId": "c4699bc2-d350-492d-e410-ca4172bda60b"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Start state: (1, 2, 3, 4, 0, 6, 7, 5, 8)\n",
            "Goal found at depth: 2\n",
            "Number of nodes expanded: 4\n",
            "Solution path:\n",
            "(1, 2, 3)\n",
            "(4, 0, 6)\n",
            "(7, 5, 8)\n",
            "\n",
            "(1, 2, 3)\n",
            "(4, 5, 6)\n",
            "(7, 0, 8)\n",
            "\n",
            "(1, 2, 3)\n",
            "(4, 5, 6)\n",
            "(7, 8, 0)\n",
            "\n"
          ]
        }
      ],
      "source": [
        "GOAL = (1, 2, 3, 4, 5, 6, 7, 8, 0)\n",
        "START = (1, 2, 3, 4, 0, 6, 7, 5, 8)\n",
        "\n",
        "def neighbors(state):\n",
        "    i = state.index(0)                    # position of the blank\n",
        "    r, c = divmod(i, 3)\n",
        "    result = []\n",
        "    for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):\n",
        "        nr, nc = r + dr, c + dc\n",
        "        if 0 <= nr < 3 and 0 <= nc < 3:\n",
        "            j = nr * 3 + nc\n",
        "            s = list(state)\n",
        "            s[i], s[j] = s[j], s[i]\n",
        "            result.append(tuple(s))\n",
        "    return result\n",
        "\n",
        "def dls_puzzle(state, limit, path, counter):\n",
        "    if state == GOAL:\n",
        "        return path\n",
        "    if limit == 0:\n",
        "        return 'cutoff'\n",
        "    counter[0] += 1                       # this node is expanded\n",
        "    cutoff_occurred = False\n",
        "    for nxt in neighbors(state):\n",
        "        if nxt in path:                   # avoid cycles\n",
        "            continue\n",
        "        res = dls_puzzle(nxt, limit - 1, path + [nxt], counter)\n",
        "        if res == 'cutoff':\n",
        "            cutoff_occurred = True\n",
        "        elif res is not None:\n",
        "            return res\n",
        "    return 'cutoff' if cutoff_occurred else None\n",
        "\n",
        "def iddfs_puzzle(start, max_depth=30):\n",
        "    total_expanded = 0\n",
        "    for depth in range(max_depth + 1):\n",
        "        counter = [0]\n",
        "        res = dls_puzzle(start, depth, [start], counter)\n",
        "        total_expanded += counter[0]\n",
        "        if res not in ('cutoff', None):\n",
        "            return depth, res, total_expanded\n",
        "    return None, None, total_expanded\n",
        "\n",
        "depth, solution, expanded = iddfs_puzzle(START)\n",
        "print('Start state:', START)\n",
        "print('Goal found at depth:', depth)\n",
        "print('Number of nodes expanded:', expanded)\n",
        "print('Solution path:')\n",
        "for s in solution:\n",
        "    print(s[0:3])\n",
        "    print(s[3:6])\n",
        "    print(s[6:9])\n",
        "    print()"
      ]
    }
  ]
}