#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 24 21:43:48 2017

@author: abriosi
"""

# Import datasets, classifiers and performance metrics
from sklearn.datasets import make_circles
import matplotlib.pyplot as plt
import MDL_GMM
X,y=make_circles(n_samples=2000, shuffle=True, noise=0.1, random_state=1337, factor=0.4)

plt.title('Circle Data')
plt.scatter(X[:,0],X[:,1],alpha=0.2,s=10)
plt.show()

unsupervised=MDL_GMM.MDL_GMM(threshold=1e-4,
                             live_2d_plot=False,
                             check_plot=True,
                             max_iters=1000, 
                             regularize=0)
unsupervised.fit(X)
samples=unsupervised.sample(10000)

plt.title('Sampled from GMM')
plt.scatter(samples[:,0],samples[:,1],alpha=0.2,s=10)
plt.show()

