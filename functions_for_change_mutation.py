# -*- coding: utf-8 -*-
"""Functions for change mutation.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1GXoRlj-3ro0wbQHRUCu03rNf_clB5Rxk
"""

#Mutacja przez zamianę

def change_mut(ind):
    index1 = random.randint(0,len(ind)-1)
    index2 = random.randint(0,len(ind)-1)
    ind[index1],ind[index2] = ind[index2],ind[index1]


def mutation_change(pop, pm_change):  #mutacja dostaje na wejściu populację i prawdopodobieństwo mutacji (mutować czy nie mutować)
    for ind in pop:
        if random.random()<pm_change:
            change_mut(ind)