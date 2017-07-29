# Unsupervised Learning of Guassian Mixture Models

Original [paper](http://www.lx.it.pt/~mtf/IEEE_TPAMI_2002.pdf)

Unsupervised learning of guassian mixture models uses a minimum message length like criterion to learn the optimal number of components in a finite guassian mixture model. 

To install this python package:
```
pip install mml_gmm
```
An example jupyter notebook is provided [link](./notebooks/tutorial.ipynb)

<p float="left">
  <img src="./figures/best_number_components.png" width="400" /> 
  <img src="./figures/animated.gif" width="470" />
</p>

This implementation is a port from the orginal authors [matlab](http://www.lx.it.pt/~mtf/mixturecode2.zip) code with small modifications and it is built as a sklearn wrapper. The dependencies are:
```
numpy
scipy
sklearn
```
To run the example scripts it also advisable to install `matplotlib`

This code is a work in progress and it needs a lot of refactoring. It is supposed to be compatible with python2 and python3
