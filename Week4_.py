{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyOiZmPmpL9+FfRfvMQnlqSx",
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
        "<a href=\"https://colab.research.google.com/github/MissMukuru/Lux_Academy_BootCamp/blob/main/Week4_.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "We push each character of the string oonto the stack and compare them to the original strings character in reverse order, if tghey do not match, then we can asume that it is not a palindrome"
      ],
      "metadata": {
        "id": "pGwhBEZ_3P4d"
      }
    },
    {
      "cell_type": "code",
      "execution_count": 1,
      "metadata": {
        "id": "Agr8SiCCz590"
      },
      "outputs": [],
      "source": [
        "def checker(text):\n",
        "  stack = []\n",
        "\n",
        "  for char in text:\n",
        "    stack.append(char)\n",
        "\n",
        "    for char in text:\n",
        "      if char != stack.pop():\n",
        "        return false\n",
        "\n",
        "    return true"
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "List comprehemnssion is an easy wat to create a a list in python, using user defined functions"
      ],
      "metadata": {
        "id": "W_K1tYWy2ZLl"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "square_numbers = [x**2 for x in range(10)]\n",
        "print(f\"Square numbers are: {square_numbers}\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "XRJxyixU0j6I",
        "outputId": "3afe47c0-6332-4708-b68b-eea652fbccea"
      },
      "execution_count": 7,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Square numbers are: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "a compound data tyoe is a dat type that hold a collection of other data types like a strings,integers or floats"
      ],
      "metadata": {
        "id": "ATVMqYnQ1jZK"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "a_list = ['Abby', 'Ashley', 12, 3.24]\n",
        "a_tuple = (10, 79, 3.14, 'Abby')\n",
        "a_set = {'Abby', 34, 3.35}\n",
        "\n",
        "print(a_list)\n",
        "print(a_tuple)\n",
        "print(a_set)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "ftA_mOm81O0C",
        "outputId": "feb6af60-be54-42f1-b04b-e371662e0a8e"
      },
      "execution_count": 9,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "['Abby', 'Ashley', 12, 3.24]\n",
            "(10, 79, 3.14, 'Abby')\n",
            "{34, 3.35, 'Abby'}\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "bigram function this function lets me iterate over the string extracting pairs of consqcutive characters"
      ],
      "metadata": {
        "id": "EDN9d7mT3BJk"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "def bigram_char(text):\n",
        "  bigrams = []\n",
        "\n",
        "  for i in range(len(text)-1):\n",
        "    bigrams.append(text[i:i+2])\n",
        "    return bigrams\n",
        "\n",
        "\n",
        "text = \"IloveDataengineeringsomuch\"\n",
        "print(f\"Bigrams in the text are\", bigram_char(text))\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "oVS3gcg816TU",
        "outputId": "c0aff9a2-d04f-4e3a-977c-f4468c6e7ca9"
      },
      "execution_count": 11,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Bigrams in the text are ['Il']\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "def closest_key(dictionary, value):\n",
        "  closest_key = None\n",
        "\n",
        "  closest_index = float\n",
        "\n",
        "\n",
        "  for key, value in dictionary.items():\n",
        "    if value in value:\n",
        "      index = value.index(value)\n",
        "\n",
        "      if index < closest_index:\n",
        "        closest_index = index\n",
        "        closest_key = key\n",
        "\n",
        "  return closest_key\n",
        "\n",
        "dict = {\n",
        "    'a': ['cats','dogs', 'rabbits'],\n",
        "    'b' : ['shoes', 'socks', 'crocs'],\n",
        "    'c' : ['bmw', 'Mercedes', 36]\n",
        "}\n",
        "\n",
        "print('closest_key', closest_key(dict, 'bmw'))\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "j5Pj4pWv3bwM",
        "outputId": "e2bb41be-49da-47b5-8fbf-962a9a6a3e6f"
      },
      "execution_count": 14,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "closest_key None\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "SFTu4my_6iRD"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}