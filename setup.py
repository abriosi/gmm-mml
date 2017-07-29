from setuptools import setup

setup(name='mml_gmm',
      version='0.1',
      description='Unsupervised cluster selection',
      url='https://github.com/abriosi/mml_gmm/',
      author='abriosi',
      license='MIT',
      packages=['mml_gmm'],
      install_requires=[
          'numpy',
          'scipy',
          'sklearn',
      ],
      zip_safe=False)
