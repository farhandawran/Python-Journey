{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyO91+kZ3UaqbfP5Ryryu8Or"
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
      "execution_count": null,
      "metadata": {
        "id": "qCHjEFR2VMCz"
      },
      "outputs": [],
      "source": [
        "a= int(input(\"Enter First No:\"))\n",
        "b= int(input(\"Enter second No:\"))\n",
        "Operation =input(\"Which function do you want to perform (+,-,*,/ : ): \")\n",
        "\n",
        "def add(a, b):\n",
        "    return a+b\n",
        "def sub(a, b):\n",
        "    return a-b\n",
        "def mul(a, b):\n",
        "     return a*b\n",
        "def div(a, b):\n",
        "     return a/b\n",
        "\n",
        "match Operation:\n",
        "    case \"+\":\n",
        "        print(f\"Sum :  {add(a,b)}\")\n",
        "    case \"-\":\n",
        "            print(f\"sub: {sub(a,b)}\")\n",
        "    case \"*\":\n",
        "        print(f\"mul : {mul(a,b)}\")\n",
        "    case \"/\":\n",
        "            print(f\"Div: {div(a,b)}\")"
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "I created a simple calculator today. Its a basic calculator which i made just for understanding python.."
      ],
      "metadata": {
        "id": "ckT7uFRnVe-M"
      }
    }
  ]
}