from setuptools import setup

setup(name='gmm-mml',
      version='0.11',
      description='Unsupervised cluster selection for finite guassian mixture models',
      url='https://github.com/abriosi/gmm-mml/',
      author='abriosi',
      license='MIT',
      packages=['gmm_mml'],
      install_requires=[
          'numpy',
          'scipy',
          'sklearn',
      ],
      zip_safe=False)
