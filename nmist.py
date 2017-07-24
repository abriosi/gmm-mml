#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 24 21:43:48 2017

@author: abriosi
"""

# Import datasets, classifiers and performance metrics
from sklearn import datasets
import matplotlib.pyplot as plt
import MDL_GMM

# The digits dataset
digits = datasets.load_digits()

X = digits.data
y = digits.target

images_and_labels = list(zip(digits.images, digits.target))
for index, (image, label) in enumerate(images_and_labels[:4]):
    plt.subplot(2, 4, index + 1)
    plt.axis('off')
    plt.imshow(image, cmap=plt.cm.gray_r, interpolation='nearest')
    plt.title('Digit: %i' % label)
plt.show()
  
    

unsupervised=MDL_GMM.MDL_GMM(threshold=1e-4,
                             live_2d_plot=False,
                             max_iters=100, 
                             regularize=1e-6)
unsupervised.fit(X)
samples=unsupervised.sample(10)


images_and_labels = list(zip(samples.reshape(len(samples),8,8), digits.target))
for index, (image, label) in enumerate(images_and_labels[:4]):
    plt.subplot(2, 4, index + 1)
    plt.axis('off')
    plt.imshow(image, cmap=plt.cm.gray_r, interpolation='nearest')
    plt.title('Digit: %i' % label)
plt.show()