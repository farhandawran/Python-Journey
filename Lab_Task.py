{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyOI7xSeZs7dSWwZoBiMDcbJ"
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
      "execution_count": 1,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "-2KEfRMJmmVe",
        "outputId": "3a75fb81-169e-4f3b-f52c-9281d710e9ef"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "=== TASK 3: reflex vs random ===\n",
            "State  1: A=Clean B=Clean start=B | reflex -20 | random -13\n",
            "State  2: A=Clean B=Dirty start=B | reflex  -9 | random  -1\n",
            "State  3: A=Dirty B=Dirty start=A | reflex   2 | random   9\n",
            "State  4: A=Clean B=Dirty start=A | reflex  -9 | random  -2\n",
            "State  5: A=Dirty B=Dirty start=A | reflex   2 | random  10\n",
            "State  6: A=Dirty B=Dirty start=A | reflex   2 | random   8\n",
            "State  7: A=Clean B=Dirty start=A | reflex  -9 | random -15\n",
            "State  8: A=Clean B=Clean start=A | reflex -20 | random -14\n",
            "State  9: A=Dirty B=Clean start=B | reflex  -9 | random  -7\n",
            "State 10: A=Clean B=Clean start=B | reflex -20 | random  -9\n",
            "Average reflex: -9.0\n",
            "Average random: -3.4\n",
            "\n",
            "=== TASK 4: model-based ===\n",
            "Trace (A Dirty, B Dirty, start A):\n",
            "Step  0: at A, sees Dirty -> Suck  | score 0\n",
            "Step  1: at A, sees Clean -> Right | score 10\n",
            "Step  2: at B, sees Dirty -> Suck  | score 9\n",
            "Step  3: at B, sees Clean -> NoOp  | score 19\n",
            "Step  4: at B, sees Clean -> NoOp  | score 19\n",
            "Step  5: at B, sees Clean -> NoOp  | score 19\n",
            "\n",
            "Average reflex:       -9.0\n",
            "Average model-based:  9.0\n"
          ]
        }
      ],
      "source": [
        "import random\n",
        "\n",
        "def reflex_agent(percept):\n",
        "    location, status = percept\n",
        "    if status == \"Dirty\":\n",
        "        return \"Suck\"\n",
        "    return \"Right\" if location == \"A\" else \"Left\"\n",
        "\n",
        "def random_agent(percept):\n",
        "    return random.choice([\"Left\", \"Right\", \"Suck\"])\n",
        "\n",
        "def make_model_based_agent():\n",
        "    cleaned = set()\n",
        "    def agent(percept):\n",
        "        location, status = percept\n",
        "        cleaned.add(location)\n",
        "        if status == \"Dirty\":\n",
        "            return \"Suck\"\n",
        "        if cleaned == {\"A\", \"B\"}:\n",
        "            return \"NoOp\"\n",
        "        return \"Right\" if location == \"A\" else \"Left\"\n",
        "    return agent\n",
        "\n",
        "def run(agent, world, location, steps=20, verbose=False):\n",
        "    world = dict(world)\n",
        "    score = 0\n",
        "    for step in range(steps):\n",
        "        action = agent((location, world[location]))\n",
        "        if verbose:\n",
        "            print(f\"Step {step:2}: at {location}, sees {world[location]:5} -> {action:5} | score {score}\")\n",
        "        if action == \"Suck\":\n",
        "            if world[location] == \"Dirty\":\n",
        "                score += 10\n",
        "            world[location] = \"Clean\"\n",
        "        elif action == \"Right\":\n",
        "            location = \"B\"; score -= 1\n",
        "        elif action == \"Left\":\n",
        "            location = \"A\"; score -= 1\n",
        "    return score\n",
        "\n",
        "random.seed(1)\n",
        "states = [({\"A\": random.choice([\"Clean\", \"Dirty\"]),\n",
        "            \"B\": random.choice([\"Clean\", \"Dirty\"])},\n",
        "           random.choice([\"A\", \"B\"])) for _ in range(10)]\n",
        "\n",
        "print(\"=== TASK 3: reflex vs random ===\")\n",
        "tr = tn = 0\n",
        "for i, (w, loc) in enumerate(states, 1):\n",
        "    r = run(reflex_agent, w, loc)\n",
        "    n = run(random_agent, w, loc)\n",
        "    tr += r; tn += n\n",
        "    print(f\"State {i:2}: A={w['A']:5} B={w['B']:5} start={loc} | reflex {r:3} | random {n:3}\")\n",
        "print(f\"Average reflex: {tr/10}\")\n",
        "print(f\"Average random: {tn/10}\")\n",
        "\n",
        "print(\"\\n=== TASK 4: model-based ===\")\n",
        "w, loc = {\"A\": \"Dirty\", \"B\": \"Dirty\"}, \"A\"\n",
        "print(\"Trace (A Dirty, B Dirty, start A):\")\n",
        "run(make_model_based_agent(), w, loc, steps=6, verbose=True)\n",
        "\n",
        "tm = tr2 = 0\n",
        "for w, loc in states:\n",
        "    tm += run(make_model_based_agent(), w, loc)\n",
        "    tr2 += run(reflex_agent, w, loc)\n",
        "print(f\"\\nAverage reflex:       {tr2/10}\")\n",
        "print(f\"Average model-based:  {tm/10}\")"
      ]
    }
  ]
}