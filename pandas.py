{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "pandas",
      "provenance": [],
      "collapsed_sections": [],
      "authorship_tag": "ABX9TyOMnyLTAN+CqseFZFB3xyHQ",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
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
        "<a href=\"https://colab.research.google.com/github/deekshadaga/forsk_python/blob/master/pandas.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "6ZJHpW1zXR8K",
        "colab_type": "code",
        "colab": {
          "resources": {
            "http://localhost:8080/nbextensions/google.colab/files.js": {
              "data": "Ly8gQ29weXJpZ2h0IDIwMTcgR29vZ2xlIExMQwovLwovLyBMaWNlbnNlZCB1bmRlciB0aGUgQXBhY2hlIExpY2Vuc2UsIFZlcnNpb24gMi4wICh0aGUgIkxpY2Vuc2UiKTsKLy8geW91IG1heSBub3QgdXNlIHRoaXMgZmlsZSBleGNlcHQgaW4gY29tcGxpYW5jZSB3aXRoIHRoZSBMaWNlbnNlLgovLyBZb3UgbWF5IG9idGFpbiBhIGNvcHkgb2YgdGhlIExpY2Vuc2UgYXQKLy8KLy8gICAgICBodHRwOi8vd3d3LmFwYWNoZS5vcmcvbGljZW5zZXMvTElDRU5TRS0yLjAKLy8KLy8gVW5sZXNzIHJlcXVpcmVkIGJ5IGFwcGxpY2FibGUgbGF3IG9yIGFncmVlZCB0byBpbiB3cml0aW5nLCBzb2Z0d2FyZQovLyBkaXN0cmlidXRlZCB1bmRlciB0aGUgTGljZW5zZSBpcyBkaXN0cmlidXRlZCBvbiBhbiAiQVMgSVMiIEJBU0lTLAovLyBXSVRIT1VUIFdBUlJBTlRJRVMgT1IgQ09ORElUSU9OUyBPRiBBTlkgS0lORCwgZWl0aGVyIGV4cHJlc3Mgb3IgaW1wbGllZC4KLy8gU2VlIHRoZSBMaWNlbnNlIGZvciB0aGUgc3BlY2lmaWMgbGFuZ3VhZ2UgZ292ZXJuaW5nIHBlcm1pc3Npb25zIGFuZAovLyBsaW1pdGF0aW9ucyB1bmRlciB0aGUgTGljZW5zZS4KCi8qKgogKiBAZmlsZW92ZXJ2aWV3IEhlbHBlcnMgZm9yIGdvb2dsZS5jb2xhYiBQeXRob24gbW9kdWxlLgogKi8KKGZ1bmN0aW9uKHNjb3BlKSB7CmZ1bmN0aW9uIHNwYW4odGV4dCwgc3R5bGVBdHRyaWJ1dGVzID0ge30pIHsKICBjb25zdCBlbGVtZW50ID0gZG9jdW1lbnQuY3JlYXRlRWxlbWVudCgnc3BhbicpOwogIGVsZW1lbnQudGV4dENvbnRlbnQgPSB0ZXh0OwogIGZvciAoY29uc3Qga2V5IG9mIE9iamVjdC5rZXlzKHN0eWxlQXR0cmlidXRlcykpIHsKICAgIGVsZW1lbnQuc3R5bGVba2V5XSA9IHN0eWxlQXR0cmlidXRlc1trZXldOwogIH0KICByZXR1cm4gZWxlbWVudDsKfQoKLy8gTWF4IG51bWJlciBvZiBieXRlcyB3aGljaCB3aWxsIGJlIHVwbG9hZGVkIGF0IGEgdGltZS4KY29uc3QgTUFYX1BBWUxPQURfU0laRSA9IDEwMCAqIDEwMjQ7Ci8vIE1heCBhbW91bnQgb2YgdGltZSB0byBibG9jayB3YWl0aW5nIGZvciB0aGUgdXNlci4KY29uc3QgRklMRV9DSEFOR0VfVElNRU9VVF9NUyA9IDMwICogMTAwMDsKCmZ1bmN0aW9uIF91cGxvYWRGaWxlcyhpbnB1dElkLCBvdXRwdXRJZCkgewogIGNvbnN0IHN0ZXBzID0gdXBsb2FkRmlsZXNTdGVwKGlucHV0SWQsIG91dHB1dElkKTsKICBjb25zdCBvdXRwdXRFbGVtZW50ID0gZG9jdW1lbnQuZ2V0RWxlbWVudEJ5SWQob3V0cHV0SWQpOwogIC8vIENhY2hlIHN0ZXBzIG9uIHRoZSBvdXRwdXRFbGVtZW50IHRvIG1ha2UgaXQgYXZhaWxhYmxlIGZvciB0aGUgbmV4dCBjYWxsCiAgLy8gdG8gdXBsb2FkRmlsZXNDb250aW51ZSBmcm9tIFB5dGhvbi4KICBvdXRwdXRFbGVtZW50LnN0ZXBzID0gc3RlcHM7CgogIHJldHVybiBfdXBsb2FkRmlsZXNDb250aW51ZShvdXRwdXRJZCk7Cn0KCi8vIFRoaXMgaXMgcm91Z2hseSBhbiBhc3luYyBnZW5lcmF0b3IgKG5vdCBzdXBwb3J0ZWQgaW4gdGhlIGJyb3dzZXIgeWV0KSwKLy8gd2hlcmUgdGhlcmUgYXJlIG11bHRpcGxlIGFzeW5jaHJvbm91cyBzdGVwcyBhbmQgdGhlIFB5dGhvbiBzaWRlIGlzIGdvaW5nCi8vIHRvIHBvbGwgZm9yIGNvbXBsZXRpb24gb2YgZWFjaCBzdGVwLgovLyBUaGlzIHVzZXMgYSBQcm9taXNlIHRvIGJsb2NrIHRoZSBweXRob24gc2lkZSBvbiBjb21wbGV0aW9uIG9mIGVhY2ggc3RlcCwKLy8gdGhlbiBwYXNzZXMgdGhlIHJlc3VsdCBvZiB0aGUgcHJldmlvdXMgc3RlcCBhcyB0aGUgaW5wdXQgdG8gdGhlIG5leHQgc3RlcC4KZnVuY3Rpb24gX3VwbG9hZEZpbGVzQ29udGludWUob3V0cHV0SWQpIHsKICBjb25zdCBvdXRwdXRFbGVtZW50ID0gZG9jdW1lbnQuZ2V0RWxlbWVudEJ5SWQob3V0cHV0SWQpOwogIGNvbnN0IHN0ZXBzID0gb3V0cHV0RWxlbWVudC5zdGVwczsKCiAgY29uc3QgbmV4dCA9IHN0ZXBzLm5leHQob3V0cHV0RWxlbWVudC5sYXN0UHJvbWlzZVZhbHVlKTsKICByZXR1cm4gUHJvbWlzZS5yZXNvbHZlKG5leHQudmFsdWUucHJvbWlzZSkudGhlbigodmFsdWUpID0+IHsKICAgIC8vIENhY2hlIHRoZSBsYXN0IHByb21pc2UgdmFsdWUgdG8gbWFrZSBpdCBhdmFpbGFibGUgdG8gdGhlIG5leHQKICAgIC8vIHN0ZXAgb2YgdGhlIGdlbmVyYXRvci4KICAgIG91dHB1dEVsZW1lbnQubGFzdFByb21pc2VWYWx1ZSA9IHZhbHVlOwogICAgcmV0dXJuIG5leHQudmFsdWUucmVzcG9uc2U7CiAgfSk7Cn0KCi8qKgogKiBHZW5lcmF0b3IgZnVuY3Rpb24gd2hpY2ggaXMgY2FsbGVkIGJldHdlZW4gZWFjaCBhc3luYyBzdGVwIG9mIHRoZSB1cGxvYWQKICogcHJvY2Vzcy4KICogQHBhcmFtIHtzdHJpbmd9IGlucHV0SWQgRWxlbWVudCBJRCBvZiB0aGUgaW5wdXQgZmlsZSBwaWNrZXIgZWxlbWVudC4KICogQHBhcmFtIHtzdHJpbmd9IG91dHB1dElkIEVsZW1lbnQgSUQgb2YgdGhlIG91dHB1dCBkaXNwbGF5LgogKiBAcmV0dXJuIHshSXRlcmFibGU8IU9iamVjdD59IEl0ZXJhYmxlIG9mIG5leHQgc3RlcHMuCiAqLwpmdW5jdGlvbiogdXBsb2FkRmlsZXNTdGVwKGlucHV0SWQsIG91dHB1dElkKSB7CiAgY29uc3QgaW5wdXRFbGVtZW50ID0gZG9jdW1lbnQuZ2V0RWxlbWVudEJ5SWQoaW5wdXRJZCk7CiAgaW5wdXRFbGVtZW50LmRpc2FibGVkID0gZmFsc2U7CgogIGNvbnN0IG91dHB1dEVsZW1lbnQgPSBkb2N1bWVudC5nZXRFbGVtZW50QnlJZChvdXRwdXRJZCk7CiAgb3V0cHV0RWxlbWVudC5pbm5lckhUTUwgPSAnJzsKCiAgY29uc3QgcGlja2VkUHJvbWlzZSA9IG5ldyBQcm9taXNlKChyZXNvbHZlKSA9PiB7CiAgICBpbnB1dEVsZW1lbnQuYWRkRXZlbnRMaXN0ZW5lcignY2hhbmdlJywgKGUpID0+IHsKICAgICAgcmVzb2x2ZShlLnRhcmdldC5maWxlcyk7CiAgICB9KTsKICB9KTsKCiAgY29uc3QgY2FuY2VsID0gZG9jdW1lbnQuY3JlYXRlRWxlbWVudCgnYnV0dG9uJyk7CiAgaW5wdXRFbGVtZW50LnBhcmVudEVsZW1lbnQuYXBwZW5kQ2hpbGQoY2FuY2VsKTsKICBjYW5jZWwudGV4dENvbnRlbnQgPSAnQ2FuY2VsIHVwbG9hZCc7CiAgY29uc3QgY2FuY2VsUHJvbWlzZSA9IG5ldyBQcm9taXNlKChyZXNvbHZlKSA9PiB7CiAgICBjYW5jZWwub25jbGljayA9ICgpID0+IHsKICAgICAgcmVzb2x2ZShudWxsKTsKICAgIH07CiAgfSk7CgogIC8vIENhbmNlbCB1cGxvYWQgaWYgdXNlciBoYXNuJ3QgcGlja2VkIGFueXRoaW5nIGluIHRpbWVvdXQuCiAgY29uc3QgdGltZW91dFByb21pc2UgPSBuZXcgUHJvbWlzZSgocmVzb2x2ZSkgPT4gewogICAgc2V0VGltZW91dCgoKSA9PiB7CiAgICAgIHJlc29sdmUobnVsbCk7CiAgICB9LCBGSUxFX0NIQU5HRV9USU1FT1VUX01TKTsKICB9KTsKCiAgLy8gV2FpdCBmb3IgdGhlIHVzZXIgdG8gcGljayB0aGUgZmlsZXMuCiAgY29uc3QgZmlsZXMgPSB5aWVsZCB7CiAgICBwcm9taXNlOiBQcm9taXNlLnJhY2UoW3BpY2tlZFByb21pc2UsIHRpbWVvdXRQcm9taXNlLCBjYW5jZWxQcm9taXNlXSksCiAgICByZXNwb25zZTogewogICAgICBhY3Rpb246ICdzdGFydGluZycsCiAgICB9CiAgfTsKCiAgaWYgKCFmaWxlcykgewogICAgcmV0dXJuIHsKICAgICAgcmVzcG9uc2U6IHsKICAgICAgICBhY3Rpb246ICdjb21wbGV0ZScsCiAgICAgIH0KICAgIH07CiAgfQoKICBjYW5jZWwucmVtb3ZlKCk7CgogIC8vIERpc2FibGUgdGhlIGlucHV0IGVsZW1lbnQgc2luY2UgZnVydGhlciBwaWNrcyBhcmUgbm90IGFsbG93ZWQuCiAgaW5wdXRFbGVtZW50LmRpc2FibGVkID0gdHJ1ZTsKCiAgZm9yIChjb25zdCBmaWxlIG9mIGZpbGVzKSB7CiAgICBjb25zdCBsaSA9IGRvY3VtZW50LmNyZWF0ZUVsZW1lbnQoJ2xpJyk7CiAgICBsaS5hcHBlbmQoc3BhbihmaWxlLm5hbWUsIHtmb250V2VpZ2h0OiAnYm9sZCd9KSk7CiAgICBsaS5hcHBlbmQoc3BhbigKICAgICAgICBgKCR7ZmlsZS50eXBlIHx8ICduL2EnfSkgLSAke2ZpbGUuc2l6ZX0gYnl0ZXMsIGAgKwogICAgICAgIGBsYXN0IG1vZGlmaWVkOiAkewogICAgICAgICAgICBmaWxlLmxhc3RNb2RpZmllZERhdGUgPyBmaWxlLmxhc3RNb2RpZmllZERhdGUudG9Mb2NhbGVEYXRlU3RyaW5nKCkgOgogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAnbi9hJ30gLSBgKSk7CiAgICBjb25zdCBwZXJjZW50ID0gc3BhbignMCUgZG9uZScpOwogICAgbGkuYXBwZW5kQ2hpbGQocGVyY2VudCk7CgogICAgb3V0cHV0RWxlbWVudC5hcHBlbmRDaGlsZChsaSk7CgogICAgY29uc3QgZmlsZURhdGFQcm9taXNlID0gbmV3IFByb21pc2UoKHJlc29sdmUpID0+IHsKICAgICAgY29uc3QgcmVhZGVyID0gbmV3IEZpbGVSZWFkZXIoKTsKICAgICAgcmVhZGVyLm9ubG9hZCA9IChlKSA9PiB7CiAgICAgICAgcmVzb2x2ZShlLnRhcmdldC5yZXN1bHQpOwogICAgICB9OwogICAgICByZWFkZXIucmVhZEFzQXJyYXlCdWZmZXIoZmlsZSk7CiAgICB9KTsKICAgIC8vIFdhaXQgZm9yIHRoZSBkYXRhIHRvIGJlIHJlYWR5LgogICAgbGV0IGZpbGVEYXRhID0geWllbGQgewogICAgICBwcm9taXNlOiBmaWxlRGF0YVByb21pc2UsCiAgICAgIHJlc3BvbnNlOiB7CiAgICAgICAgYWN0aW9uOiAnY29udGludWUnLAogICAgICB9CiAgICB9OwoKICAgIC8vIFVzZSBhIGNodW5rZWQgc2VuZGluZyB0byBhdm9pZCBtZXNzYWdlIHNpemUgbGltaXRzLiBTZWUgYi82MjExNTY2MC4KICAgIGxldCBwb3NpdGlvbiA9IDA7CiAgICB3aGlsZSAocG9zaXRpb24gPCBmaWxlRGF0YS5ieXRlTGVuZ3RoKSB7CiAgICAgIGNvbnN0IGxlbmd0aCA9IE1hdGgubWluKGZpbGVEYXRhLmJ5dGVMZW5ndGggLSBwb3NpdGlvbiwgTUFYX1BBWUxPQURfU0laRSk7CiAgICAgIGNvbnN0IGNodW5rID0gbmV3IFVpbnQ4QXJyYXkoZmlsZURhdGEsIHBvc2l0aW9uLCBsZW5ndGgpOwogICAgICBwb3NpdGlvbiArPSBsZW5ndGg7CgogICAgICBjb25zdCBiYXNlNjQgPSBidG9hKFN0cmluZy5mcm9tQ2hhckNvZGUuYXBwbHkobnVsbCwgY2h1bmspKTsKICAgICAgeWllbGQgewogICAgICAgIHJlc3BvbnNlOiB7CiAgICAgICAgICBhY3Rpb246ICdhcHBlbmQnLAogICAgICAgICAgZmlsZTogZmlsZS5uYW1lLAogICAgICAgICAgZGF0YTogYmFzZTY0LAogICAgICAgIH0sCiAgICAgIH07CiAgICAgIHBlcmNlbnQudGV4dENvbnRlbnQgPQogICAgICAgICAgYCR7TWF0aC5yb3VuZCgocG9zaXRpb24gLyBmaWxlRGF0YS5ieXRlTGVuZ3RoKSAqIDEwMCl9JSBkb25lYDsKICAgIH0KICB9CgogIC8vIEFsbCBkb25lLgogIHlpZWxkIHsKICAgIHJlc3BvbnNlOiB7CiAgICAgIGFjdGlvbjogJ2NvbXBsZXRlJywKICAgIH0KICB9Owp9CgpzY29wZS5nb29nbGUgPSBzY29wZS5nb29nbGUgfHwge307CnNjb3BlLmdvb2dsZS5jb2xhYiA9IHNjb3BlLmdvb2dsZS5jb2xhYiB8fCB7fTsKc2NvcGUuZ29vZ2xlLmNvbGFiLl9maWxlcyA9IHsKICBfdXBsb2FkRmlsZXMsCiAgX3VwbG9hZEZpbGVzQ29udGludWUsCn07Cn0pKHNlbGYpOwo=",
              "ok": true,
              "headers": [
                [
                  "content-type",
                  "application/javascript"
                ]
              ],
              "status": 200,
              "status_text": "OK"
            }
          },
          "base_uri": "https://localhost:8080/",
          "height": 77
        },
        "outputId": "46a5b92a-d682-4cdf-8285-aba9d7387f22"
      },
      "source": [
        "import pandas as pd\n",
        "import io\n",
        "import matplotlib.pyplot as plt\n",
        "from google.colab import files\n",
        "uploaded = files.upload()\n",
        "df = pd.read_csv(io.BytesIO(uploaded['Salaries.csv']))"
      ],
      "execution_count": 104,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "text/html": [
              "\n",
              "     <input type=\"file\" id=\"files-08ee1230-5744-4069-82ff-eeae79dd0e09\" name=\"files[]\" multiple disabled />\n",
              "     <output id=\"result-08ee1230-5744-4069-82ff-eeae79dd0e09\">\n",
              "      Upload widget is only available when the cell has been executed in the\n",
              "      current browser session. Please rerun this cell to enable.\n",
              "      </output>\n",
              "      <script src=\"/nbextensions/google.colab/files.js\"></script> "
            ],
            "text/plain": [
              "<IPython.core.display.HTML object>"
            ]
          },
          "metadata": {
            "tags": []
          }
        },
        {
          "output_type": "stream",
          "text": [
            "Saving Salaries.csv to Salaries (8).csv\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "X4ftUFZAuKr8",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 121
        },
        "outputId": "1cf9423b-cc2d-4957-d61c-f6d7ae35acd5"
      },
      "source": [
        "#1. Which Male and Female Professor has the highest and the lowest salaries\n",
        "d1=df[(df['sex']=='Male') & (df['rank']=='Prof')]\n",
        "d2=df[(df['sex']=='Female') & (df['rank']=='Prof')]\n",
        "print('For male professors :\\nHighest salary is =',d1['salary'].max(),'\\nLowest salary is =',d1['salary'].min())\n",
        "print('For female professors :\\nHighest salary is =',d2['salary'].max(),'\\nLowest salary is =',d2['salary'].min())"
      ],
      "execution_count": 105,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "For male professors :\n",
            "Highest salary is = 186960.0 \n",
            "Lowest salary is = 57800.0\n",
            "For female professors :\n",
            "Highest salary is = 161101.0 \n",
            "Lowest salary is = 90450.0\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "ND8AuW8juq5B",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 69
        },
        "outputId": "1fefc37a-fa9d-49d2-be50-a14f745d38cf"
      },
      "source": [
        "#2. Which Professor takes the highest and lowest salaries.\n",
        "d3=df[(df['rank']=='Prof')]\n",
        "print('For professors :\\nHighest salary is =',d3['salary'].max(),'\\nLowest salary is =',d3['salary'].min())"
      ],
      "execution_count": 106,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "For professors :\n",
            "Highest salary is = 186960.0 \n",
            "Lowest salary is = 57800.0\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "3sCZFnWTuse8",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "#3. Missing Salaries - should be mean of the matching salaries of those whose service is the same"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "skGfaA-Tu3_m",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "#4. Missing phd - should be mean of the matching service "
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "e9XmZcTiu6aC",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 509
        },
        "outputId": "8dfce628-e821-445a-95f1-a2cd0748a800"
      },
      "source": [
        "#5. How many are Male Staff and how many are Female Staff. \n",
        "\n",
        "#Show both in numbers and Graphically using Pie Chart.  \n",
        "\n",
        "print('number of staff :\\n',df['sex'].value_counts(),'\\n\\nPie chart :')\n",
        "df.sex.value_counts().plot.pie()\n",
        "plt.show()\n",
        "\n",
        "#Show both numbers and in percentage\n",
        "\n",
        "print('number of staff :\\n',df['sex'].value_counts(),'\\n\\nPercentage :\\n',df['sex'].value_counts(normalize=True)*100)\n"
      ],
      "execution_count": 119,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "number of staff :\n",
            " Male      39\n",
            "Female    39\n",
            "Name: sex, dtype: int64 \n",
            "\n",
            "Pie chart :\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "display_data",
          "data": {
            "image/png": "iVBORw0KGgoAAAANSUhEUgAAAPUAAADnCAYAAADGrxD1AAAABHNCSVQICAgIfAhkiAAAAAlwSFlz\nAAALEgAACxIB0t1+/AAAADh0RVh0U29mdHdhcmUAbWF0cGxvdGxpYiB2ZXJzaW9uMy4yLjAsIGh0\ndHA6Ly9tYXRwbG90bGliLm9yZy8GearUAAARVklEQVR4nO3dfbQcdX3H8feXJJCU4pUHkaDYUcCi\nUNES0IAeQ9Fqu4pVcopS8QEQFKuitTiIyiiI61M51lNUEIpKpXgAJTAoaCE+gDzLg5ECQldAErU8\nDBAwCcn0j5lbLpe9uZub3f3O77ef1zl7LnvvXeaTZD7397uzM7+xsiwRkXhs4h1ARPpLpRaJjEot\nEhmVWiQyKrVIZFRqkcio1CKRUalFIqNSi0RGpRaJjEotEhmVWiQyKrVIZFRqkcio1PL/zKw0szMn\nPJ9tZn8wswuned2i6b5HhkellolWAruZ2bz6+auB3zrmkRlQqWWyi4BW/d9vAc4a/4KZ7WVmPzez\nX5jZFWb255NfbGabm9npZnZ1/X1vGFJuqanUMtl/Am82s7nAi4CrJnztv4FXlGX5EuATwIldXn8s\ncGlZlnsB+wKfN7PNB5xZJpjtHUCapSzLm8wsoRqlL5r05THgG2a2M1ACc7r8L/4a2N/MPlw/nws8\nB7hlIIHlKVRq6WYJ8AVgEbD1hM8fD1xWluUb6+Iv7fJaAw4oy/LWwUaUqWj6Ld2cDnyyLMubJ31+\njCcOnL1jitdeDLzPzAzAzF4ykIQyJZVanqIsy3vKsvzXLl/6HPAZM/sFU8/yjqealt9kZsvq5zJE\npiWCReKikVokMiq1SGRUapHIqNQikdH71BFK0nxTYP6Ex/aTPj4TmEf17z/+AHi8fqyhOg98BbAc\nuLfLx9912q21w/kTyYbQ0e/AJWm+JfCXwB7Agvrjc6lOAhmktcCtwLXAdfXjhk67tXLA25VpqNQB\nSdJ8FrAQ2JsnCvw811BPto7q/PDxov+00279wjfS6FGpGy5J8y2A1wKvB/6WJ5+2GYK7gQupTj29\ntNNurXbOEz2VuoGSNN8B2L9+LAI2dQ3UPw8Dl1AVPO+0W/c554mSSt0QSZrPAw4CjgD2dI4zDGuB\nS4GvAufroFv/qNTOkjTfGTgSeDuwpXMcL/cApwKndNqtFd5hQqdSO6gPeO1PVeb9GPyR6lCsAb4L\nnNxpt37sHSZUKvUQJWk+F/hH4APAs53jNN0y4PPAtzrt1jrvMCFRqYegHpnfCWTAs3zTBOeXwLGd\ndmuJd5BQqNQDlqT5AcAJwC7eWQJ3OZB22q2feQdpOpV6QJI03xdoA3t5Z4lMDhzTabcmr8oiNZW6\nz5I0fx5wMvAa7ywRWwd8C/hQp9263ztM06jUfZKkuQHvpRqdtSTucPwOeHen3fqed5AmUan7oB6d\nT6M6+0uG79vA+zRqV1TqjaDRuVE0atdU6hnS6NxYIz9qq9QzkKT5YuAMNDo31XLgTZ1260rvIB5U\n6g1QT7cz4OPo1M6mWwUc3mm3vukdZNhU6h4lab458E3gTd5ZZIP8C3D0KF0FplL3IEnzBDif6i6Q\nEp6LgTd32q0HvYMMg0o9jSTNXwmcA2zjnUU2ym3A/p12K/ob92mJ4PVI0vww4Ieo0DF4PnBVkuav\n8g4yaCr1FJI0P4rqwv1u92CWMI0BFyZp/nrvIIOkUneRpHkKnOSdQwZiM+Dc+uq5KKnUkyRpfhzw\nGe8cMlBzgLOTNH+Ld5BB0IGyCZI0/yjwae8cMjRrqY6Kn+MdpJ9U6lqS5h+kek9TRssa4IBOu3WB\nd5B+UamBJM2PoFqqVkbTKuB1nXbrR95B+mHkS52k+auB7wOzvLOIqwJ4aQzvY490qZM03wm4mtFd\nb1ue7DaqYgd95tnIHv1O0vxpVLd/UaFl3POBs+rVX4M1kqVO0nwTqutuX+CdRRrntcDnvENsjJEs\nNXAi0PIOIY31oSTN3+YdYqZG7nfqJM0PAv7DO4c03irglZ126yrvIBtqpEqdpPmuVDdEn+udRYKw\nHNgttKWRRmb6naT5bKoliFRo6dV84MveITbUyJQaOBpY4B1CgnNQkuZ/5x1iQ4zE9Luedl8PbOqd\nRYK0Atg1lGl49CP1hGm3Ci0ztR0BTcOjLzWadkt/BDMNj3r6rWm39FkQ0/BoR+p6je7TUKGlf7YD\nvugdYjrRlhpYDLzUO4RE521Jmv+Fd4j1ibLU9cGxE7xzSJQ2oTrNuLGiLDVwCNUVNyKD8LokzV/u\nHWIq0ZU6SfN5wHHeOSR6be8AU4mu1MD7ge29Q0j09mnq+uFRvaWVpPmWwJ3A072zyEj4JbB7p91a\n5x1kothG6o+gQsvw7Aa81TvEZNGUOknzPwWO9M4hI+do7wCTRVNq4GBgC+8QMnJ2re+M2hgxlfo9\n3gFkZDVqhhjFgbIkzV8B/MQ7h4ysNcBzOu3WCu8gEM9I3aiflDJy5gDv8g4xLviROknzZwJ3oQs3\nxNc9QNJpt9Z6B4lhpD4MFVr8PRvY3zsEBF7qelH+w71ziNQacbA26FJTXVr5HO8QIrW/StJ8K+8Q\noZe6EdMdkdosGnDnF5VapL/c98lgj34nab4j8GvvHCKTPAxs02m3VnsFCHmkdv+JKNLFFsC+ngFU\napH+c903gyx1fd10Y5eTkZHnunhCkKUG/gaY7R1CZAo7JGn+Yq+Nh1rqV3gHEJmG2z4aaqn38A4g\nMg23Wz0FV+okzecAL/LOITINt4EnuFJTrQu1mXcIkWnskqT5n3hsOMRSa+otIZgFuBwsU6lFBsdl\nX1WpRQbH5WBZUKXWQTIJjEbqHuyEDpJJOHZJ0nzWsDcaWql1jywJySxg22FvVKUWGayh77OhlXq+\ndwCRDTT0fTa0UmukltBopJ6GRmoJjUbqaWikltA0c6Q2s0MnPZ9lZscNJtJ6aaSW0DR2pN7PzC4y\ns/lmtitwJT63jd3OYZsiG2Pope5p9ZCyLA8yswOBm4GVwEFlWV4+0GTdbe6wTZGNMfQrtXqdfu8M\nfAA4F/gNcLCZDTVskuZavkhCNGfYG+x1+n0B8ImyLI8AXgncDlwzsFTdqdQSoqHvt71ucK+yLB8C\nKKvV/79oZhcMLlZXKrWEqLGlnmdmJwHPKsvytWb2QmAhcNvgoj3Z9ZsdUT6dR+4f1vZE+mEd9hA8\nMNRt9lrqM4B/B46tn98GnA2cNoBMXW1lD68F3O8oKLIhNqEshr/N3mxTluV3gHUAZVk+DqwdWKru\nHh/y9kT6Yej7ba+lXmlmWwMlgJm9DBjuT6CsUKklREPfb3udfn8IWALsaGaXA88AFg8s1dT+CMx1\n2K7ITP1x2BvsdaTekepWN3sDF1O9peVxNPp3DtsU2Rgrhr3BXkv98fotrS2pbtN5MvCVgaWa2nKH\nbYpsjKHvs72WevygWAs4tSzLHNh0MJHW616HbYpsjKHvs72W+rdm9jXgQOAiM9tsA17bTxqpJTSN\nHan/nup36deUZfkg1fvF/zywVFPTSC2hGfo+2+tVWo8C5014vhyfUVMjtYSmsSN1U6jUEhqVehqa\nfktISlTqaf2a4Z+eKjJTd5IVa4a90bBKnRWPArd4xxDp0XUeGw2r1JVrvQOI9Eil7pHLX5TIDLgM\nQCq1yOBc77HREEt9IzpYJs13B1nxoMeGwyu1DpZJGNxmlOGVuqKDZdJ0KvUGusI7gMg03PbRUEud\nUy+tJNJA/wv83GvjYZY6K+5FR8GluS4iK9wO5oZZ6soS7wAiU3DdN0Mu9bDvECLSi1VUaw+4CbfU\nWXEDcJd3DJFJlpIVj3gGCLfUFY3W0jTuvxaGXmr3v0CRSdz3ydBLvRTQTfOkKa4mK+7xDhF2qbNi\nNdWN+0Sa4GveASD0Ule+gk5EEX8PAGd5h4AYSp0VdwCXeMeQkXcGWfGYdwiIodSVk70DyEgr8bkN\nVVexlPpC4DfeIWRk/YisuN07xLg4Sp0V64BTvGPIyGrUTDGOUle+Dqz2DiEj524adhJUPKXOit8D\nZ3rHkJHzJc8rsrqJp9SVjOqEepFhuAf4N+8Qk8VV6qy4mwb+JUu0MrLij94hJour1JUTgYe8Q0j0\nbgHO8A7RTXylzor7gM97x5Dofaxpv0uPi6/UlZOAFd4hJFpXkRXnTf9tPuIsdVasBI73jiHRSr0D\nrE+cpa6cSnXrW5F++gFZsdQ7xPrEW+rqvsCHoyu4pH9WAkd6h5hOvKUGyIrLaNCJ9hK8j5AV/+Md\nYjpxl7pyNND4fwhpvMto2DneU4m/1NVBs0PRNFxmrtqHsiKIfSj+UoOm4bKxgph2jxuNUlc0DZeZ\nCGbaPW50Sl1Nww9B03Dp3SMENO0eNzqlBur3Fz/hHUOCUAJvD2naPW60Sg2QFScA3/GOIY33qSaf\nCro+o1fqyjuB671DSGOdC3zSO8RMWVkG9etC/2RjOwDXAM/0jiKNciOwT30MJkijOlKPL6hwAFrX\nTJ7wB+ANIRcaRrnUAFlxOfAe7xjSCGuAxWRF8EtNj3apAbLidOCL3jHE3XvIip94h+gHlRogKz4M\nfNU7hrg5iqw4zTtEv6jUTziShq45JQOVkhVf8g7RTyr1uOqsoUOBb3tHkaE5jqz4rHeIflOpJ6pu\n33MwGrFHwTFkxae8QwyCSj1ZVexDaMgNxGUgPkhWtL1DDMronnzSi2zsC8A/eceQvlkLvJesiPoH\ntko9nWzsEKprsTf1jiIb5X7gQLLiR95BBk2l7kU2tjdwHjqlNFS/ojpTbCRWl9Xv1L3IiiuAPdFF\nICG6EHjZqBQaVOreVeeKvxw42zuK9KxNNUI/7B1kmDT9nols7FiqO4CYdxTp6jGqFUvO8g7iQaWe\nqWxsEXA68FznJPJk1wDvJCuWeQfxoun3TFVLI72IalE6/WT0twr4KLBwlAsNGqn7IxvbFzgNjdpe\nRn50nkgjdT9U64pr1B4+jc5daKTut2rUPgXYyTtK5K4EDlOZn0qlHoRsbA7wLuDjwHbOaWJzK/Ax\nsuIc7yBNpVIPUja2OXAU1d1BnuacJnS/pVrh83SyYq13mCZTqYchG9saOAZ4LzDXOU1oHqA6ieTL\nZMVj3mFCoFIPU7Us8XFU12zrApH1e4jqwONnyYoHvcOERKX2kI1tS7XKyhHAnzmnaZqbqK6KO5Os\neMQ7TIhUak/Z2CZAi2p9tNcwuqedrqa6K8bJZMXPvMOETqVuimxsR+DdVLcE2to5zbDcRbXCzNfJ\nit97h4mFSt001dthi4D9gdcT3/R8GbCkflwV2m1iQ6BSN102tjtPFHwB4U3RHwd+yniRs+JO5zzR\nU6lDko3NB14H7A3sAbwQmOWa6alWUR3supaqzN/X0evhUqlDlo3NA3anKvgChl/0iQW+rn4sIyvW\nDGn70oVKHZuq6DsB2wPz68f2kz5ux/pPgimBR4Hl9ePeLh/vBe5QgZtHpR5l2dgsYDYwh6rIjwOP\n6zTMsKnUIpHR9dQikVGpRSKjUotERqV2ZGZrzeyGCY9kgNvqmNk2g/r/S3PM9g4w4h4ry/LF3iEk\nLhqpG8bM9jCzH5vZdWZ2sZnNrz+/1MxOMrNrzewWM9vTzM4zs9vN7IQJr/9e/dplZnb4FNt4q5ld\nXc8OvmZmTTsrTTaCSu1r3oSp93fNbA7wZWBxWZZ7UN0s4NMTvn91WZYLgK8C51OtpLIb8A4zG7+y\n65D6tQuA90/4PABm9gLgQGCfepawFviHAf4ZZcg0/fb1pOm3me1GVdIfmhlUp3sun/D9S+qPNwPL\nyrJcXr/uTmAH4D6qIr+x/r4dgJ3rz4/bj+p00mvqbcwDdNljRFTqZjGqsi6c4uur6o/rJvz3+PPZ\nZrYIeBWwsCzLR81sKU89HdSAb5RleUzfUkujaPrdLLcCzzCzhQBmNsfMdt2A148BD9SF3gV4WZfv\n+S9gsZltW29jKzOL7ZrtkaZSN0hZlquBxcBnzexG4Aaqyyx79QOqEfsWqhU4r+yyjV8BHwMuMbOb\ngB9SXeQhkdC53yKR0UgtEhmVWiQyKrVIZFRqkcio1CKRUalFIqNSi0RGpRaJjEotEhmVWiQyKrVI\nZFRqkcio1CKRUalFIqNSi0Tm/wCjPIy77xw0qwAAAABJRU5ErkJggg==\n",
            "text/plain": [
              "<Figure size 432x288 with 1 Axes>"
            ]
          },
          "metadata": {
            "tags": []
          }
        },
        {
          "output_type": "stream",
          "text": [
            "number of staff :\n",
            " Male      39\n",
            "Female    39\n",
            "Name: sex, dtype: int64 \n",
            "\n",
            "Percentage :\n",
            " Male      50.0\n",
            "Female    50.0\n",
            "Name: sex, dtype: float64\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "sRrW0LVcu-W1",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 370
        },
        "outputId": "091c9f59-217f-4f86-b56b-1200fda61042"
      },
      "source": [
        "#6. How many are Prof, AssocProf and AsstProf. Show both in numbers adn Graphically using a Pie Chart\n",
        "print('number of staff :\\n',df['rank'].value_counts(),'\\n\\nPie chart :')\n",
        "df['rank'].value_counts().plot.pie()\n",
        "plt.show()\n"
      ],
      "execution_count": 122,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "number of staff :\n",
            " Prof         46\n",
            "AsstProf     19\n",
            "AssocProf    13\n",
            "Name: rank, dtype: int64 \n",
            "\n",
            "Pie chart :\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "display_data",
          "data": {
            "image/png": "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\nQmCC\n",
            "text/plain": [
              "<Figure size 432x288 with 1 Axes>"
            ]
          },
          "metadata": {
            "tags": []
          }
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "q6KBbiB1vJc3",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "#7. Who are the senior and junior most employees in the organization."
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "vHkSnfbNvKx0",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "#8. Draw a histogram of the salaries divided into bin starting from 50K and increment of 15K"
      ],
      "execution_count": 0,
      "outputs": []
    }
  ]
}