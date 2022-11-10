import urllib

import bs4

lst1 = [1, 2, 93, 3, 4, 56, 34, 22, 59, 34, 24, 23, 11, 74, 12, 22, 5, 6, 7, 8,
        9, 10, 99, 100]


def bubble_sort(lst):
    for i in range(len(lst)):
        swap = False
        for j in range(len(lst) - i - 1):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
                swap = True
            if not swap:
                break
    return lst


def bubbleSort(theSeq):
    n = len(theSeq)

    for i in range(n - 1):
        flag = 0

        for j in range(n - 1):

            if theSeq[j] > theSeq[j + 1]:
                temp = theSeq[j]
                theSeq[j] = theSeq[j + 1]
                theSeq[j + 1] = temp
                flag = 1

        if flag == 0:
            break

    return theSeq


result_1 = bubble_sort(lst1)

result = bubbleSort(lst1)

print(result)
print(result_1)

newlist = []
for i in list:
    s = {}  # make an empty dict to store new dict data
    for k in i.keys():  # to get keys in the dict of the list
        s[k] = int(i[k])  # change the values from string to int by int func
    newlist.append(s)


def google_alg_for_sherch():
    {
        "cells": [
            {
                "cell_type": "code",
                "execution_count": 2,
                "metadata": {},
                "outputs": [],
                "source": [
                    "import numpy as np"
                ]
            },
            {
                "cell_type": "markdown",
                "metadata": {},
                "source": [
                    "Define the matrices A, B and the transition matrix $T=0.15*A + 0.85*B$"
                ]
            },
            {
                "cell_type": "code",
                "execution_count": 3,
                "metadata": {},
                "outputs": [],
                "source": [
                    "A = 0.25*np.ones((4,4))\n",
                    "B = np.array([[0, 0, 0, 0],\n",
                    "             [0.5, 0, 0, 0],\n",
                    "             [0.5, 1, 0, 1],\n",
                    "             [0, 0, 1, 0]])\n",
                    "T = 0.15*A + 0.85*B"
                ]
            },
            {
                "cell_type": "code",
                "execution_count": 5,
                "metadata": {
                    "scrolled": True
                },
                "outputs": [
                    {
                        "data": {
                            "text/plain": [
                                "array([[0.0375, 0.0375, 0.0375, 0.0375],\n",
                                "       [0.4625, 0.0375, 0.0375, 0.0375],\n",
                                "       [0.4625, 0.8875, 0.0375, 0.8875],\n",
                                "       [0.0375, 0.0375, 0.8875, 0.0375]])"
                            ]
                        },
                        "execution_count": 5,
                        "metadata": {},
                        "output_type": "execute_result"
                    }
                ],
                "source": [
                    "T"
                ]
            },
            {
                "cell_type": "markdown",
                "metadata": {},
                "source": [
                    "Find the eigenvalues and eigenvectors of $T$"
                ]
            },
            {
                "cell_type": "code",
                "execution_count": 28,
                "metadata": {},
                "outputs": [],
                "source": [
                    "w,v = np.linalg.eig(T)"
                ]
            },
            {
                "cell_type": "markdown",
                "metadata": {},
                "source": [
                    "The eigenvector which corresponds to the eigenvalue one, normalized by as a probability distribution, is"
                ]
            },
            {
                "cell_type": "code",
                "execution_count": 35,
                "metadata": {},
                "outputs": [
                    {
                        "data": {
                            "text/plain": [
                                "array([0.0375    , 0.0534375 , 0.47111486, 0.43794764])"
                            ]
                        },
                        "execution_count": 35,
                        "metadata": {},
                        "output_type": "execute_result"
                    }
                ],
                "source": [
                    "stationary_state_vec = np.real(v.T[0]/np.linalg.norm(v.T[0], ord=1))\n",
                    "stationary_state_vec"
                ]
            },
            {
                "cell_type": "markdown",
                "metadata": {},
                "source": [
                    "The PageRank order is then"
                ]
            },
            {
                "cell_type": "code",
                "execution_count": 49,
                "metadata": {},
                "outputs": [
                    {
                        "name": "stdout",
                        "output_type": "stream",
                        "text": [
                            "P3, P4, P2, P1\n"
                        ]
                    }
                ],
                "source": [
                    "print('P' + ', P'.join(map(str, np.argsort(-stationary_state_vec)+1)))"
                ]
            },
            {
                "cell_type": "markdown",
                "metadata": {},
                "source": [
                    "The 15% is necessary so that the chain is irreducible and aperiodic. Otherwise, some pages may not be connected to the rest, and the chain may not have a unique stationary distribution to which it converges."
                ]
            },
            {
                "cell_type": "markdown",
                "metadata": {},
                "source": [
                    "Now we act with the matrix $T^k$ on the initial state vector $\\vec{x}_0=(1,0,0,0)^T$ for increasing values of $k$ and compare the result for $T^k \\vec{x}_0$ and $T^{k-1} \\vec{x}_0$ up to the fourth decimal place."
                ]
            },
            {
                "cell_type": "code",
                "execution_count": 72,
                "metadata": {},
                "outputs": [
                    {
                        "name": "stdout",
                        "output_type": "stream",
                        "text": [
                            "1 False\n",
                            "2 False\n",
                            "3 False\n",
                            "4 False\n",
                            "5 False\n",
                            "6 False\n",
                            "7 False\n",
                            "8 False\n",
                            "9 False\n",
                            "10 False\n",
                            "11 False\n",
                            "12 False\n",
                            "13 False\n",
                            "14 False\n",
                            "15 False\n",
                            "16 False\n",
                            "17 False\n",
                            "18 False\n",
                            "19 False\n",
                            "20 False\n",
                            "21 False\n",
                            "22 False\n",
                            "23 False\n",
                            "24 False\n",
                            "25 False\n",
                            "26 False\n",
                            "27 False\n",
                            "28 False\n",
                            "29 False\n",
                            "30 False\n",
                            "31 False\n",
                            "32 False\n",
                            "33 False\n",
                            "34 False\n",
                            "35 False\n",
                            "36 False\n",
                            "37 False\n",
                            "38 False\n",
                            "39 False\n",
                            "40 False\n",
                            "41 False\n",
                            "42 False\n",
                            "43 False\n",
                            "44 False\n",
                            "45 False\n",
                            "46 True\n",
                            "47 True\n",
                            "48 True\n",
                            "49 True\n",
                            "50 True\n",
                            "51 True\n",
                            "52 True\n",
                            "53 True\n",
                            "54 True\n",
                            "55 True\n",
                            "56 True\n",
                            "57 True\n",
                            "58 True\n",
                            "59 True\n",
                            "60 True\n",
                            "61 True\n",
                            "62 True\n",
                            "63 True\n",
                            "64 True\n",
                            "65 True\n",
                            "66 True\n",
                            "67 True\n",
                            "68 True\n",
                            "69 True\n",
                            "70 True\n",
                            "71 True\n",
                            "72 True\n",
                            "73 True\n",
                            "74 True\n",
                            "75 True\n",
                            "76 True\n",
                            "77 True\n",
                            "78 True\n",
                            "79 True\n",
                            "80 True\n",
                            "81 True\n",
                            "82 True\n",
                            "83 True\n",
                            "84 True\n",
                            "85 True\n",
                            "86 True\n",
                            "87 True\n",
                            "88 True\n",
                            "89 True\n",
                            "90 True\n",
                            "91 True\n",
                            "92 True\n",
                            "93 True\n",
                            "94 True\n",
                            "95 True\n",
                            "96 True\n",
                            "97 True\n",
                            "98 True\n",
                            "99 True\n"
                        ]
                    }
                ],
                "source": [
                    "for i in range(1,100):\n",
                    "    print(i, np.allclose(np.linalg.matrix_power(T,i) @ np.array([1,0,0,0]),np.linalg.matrix_power(T,i-1) @ np.array([1,0,0,0]),atol=10**-5))"
                ]
            },
            {
                "cell_type": "markdown",
                "metadata": {},
                "source": [
                    "We see that starting from $k=46$ the result is converged up to the fourth decimal place. And indeed $T^{46} \\vec{x}_0$ is equal to the eigenvector we found earlier:"
                ]
            },
            {
                "cell_type": "code",
                "execution_count": 75,
                "metadata": {},
                "outputs": [
                    {
                        "data": {
                            "text/plain": [
                                "True"
                            ]
                        },
                        "execution_count": 75,
                        "metadata": {},
                        "output_type": "execute_result"
                    }
                ],
                "source": [
                    "np.allclose(np.linalg.matrix_power(T,46) @ np.array([1,0,0,0]), stationary_state_vec, atol=10**-5)"
                ]
            },
            {
                "cell_type": "code",
                "execution_count": null,
                "metadata": {},
                "outputs": [],
                "source": []
            }
        ],
        "metadata": {
            "kernelspec": {
                "display_name": "Python 3",
                "language": "python",
                "name": "python3"
            },
            "language_info": {
                "codemirror_mode": {
                    "name": "ipython",
                    "version": 3
                },
                "file_extension": ".py",
                "mimetype": "text/x-python",
                "name": "python",
                "nbconvert_exporter": "python",
                "pygments_lexer": "ipython3",
                "version": "3.7.7"
            }
        },
        "nbformat": 4,
        "nbformat_minor": 4
    return



# full_url = urllib.parse.urljoin(base_url, relative_url)


def active_crawl(base_url, index_file, out_file):
    """
    this func is activating the crawl call from the main.
    :param base_url: the url that is being used as a sours.
    :param index_file: a file that contains all of the information
    about that page and his data base html.
    :param out_file: the return file after the changes.
    :return:the action regarding activating crawl from the commend line.
    """
    base_line = base_url
    filer = reada(index_file)
    dicter = dict_create(filer)
    for line in filer:
        soup = bs4.BeautifulSoup(urllib.parse.urljoin(base_url, line))
        for line2 in filer:
            dicter.get(line).update([line2, soup.find_all(line2).size()])
    return out_file


def reada(index_file):
    return open(index_file, 'r'), splitlines()


def minidict(lost):
    returner = dict()
    for line in lost:
        returner.update([line, 0])
    return returner


def dict_create(lost):
    returner = dict()
    for line in lost:
        returner.update([line, minidict(lost)])
    return returner