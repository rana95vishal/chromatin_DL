# chromatin_DL
Dictionary learning for ChIA-Drop experiments with online convex matrix factorization

This is a repository for the paper "Online Convex Network Dictionary Learning for Inferring Chromatin Interactions."

The algorithm has two major components: an MCMC-based network subsampling and an iterative optimization to learn the dictionary. 

## Example with Synthetic Data

 We provide synthetic data generated by the Stochastic Block Model (SBM) for verification. To run just the optimization step for quick verification on the synthetic dataset, use
```
source run_example.sh
```
### Details of the pipeline

1. Raw data in the form of lists of edges for various SBM networks can be found in the sub-folder 'sampling\Data\synthetic\'.
2. To run the MCMC sampling procedure, use the script '''sampling\generate_synthetic_samples.py'''.
   ```
   source run_example.sh
   ```
3. The results
## Packages
The following packages are needed to run the code
```
python=3.8
pandas
matplotlib
ipdb
tqdm
scikit-learn
k-means-constrained
cvxpy
networkx
tensorly
psutil
```
