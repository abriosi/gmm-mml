# Unsupervised Learning of Finite Gaussian Mixture Models

## References

[[1]](http://www.lx.it.pt/~mtf/IEEE_TPAMI_2002.pdf)
M. A. T. Figueiredo and A. K. Jain, "Unsupervised learning of finite mixture models," in IEEE Transactions on Pattern Analysis and Machine Intelligence, vol. 24, no. 3, pp. 381-396, March 2002.

## Installation

Install this python package:

```bash
pip install gmm-mml
```

This implementation is a port from the orginal authors [matlab](http://www.lx.it.pt/~mtf/mixturecode2.zip) code with small modifications and it is built as a sklearn wrapper. The dependencies are:

```
numpy
scipy
sklearn
matplotlib (optional)
```

## Usage

The following points were generated using three bivariate Gaussian distributions.

<p align="center">
  <img src="./figures/generated_data.png" width="400" />
  <img src="./figures/best_number_components.png" width="400"  />
</p>
The clustering algorithm correctly converges to those distributions:

```python
from gmm_mml import GmmMml

unsupervised=GmmMml(plots=True)
unsupervised.fit(X)
```

It is also possible to visualize this process `GmmMml(plots=True,live_2d_plot=False)`:

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

Jupyter notebooks: [2d_Example](./notebooks/tutorial.ipynb) [1d_Example](./notebooks/tutorial-1D-example.ipynb)

## TODO

- Refactoring
- Docs
- Support other covariance types (right now only 'full' is supported, i.e., each component has its own general covariance matrix)
