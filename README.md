# Unsupervised Learning of Finite Gaussian Mixture Models

Original [paper](http://www.lx.it.pt/~mtf/IEEE_TPAMI_2002.pdf)

Unsupervised learning of Gaussian mixture models uses a minimum message length like criterion to learn the optimal number of components in a finite Gaussian mixture model.

## Installation

To install this python package:

```bash
pip install mml_gmm
```
This implementation is a port from the orginal authors [matlab](http://www.lx.it.pt/~mtf/mixturecode2.zip) code with small modifications and it is built as a sklearn wrapper. The dependencies are:

```python
numpy
scipy
sklearn
```
To run the example scripts it also advisable to install `matplotlib`

It should be compatible with python2 and python3

## Usage

The following points were generated using three bivariate Gaussian distributions. 

<p align="center">
  <img src="./figures/generated_data.png" width="400" /> 
  <img src="./figures/best_number_components.png" width="400"  />
</p>
The clustering algorithm correctly converges to those distributions:

```python
from mml_gmm import MmlGmm

unsupervised=MmlGmm(plots=True)
unsupervised.fit(X)
```

It is also possible to visualize this process `MmlGmm(plots=True,live_2d_plot=False)`:

<p align="center"> 
  <img src="./figures/animated.gif" width="500"  />
</p>

Available sklearn methods:

- `.fit()` - fit the finite mixture model
- `.fit_transform()` - fit and return inputs posterior probability
- `.transform()` - return inputs posterior probability
- `.predict()` - return inputs cluster
- `.predict_proba()` - same as `.transform()`
- `.sample()` - sample new data from the fitted mixture model


## Examples

On folders ./example_scipts and ./tutorials there are examples on how to use the code

An example jupyter notebook is provided [link](./notebooks/tutorial.ipynb)

## TODO

* Refactoring
* Docs
* Make it work with 1-d data (bug)
* Support other covariance types (right now only 'full' is supported, i.e., each component has its own general covariance matrix)