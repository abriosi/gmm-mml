#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 28 00:00:09 2017

@author: abriosi
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import multivariate_normal
from mdl_gmm import MdlGmm

def sample_GMM(means,covs,probs,samples):
    output=[]    
    means=np.array(means)
    covs=np.array(covs)
    select_sample=np.random.multinomial(samples, probs)
    gmm=0
    for i in select_sample:
        for i in range(i):
            output.append(np.random.multivariate_normal(means[gmm],covs[gmm]))
        gmm+=1
    return np.array(output)

mean1=[0,0]
mean2=[0,2]
mean3=[0,-2]
mean4=[5,-5]
mean5=[2,-1]
means=[mean1,mean2,mean3,mean4,mean5]
cov1=[[2,0],[0,0.2]]
cov2=[[2,0],[0,0.2]]
cov3=[[2,0],[0,0.2]]
cov4=[[2,0],[0,0.2]]
cov5=[[20,0],[0,20]]
covs=[cov1,cov2,cov3,cov4,cov5]
probs=[0.15,0.15,0.15,0.15,0.4]
X=sample_GMM(means,covs,probs,1000)
plt.title('Guassian Generated Data')
plt.scatter(X[:,0],X[:,1],alpha=0.2,s=10)
plt.show()
unsupervised=MdlGmm(plots=True)
unsupervised.fit(X)
samples=unsupervised.sample(1000)

plt.title('Sampled from GMM')
plt.scatter(samples[:,0],samples[:,1],alpha=0.2,s=10)
plt.show()


