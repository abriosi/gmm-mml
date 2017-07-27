#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 24 21:43:48 2017

@author: abriosi
"""

# Import datasets, classifiers and performance metrics
from sklearn.datasets import make_blobs
import matplotlib.pyplot as plt
import MDL_GMM

X,y=make_blobs(n_samples=1000, n_features=2, centers=5, random_state=1338)

plt.title('Blob Data')
plt.scatter(X[:,0],X[:,1],alpha=0.2,s=10)
plt.show()

unsupervised=MDL_GMM.MDL_GMM(threshold=1e-4,
                             live_2d_plot=False,
                             check_plot=True,
                             max_iters=1000, 
                             regularize=1e-5)
unsupervised.fit(X)
samples=unsupervised.sample(1000)

plt.title('Sampled from GMM')
plt.scatter(samples[:,0],samples[:,1],alpha=0.2,s=10)
plt.show()