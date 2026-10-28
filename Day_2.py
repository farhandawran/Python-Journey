{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyNVr+s0VyVInRxKrIOmqScS",
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
        "<a href=\"https://colab.research.google.com/github/farhandawran/Python-Journey/blob/main/Day_2.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 1,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "a8hm4hV8hqRs",
        "outputId": "e9dda569-04a2-4ccf-aa06-fbbd52c183ae"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Step 0: at A, sees Dirty, does Suck\n",
            "Step 1: at A, sees Clean, does Right\n",
            "Step 2: at B, sees Dirty, does Suck\n",
            "Step 3: at B, sees Clean, does Left\n",
            "Step 4: at A, sees Clean, does Right\n",
            "Step 5: at B, sees Clean, does Left\n"
          ]
        }
      ],
      "source": [
        "def vacuum_agent(percept):\n",
        "    location, status = percept\n",
        "    if status == \"Dirty\":\n",
        "        return \"Suck\"\n",
        "    elif location == \"A\":\n",
        "        return \"Right\"\n",
        "    else:\n",
        "        return \"Left\"\n",
        "\n",
        "# Environment\n",
        "world = {\"A\": \"Dirty\", \"B\": \"Dirty\"}\n",
        "location = \"A\"\n",
        "\n",
        "for step in range(6):\n",
        "    action = vacuum_agent((location, world[location]))\n",
        "    print(f\"Step {step}: at {location}, sees {world[location]}, does {action}\")\n",
        "\n",
        "    if action == \"Suck\":\n",
        "        world[location] = \"Clean\"\n",
        "    elif action == \"Right\":\n",
        "        location = \"B\"\n",
        "    elif action == \"Left\":\n",
        "        location = \"A\""
      ]
    }
  ]
}